import sqlite3
import hashlib
from datetime import datetime

DB_NAME = "database_pro.db"

def init_db():
    """Inizializza il database e crea le tabelle se non esistono"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # Tabella Utenti
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (username TEXT PRIMARY KEY, password TEXT, signup_date TEXT, status TEXT)''')
    
    # Tabella Storico Recensioni
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

def check_auth(user, pw, admin_user, admin_pw):
    """Verifica le credenziali e lo stato dell'abbonamento"""
    if user == admin_user and pw == admin_pw:
        return True, "admin", 999
    
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

# --- GESTIONE STORICO E RINOMINA ---

def save_review(username, biz_type, biz_desc, review, response):
    """Salva una nuova risposta generata nello storico dell'utente"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO history (username, biz_type, biz_desc, review, response, date) VALUES (?, ?, ?, ?, ?, ?)", 
              (username, biz_type, biz_desc, review, response, now))
    conn.commit()
    conn.close()

def get_history(username):
    """Recupera le ultime 10 risposte generate dall'utente"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT biz_type, review, response, date, biz_desc FROM history WHERE username=? ORDER BY date DESC LIMIT 10", (username,))
    res = c.fetchall()
    conn.close()
    return res

def delete_history_item(username, date):
    """Elimina definitivamente una specifica chat dallo storico"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM history WHERE username=? AND date=?", (username, date))
    conn.commit()
    conn.close()

def rename_history_item(username, old_date, new_name):
    """Aggiorna l'etichetta (campo date) di un'analisi salvata"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Aggiorniamo il campo 'date' che viene usato come titolo nella sidebar
    c.execute("UPDATE history SET date = ? WHERE username = ? AND date = ?", 
              (new_name, username, old_date))
    conn.commit()
    conn.close()

def get_last_biz_desc(username):
    """Recupera l'ultima descrizione attività usata per pre-compilare la sidebar"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT biz_desc FROM history WHERE username=? ORDER BY date DESC LIMIT 1", (username,))
    res = c.fetchone()
    conn.close()
    return res[0] if res else ""

def activate_user_db(username):
    """Passa un utente da status 'trial' a 'active' (Admin)"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET status='active' WHERE username=?", (username,))
    conn.commit()
    conn.close()