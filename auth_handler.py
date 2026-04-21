import sqlite3
import hashlib
from datetime import datetime

DB_NAME = "database_pro.db"

def init_db():
    """Inizializza il database e crea le tabelle se non esistono"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (username TEXT PRIMARY KEY, password TEXT, signup_date TEXT, status TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS history 
                 (username TEXT, biz_type TEXT, biz_desc TEXT, review TEXT, response TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def hash_pw(password):
    """Cripta la password in SHA-256"""
    return hashlib.sha256(str.encode(password)).hexdigest()

def register_user(user, pw):
    """Registra un nuovo utente nel sistema"""
    init_db()
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        today = datetime.now().strftime("%Y-%m-%d")
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", 
                  (user, hash_pw(pw), today, 'trial'))
        conn.commit()
        return True, "Registrazione completata! Accedi ora."
    except sqlite3.IntegrityError:
        return False, "Errore: questo Username esiste già."
    finally:
        conn.close()

def check_auth(user, pw):
    """Verifica le credenziali e lo stato dell'abbonamento"""
    if user == "admin" and pw == "VLLMTT":
        return True, "active", 999
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT password, signup_date, status FROM users WHERE username=?", (user,))
    res = c.fetchone()
    conn.close()

    if res and res[0] == hash_pw(pw):
        status = res[2]
        if status == "active":
            return True, "active", 999
        
        signup_date = datetime.strptime(res[1], "%Y-%m-%d")
        days_passed = (datetime.now() - signup_date).days
        remaining = 14 - days_passed
        
        if remaining > 0:
            return True, "trial", remaining
        else:
            return False, "expired", 0
            
    return False, "wrong", 0

def save_review(username, biz_type, biz_desc, review, response):
    """Salva una nuova risposta generata nello storico"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO history (username, biz_type, biz_desc, review, response, date) VALUES (?, ?, ?, ?, ?, ?)", 
              (username, biz_type, biz_desc, review, response, now))
    conn.commit()
    conn.close()

def get_history(username):
    """Recupera lo storico"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT biz_type, review, response, date, biz_desc FROM history WHERE username=? ORDER BY date DESC LIMIT 10", (username,))
    res = c.fetchall()
    conn.close()
    return res

# --- FUNZIONI DI MANUTENZIONE STORICO (Quelle che mancavano!) ---

def rename_history_item(username, old_date, new_name):
    """Rinomina un'analisi nello storico"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE history SET date = ? WHERE username = ? AND date = ?", 
              (new_name, username, old_date))
    conn.commit()
    conn.close()

def delete_history_item(username, date):
    """Elimina un'analisi dallo storico"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM history WHERE username=? AND date=?", (username, date))
    conn.commit()
    conn.close()

# --- FUNZIONI ADMIN ---

def get_all_users():
    """Recupera tutti gli utenti per il pannello Admin"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT username, signup_date, status FROM users WHERE username != 'admin'")
    rows = c.fetchall()
    conn.close()
    
    users = []
    for row in rows:
        users.append({
            "username": row["username"],
            "signup_date": row["signup_date"],
            "active": True if row["status"] == "active" else False
        })
    return users

def toggle_user_status(username):
    """Attiva o disattiva un utente"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT status FROM users WHERE username=?", (username,))
    res = c.fetchone()
    if res:
        new_status = "active" if res[0] != "active" else "trial"
        c.execute("UPDATE users SET status=? WHERE username=?", (new_status, username))
        conn.commit()
    conn.close()