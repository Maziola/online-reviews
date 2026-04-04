import streamlit as st
import pandas as pd
from styles import get_logo_html, apply_custom_styles

# 1. Configurazione della Pagina (Tab del browser)
st.set_page_config(
    page_title="Reviews Master Pro",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inizializzazione Session State per Autenticazione
if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'user_role' not in st.session_state:
    st.session_state.user_role = None

# 3. Applicazione Stili CSS Personalizzati
apply_custom_styles()

# --- LOGICA DI AUTENTICAZIONE (LOGIN) ---
if not st.session_state.auth:
    # Mostra il LOGO DEFINITIVO al centro
    st.markdown(get_logo_html(size=300), unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center;'>Benvenuto in Reviews Master Pro</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>La piattaforma AI per l'eccellenza nelle recensioni</p>", unsafe_allow_html=True)

    # Box di Login
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            tab1, tab2 = st.tabs(["Accedi", "Registrati"])
            
            with tab1:
                with st.form("login_form"):
                    email = st.text_input("Email")
                    password = st.text_input("Password", type="password")
                    submit = st.form_submit_button("Entra")
                    
                    if submit:
                        # Logica di test (puoi personalizzarla)
                        if email == "admin" and password == "admin":
                            st.session_state.auth = True
                            st.session_state.user_role = "Admin"
                            st.rerun()
                        else:
                            st.error("Credenziali non valide")
            
            with tab2:
                st.info("La registrazione è attualmente limitata ai partner invitati.")

# --- DASHBOARD PRINCIPALE (DOPO IL LOGIN) ---
else:
    # Barra Laterale (Sidebar)
    with st.sidebar:
        st.markdown(get_logo_html(size=120), unsafe_allow_html=True)
        st.markdown("---")
        st.write(f"👤 Utente: **{st.session_state.user_role}**")
        menu = st.radio("Menu Principale", ["Dashboard", "Analisi Recensioni", "Generatore Risposte", "Impostazioni"])
        
        if st.button("Esci"):
            st.session_state.auth = False
            st.rerun()

    # Contenuto Principale basato sul Menu
    st.title(f"🚀 {menu}")
    
    if menu == "Dashboard":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Recensioni Totali", "1,254", "+12%")
        with col2:
            st.metric("Rating Medio", "4.8/5", "+0.2")
        with col3:
            st.metric("Risposte AI Generate", "890", "95% successo")
            
        st.markdown("### 📈 Panoramica Prestazioni")
        # Placeholder per un grafico
        chart_data = pd.DataFrame([10, 20, 15, 30, 45, 50], columns=["Performance"])
        st.line_chart(chart_data)

    elif menu == "Analisi Recensioni":
        st.subheader("Carica le tue recensioni per l'analisi del sentiment")
        uploaded_file = st.file_uploader("Scegli un file CSV o Excel", type=["csv", "xlsx"])
        if uploaded_file:
            st.success("File caricato con successo! Analisi in corso...")

    elif menu == "Generatore Risposte":
        st.subheader("Generatore di risposte intelligenti")
        review_text = st.text_area("Incolla qui la recensione del cliente:")
        tone = st.select_slider("Seleziona il tono della risposta", options=["Formale", "Amichevole", "Entusiasta"])
        if st.button("Genera Risposta con AI"):
            st.info("L'AI sta scrivendo una risposta perfetta per te...")
            st.markdown(f"**Risposta Suggerita ({tone}):**")
            st.write("Gentile cliente, grazie mille per il tuo feedback positivo! Siamo felici che tu abbia apprezzato il nostro servizio. Speriamo di rivederti presto!")

    elif menu == "Impostazioni":
        st.subheader("Configurazione Account")
        st.checkbox("Notifiche Email")
        st.checkbox("Risposta Automatica (Beta)")
