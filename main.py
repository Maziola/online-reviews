import streamlit as st
from openai import OpenAI

# IMPORTIAMO LE FUNZIONI DAI TUOI FILE .PY
from styles import apply_custom_styles, get_logo_html
from database import salva_dato_silenzioso, carica_dati, registra_utente, verifica_utente

# Configurazione Pagina
st.set_page_config(page_title="Reviews Master Pro", layout="centered")
apply_custom_styles()

# Inizializzazione Sessione
if "auth" not in st.session_state: st.session_state.auth = False
if "user" not in st.session_state: st.session_state.user = None

# --- LOGICA DI ACCESSO / REGISTRAZIONE ---
if not st.session_state.auth:
    st.markdown(get_logo_html(120), unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Reviews Master Pro</h1>", unsafe_allow_html=True)
    
    # BOX DI LOGIN/REGISTRAZIONE
    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        
        # IL SELETTORE: Se non lo vedi, controlla di aver salvato main.py
        modalita = st.radio("Cosa vuoi fare?", ["Accedi", "Registrati"], horizontal=True)
        
        user_input = st.text_input("Username", key="login_user")
        pass_input = st.text_input("Password", type="password", key="login_pass")
        
        if modalita == "Accedi":
            if st.button("ENTRA", type="primary", use_container_width=True):
                username = verifica_utente(user_input, pass_input)
                if username:
                    st.session_state.auth = True
                    st.session_state.user = username
                    st.rerun()
                else:
                    st.error("Credenziali errate o utente inesistente.")
        
        else: # REGISTRAZIONE
            st.info("Scegli un username e una password per creare il tuo account.")
            if st.button("CREA ACCOUNT", type="primary", use_container_width=True):
                if registra_utente(user_input, pass_input):
                    st.success("✅ Account creato! Ora seleziona 'Accedi' sopra.")
                else:
                    st.error("❌ Errore: Username già preso o campi vuoti.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- DASHBOARD (Dopo il Login) ---
st.markdown(f"### Benvenuto, {st.session_state.user} 👋")

t1, t2 = st.tabs(["✨ Scrivi Risposta", "📊 I tuoi Trend"])

with t1:
    col1, col2 = st.columns(2)
    with col1:
        biz = st.selectbox("Attività", ["Hotel", "Ristorante", "B&B", "Negozio"])
        tone = st.selectbox("Tono", ["Professionale", "Amichevole", "Empatico"])
    with col2:
        rev_text = st.text_area("Incolla recensione", height=150)
    
    if st.button("Genera Risposte ✨", type="primary", use_container_width=True):
        if rev_text:
            # Salvataggio dati per i trend
            salva_dato_silenzioso(biz, tone)
            
            # Qui andrebbe la chiamata OpenAI. Per ora simuliamo:
            st.markdown("---")
            st.markdown('<div class="variant-card"><strong>Variante 1</strong><br>Grazie per la tua visita! Ci fa piacere...</div>', unsafe_allow_html=True)
            st.success("Risposta salvata nei trend!")
        else:
            st.warning("Inserisci il testo della recensione.")

with t2:
    st.subheader("Statistiche Generali")
    dati = carica_dati()
    if dati is not None:
        st.line_chart(dati.groupby("Data").size())
        st.dataframe(dati, use_container_width=True)
    else:
        st.info("Ancora nessun dato. Inizia a generare risposte!")

if st.sidebar.button("Logout"):
    st.session_state.auth = False
    st.rerun()