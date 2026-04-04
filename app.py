import streamlit as st
from styles import get_logo_html, apply_custom_styles

# Configurazione base della pagina
st.set_page_config(page_title="Reviews Master Pro", layout="wide")
apply_custom_styles()

if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # Mostra prima il logo definitivo, ben separato dalla scritta
    st.markdown(get_logo_html(150), unsafe_allow_html=True)
    
    # Crea una colonna centrale per il form di login
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            st.markdown("<h3 style='text-align: center;'>Area Riservata</h3>", unsafe_allow_html=True)
            user = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Accedi"):
                # Sostituisci con la tua logica di autenticazione
                if user == "admin" and password == "admin":
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Credenziali errate")
else:
    # Sidebar con logo piccolo
    with st.sidebar:
        st.markdown(get_logo_html(80), unsafe_allow_html=True)
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()
    
    st.title("Dashboard Reviews Master Pro")
    st.write("Benvenuto nel tuo pannello di controllo professionale per la gestione delle recensioni.")
