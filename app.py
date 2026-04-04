import streamlit as st
from styles import get_logo_html, apply_custom_styles

# Configurazione obbligatoria come prima riga
st.set_page_config(page_title="Reviews Master Pro", layout="centered")

# Applica lo stile
apply_custom_styles()

if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # 1. Logo e Titolo fuori dalla card per massima visibilità
    st.markdown(get_logo_html(100), unsafe_allow_html=True)
    
    # 2. Form di Login
    with st.form("login_box"):
        st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Area Riservata</h3>", unsafe_allow_html=True)
        user = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        submit = st.form_submit_button("Accedi")
        
        if submit:
            if user == "admin" and password == "admin":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Credenziali non valide")
else:
    st.success("Accesso effettuato!")
    if st.button("Esci"):
        st.session_state.auth = False
        st.rerun()
