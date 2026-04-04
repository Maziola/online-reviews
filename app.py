import streamlit as st
from styles import get_logo_html, apply_custom_styles

# Configurazione iniziale
st.set_page_config(page_title="Reviews Master Pro", layout="centered")
apply_custom_styles()

if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # Mostra Logo e Titolo
    st.markdown(get_logo_html(100), unsafe_allow_html=True)
    
    # Navigazione Accedi/Registrati
    tab_login, tab_reg = st.tabs(["ACCEDI", "REGISTRATI"])
    
    with tab_login:
        with st.form("login"):
            username = st.text_input("Username", placeholder="Inserisci il tuo username")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            if st.form_submit_button("ACCEDI"):
                if username == "admin" and password == "admin":
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Credenziali non valide")

    with tab_reg:
        with st.form("register"):
            st.text_input("Nome Completo")
            st.text_input("Email")
            st.text_input("Nuova Password", type="password")
            if st.form_submit_button("CREA ACCOUNT"):
                st.success("Registrazione completata!")

else:
    # Dashboard post-login
    st.markdown("<h2 style='color:white; text-align:center;'>Dashboard attiva</h2>", unsafe_allow_html=True)
    if st.button("Logout"):
        st.session_state.auth = False
        st.rerun()
