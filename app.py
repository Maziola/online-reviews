import streamlit as st
from styles import get_logo_html, apply_custom_styles

# Configurazione Pagina
st.set_page_config(page_title="Reviews Master Pro", layout="centered")
apply_custom_styles()

if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # Intestazione con Logo e Titolo
    st.markdown(get_logo_html(110), unsafe_allow_html=True)
    
    # Sistema a Tab per Accedi/Registrati
    tab_login, tab_reg = st.tabs(["ACCEDI", "REGISTRATI"])
    
    with tab_login:
        with st.form("login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("ACCEDI"):
                if username == "admin" and password == "admin":
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Credenziali non corrette")

    with tab_reg:
        with st.form("registration"):
            full_name = st.text_input("Nome Completo")
            email = st.text_input("Email")
            new_password = st.text_input("Scegli Password", type="password")
            
            if st.form_submit_button("CREA ACCOUNT"):
                st.success("Account creato! Ora puoi effettuare l'accesso.")

else:
    # Contenuto Dashboard (dopo il login)
    st.markdown("<h2 style='color:white;'>Benvenuto nella tua Dashboard</h2>", unsafe_allow_html=True)
    if st.button("Logout"):
        st.session_state.auth = False
        st.rerun()
