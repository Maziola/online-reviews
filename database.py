import pandas as pd
from datetime import datetime
import os
import hashlib

# --- SICUREZZA PASSWORD ---
def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# --- GESTIONE UTENTI ---
def registra_utente(username, password):
    file_path = 'users.csv'
    username = username.strip()
    if not username or not password:
        return False
    
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path)
        if username in df['username'].values:
            return False # Utente esiste già
    
    nuovo = pd.DataFrame([{"username": username, "password": hash_password(password)}])
    if os.path.isfile(file_path):
        nuovo.to_csv(file_path, mode='a', index=False, header=False)
    else:
        nuovo.to_csv(file_path, index=False)
    return True

def verifica_utente(username, password):
    file_path = 'users.csv'
    if not os.path.isfile(file_path):
        return None
    df = pd.read_csv(file_path)
    hashed_p = hash_password(password)
    valido = df[(df['username'] == username.strip()) & (df['password'] == hashed_p)]
    return username.strip() if not valido.empty else None

# --- GESTIONE STORICO ---
def salva_dato_silenzioso(biz_type, tone):
    file_path = 'history.csv'
    nuovo = pd.DataFrame([{
        "Data": datetime.now().strftime("%Y-%m-%d"),
        "Attivita": biz_type,
        "Tono": tone,
        "Conteggio": 1
    }])
    if os.path.isfile(file_path):
        nuovo.to_csv(file_path, mode='a', index=False, header=False)
    else:
        nuovo.to_csv(file_path, index=False)

def carica_dati():
    if os.path.isfile('history.csv'):
        return pd.read_csv('history.csv')
    return None