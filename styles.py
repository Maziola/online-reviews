import streamlit as st

def get_logo_html(size=100):
    """
    Logo Premium: Omino Blu e Stelle Oro.
    """
    return f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding-bottom: 25px;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="width: {size}px; height: {size}px;">
            <path d="M12 1L13.5 5.5H18L14.5 8L16 12.5L12 10L8 12.5L9.5 8L6 5.5H10.5L12 1z" fill="#D4AF37"/>
            <path d="M5 4L5.8 6H8L6.2 7.2L7 9L5 7.8L3 9L3.8 7.2L2 6H4.2L5 4z" fill="#D4AF37" opacity="0.6"/>
            <path d="M19 4L19.8 6H22L20.2 7.2L21 9L19 7.8L17 9L17.8 7.2L16 6H18.2L19 4z" fill="#D4AF37" opacity="0.6"/>
            <circle cx="12" cy="14" r="3" fill="#367588"/>
            <path d="M12 18c-4 0-6 2-6 4v1h12v-1c0-2-2-4-6-4z" fill="#367588"/>
        </svg>
        <div style="margin-top: 15px; text-align: center;">
            <span style="font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 800; color: #FFFFFF; letter-spacing: 1.5px;">REVIEWS MASTER</span>
            <span style="font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 300; color: #367588; margin-left: 5px;">PRO</span>
        </div>
    </div>
    """

def apply_custom_styles():
    """
    Design avanzato: Contrasto migliorato e leggibilità dei tasti garantita.
    """
    st.markdown("""
    <style>
        /* Sfondo profondo */
        .stApp {
            background-color: #0B0E14;
        }

        /* Card di Login: Bianco morbido con ombra soft */
        [data-testid="stForm"] {
            background-color: #F8F9FA !important;
            border-radius: 20px !important;
            padding: 40px !important;
            box-shadow: 0 15px 35px rgba(0,0,0,0.5) !important;
            border: none !important;
        }

        /* Label (Username/Password): Grigio scuro per contrasto su bianco */
        [data-testid="stForm"] label p {
            color: #1F2937 !important;
            font-weight: 600 !important;
            font-size: 15px !important;
        }

        /* Input Fields: Bianco puro con bordo sottile */
        input {
            background-color: #FFFFFF !important;
            color: #111827 !important;
            border: 1px solid #D1D5DB !important;
            border-radius: 10px !important;
            padding: 12px !important;
        }

        /* PULSANTI: Sfondo Teal e TESTO BIANCO (Garantito) */
        div.stButton > button {
            background-color: #367588 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 50px !important;
            height: 3.5em !important;
            width: 100% !important;
            font-weight: 700 !important;
            font-size: 16px !important;
            box-shadow: 0 4px 12px rgba(54, 117, 136, 0.4) !important;
            text-transform: uppercase !important;
        }

        /* Tabs in alto */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
        }
        .stTabs [data-baseweb="tab"] {
            color: #9CA3AF;
            font-weight: 600;
        }
        .stTabs [aria-selected="true"] {
            color: #367588 !important;
            border-bottom-color: #367588 !important;
        }
        
        /* Correzione per scritte bianche su card bianca (Area Riservata) */
        h3 {
            color: #1F2937 !important;
        }
    </style>
    """, unsafe_allow_html=True)
