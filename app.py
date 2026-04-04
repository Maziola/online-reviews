import streamlit as st
from openai import OpenAI

# IMPORTIAMO LE FUNZIONI DAI TUOI FILE .PY
from styles import apply_custom_styles, get_logo_html
from database import salva_dato_silenzioso, carica_dati, registra_utente, verifica_utente

# 1. Configurazione Pagina (LAYOUT WIDE per occupare tutto lo schermo)
st.set_page_config(page_title="Reviews Master Pro", layout="wide", initial_sidebar_state="collapsed")
apply_custom_styles()

# Inizializzazione Sessione
if "auth" not in st.session_state: st.session_state.auth = False
if "user" not in st.session_state: st.session_state.user = None

# --- LOGICA DI ACCESSO / REGISTRAZIONE ---
if not st.session_state.auth:
    st.markdown(get_logo_html(120), unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Reviews Master Pro</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="login-box" style="max-width: 500px; margin: 0 auto;">', unsafe_allow_html=True)
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
        else:
            if st.button("CREA ACCOUNT", type="primary", use_container_width=True):
                if registra_utente(user_input, pass_input):
                    st.success("✅ Account creato! Ora seleziona 'Accedi'.")
                else:
                    st.error("❌ Errore: Username già preso o campi vuoti.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- DASHBOARD (Layout Wide) ---
st.markdown(f"### Benvenuto, {st.session_state.user} 👋")

t1, t2 = st.tabs(["✨ Scrivi Risposta", "📊 I tuoi Trend"])

with t1:
    # Divisore in due grandi colonne
    col1, col2 = st.columns([1, 2]) # Colonna sinistra più stretta, destra più larga
    
    with col1:
        st.subheader("Configura la risposta")
        
        # ATTIVITÀ (Lista completa + Altro)
        lista_attivita = ["Hotel", "Ristorante", "B&B", "Negozio", "Bar", "Pizzeria", "Agriturismo", "Centro Estetico", "Altro"]
        biz = st.selectbox("Tipo di Attività", lista_attivita)
        
        # Se seleziona "Altro", appare il campo testo libero
        biz_custom = ""
        if biz == "Altro":
            biz_custom = st.text_input("Specifica attività...", placeholder="Esempio: Palestra")

        # TONO (Lista ampliata)
        lista_toni = ["Professionale", "Amichevole", "Empatico", "Elegante", "Ironico", "Formale", "Diretto"]
        tone = st.selectbox("Tono della Risposta", lista_toni)

        # BOX INFO AGGIUNTIVE (Scomparso e ora tornato!)
        extra_info = st.text_area("Informazioni extra per l'IA", 
                                 placeholder="Esempio: Offri uno sconto del 10% per la prossima volta o menziona che abbiamo rinnovato la piscina.",
                                 help="Aggiungi dettagli specifici che vuoi includere nella risposta.")

    with col2:
        st.subheader("Inserisci la Recensione")
        rev_text = st.text_area("Incolla qui il testo del cliente", height=280)
        
        if st.button("Genera Risposte Professionali ✨", type="primary", use_container_width=True):
            if rev_text:
                # Usiamo l'attività custom se presente
                attivita_finale = biz_custom if biz == "Altro" else biz
                salva_dato_silenzioso(attivita_finale, tone)
                
                # Simulazione Risposta (Pronto per OpenAI)
                st.markdown("---")
                st.info("🤖 **L'Intelligenza Artificiale sta scrivendo...**")
                
                # Box Risultato
                st.markdown(f'''
                <div class="variant-card" style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b;">
                    <strong>Bozza Generata:</strong><br><br>
                    Gentile cliente, grazie per aver scelto il nostro {attivita_finale}. 
                    Ci fa molto piacere che abbia apprezzato il servizio. {extra_info if extra_info else ""}
                    Speriamo di rivederla presto!
                </div>
                ''', unsafe_allow_html=True)
                
                st.success("Risposta generata con successo!")
            else:
                st.warning("⚠️ Per favore, incolla prima una recensione.")

with t2:
    st.subheader("Analisi Storica")
    dati = carica_dati()
    if dati is not None and not dati.empty:
        col_stats1, col_stats2 = st.columns(2)
        with col_stats1:
            st.line_chart(dati.groupby("Data").size())
        with col_stats2:
            st.write("Dettaglio ultime attività:")
            st.dataframe(dati, use_container_width=True)
    else:
        st.info("Nessun dato disponibile nei trend. Inizia a generare risposte!")

# Tasto Logout in Sidebar
with st.sidebar:
    st.markdown("---")
    if st.button("LOGOUT"):
        st.session_state.auth = False
        st.rerun()
