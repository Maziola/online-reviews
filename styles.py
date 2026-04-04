import streamlit as st

def get_logo_html(size=120):
    """
    Logo SVG pulito: Omino sopra, scritta sotto, ben spaziati.
    """
    return f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 40px; width: 100%;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" style="width: {size}px; height: {size}px;">
            <path d="M12 2l1.2 3.6h3.8l-3 2.2 1.1 3.7-3.1-2.3-3.1 2.3 1.1-3.7-3-2.2h3.8z" fill="#FFD700"/>
            <circle cx="12" cy="13" r="3" fill="#1F4788"/>
            <path d="M12 17c-4 0-6 2-6 4v1h12v-1c0-2-2-4-6-4z" fill="#1F4788"/>
        </svg>
        <div style="margin-top: 15px; text-align: center;">
            <span style="font-family: 'Helvetica Neue', sans-serif; font-size: 28px; font-weight: 800; color: #1F4788; letter-spacing: 1px;">REVIEWS MASTER</span>
            <span style="font-family: 'Helvetica Neue', sans-serif; font-size: 28px; font-weight: 300; color: #367588; margin-left: 5px;">PRO</span>
        </div>
    </div>
    """

def apply_custom_styles():
    """
    Forza il tema chiaro e pulito indipendentemente dalle impostazioni del browser.
    """
    st.markdown("""
    <style>
        /* Forza lo sfondo della pagina a essere scuro/elegante per far risaltare la card */
        .stApp {
            background-color: #0e1117;
        }

        /* La Card di Login: Bianca, pulita, moderna */
        div[data-testid="stForm"] {
            background-color: #ffffff !important;
            border-radius: 20px !important;
            padding: 50px !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3) !important;
            border: none !important;
            max-width: 450px;
            margin: auto;
        }

        /* Testo dentro la card (Username, Password, Titoli) */
        div[data-testid="stForm"] h3, 
        div[data-testid="stForm"] label,
        div[data-testid="stForm"] p {
            color: #1F4788 !important;
            font-weight: 600 !important;
        }

        /* Campi di input: sfondo grigio chiaro, testo scuro */
        div[data-testid="stForm"] input {
            background-color: #f0f2f6 !important;
            color: #0e1117 !important;
            border-radius: 10px !important;
        }

        /* Pulsante "Accedi" Moderno (Teal/Blu) */
        div.stButton > button {
            background-color: #367588 !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            height: 3.5em !important;
            width: 100% !important;
            font-weight: bold !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 20px;
        }
    </style>
    """, unsafe_allow_html=True)
