import streamlit as st
from styles import get_logo_html, apply_custom_styles

st.set_page_config(page_title="Reviews Master Pro", layout="centered")
apply_custom_styles()

if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # Intestazione fuori dalla card
    st.markdown(get_logo_html(110), unsafe_allow_html=True)
    
    # Tabs per Accedi e Registrati
    tab_login, tab_reg = st.tabs(["🔑 ACCEDI", "📝 REGISTRATI"])
    
    with tab_login:
        with st.form("login"):
            user = st.text_input("Username o Email")
            pw = st.text_input("Password", type="password")
            if st.form_submit_button("ENTRA NELLA DASHBOARD"):
                if user == "admin" and pw == "admin":
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Credenziali non valide")

    with tab_reg:
        with st.form("registration"):
            new_user = st.text_input("Nome Completo")
            new_email = st.text_input("Email Aziendale")
            new_pw = st.text_input("Scegli Password", type="password")
            plan = st.selectbox("Piano desiderato", ["Starter", "Professional", "Enterprise"])
            if st.form_submit_button("CREA ACCOUNT PRO"):
                st.success("Richiesta inviata! Riceverai un'email di conferma.")

else:
    st.markdown(f"<h1 style='color:white;'>Benvenuto in Master Pro</h1>", unsafe_allow_html=True)
    if st.button("Logout"):
        st.session_state.auth = False
        st.rerun()
