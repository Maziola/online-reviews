import streamlit as st

def get_logo_html(size=100):
    """
    Logo Premium: Omino Blu con Costellazione di Stelle Oro.
    """
    return f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="width: {size}px; height: {size}px;">
            <path d="M12 1L13.5 5.5H18L14.5 8L16 12.5L12 10L8 12.5L9.5 8L6 5.5H10.5L12 1z" fill="#D4AF37"/>
            <path d="M5 4L5.8 6H8L6.2 7.2L7 9L5 7.8L3 9L3.8 7.2L2 6H4.2L5 4z" fill="#D4AF37" opacity="0.6"/>
            <path d="M19 4L19.8 6H22L20.2 7.2L21 9L19 7.8L17 9L17.8 7.2L16 6H18.2L19 4z" fill="#D4AF37" opacity="0.6"/>
            <circle cx="12" cy="14" r="3" fill="#367588"/>
            <path d="M12 18c-4 0-6 2-6 4v1h12v-1c0-2-2-4-6-4z" fill="#367588"/>
        </svg>
        <div style="margin-top: 10px;">
            <span style="font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 800; color: #E0E0E0; letter-spacing: 1px;">REVIEWS MASTER</span>
            <span style="font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 300; color: #367588; margin-left: 5px;">PRO</span>
        </div>
    </div>
    """

def apply_custom_styles():
    """
    Design Dark Moderno con Card ad alto contrasto.
    """
    st.markdown("""
    <style>
        /* Sfondo Pagina */
        .stApp {
            background-color: #0B0E14;
        }

        /* Container Login */
        .login-container {
            max-width: 450px;
            margin: auto;
            background: #161B22;
            padding: 40px;
            border-radius: 20px;
            border: 1px solid #30363D;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }

        /* Input Fields */
        .stTextInput input {
            background-color: #0D1117 !important;
            color: white !important;
            border: 1px solid #30363D !important;
            border-radius: 10px !important;
            padding: 12px !important;
        }

        /* Tabs (Accedi / Registrati) */
        .stTabs [data-baseweb="tab-list"] {
            gap: 20px;
            background-color: transparent;
        }
        .stTabs [data-baseweb="tab"] {
            color: #8B949E;
            font-weight: 600;
        }
        .stTabs [aria-selected="true"] {
            color: #367588 !important;
            border-bottom-color: #367588 !important;
        }

        /* Pulsante Principale */
        div.stButton > button {
            background: linear-gradient(135deg, #367588 0%, #1F4788 100%) !important;
            color: white !important;
            border: none !important;
            padding: 15px !important;
            border-radius: 12px !important;
            width: 100% !important;
            font-weight: 700 !important;
            transition: transform 0.2s;
        }
        div.stButton > button:hover {
            transform: scale(1.02);
        }
    </style>
    """, unsafe_allow_html=True)
