import streamlit as st
from styles import get_logo_html, apply_custom_styles

st.set_page_config(page_title="Reviews Master Pro", layout="centered")
apply_custom_styles()

if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # Logo e Titolo
    st.markdown(get_logo_html(100), unsafe_allow_html=True)
    
    # Navigazione
    tab_login, tab_reg = st.tabs(["ACCEDI", "REGISTRATI"])
    
    with tab_login:
        with st.form("login"):
            st.markdown("<h3 style='text-align: center; margin-top: 0;'>Area Riservata</h3>", unsafe_allow_html=True)
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("ACCEDI"):
                if username == "admin" and password == "admin":
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Credenziali non valide")

    with tab_reg:
        with st.form("registration"):
            st.markdown("<h3 style='text-align: center; margin-top: 0;'>Nuovo Account</h3>", unsafe_allow_html=True)
            st.text_input("Nome Completo")
            st.text_input("Email")
            st.text_input("Password", type="password")
            if st.form_submit_button("CREA ACCOUNT"):
                st.success("Registrazione completata correttamente!")

else:
    st.markdown("<h2 style='color:white; text-align:center;'>Dashboard</h2>", unsafe_allow_html=True)
    if st.button("Logout"):
        st.session_state.auth = False
        st.rerun()
