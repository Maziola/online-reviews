import streamlit as st

def get_logo_html(size=100):
    """
    Logo con omino e stelle, centrato e distanziato.
    """
    return f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 30px;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="width: {size}px; height: {size}px;">
            <path d="M12 1L13.5 5.5H18L14.5 8L16 12.5L12 10L8 12.5L9.5 8L6 5.5H10.5L12 1z" fill="#D4AF37"/>
            <path d="M5 4L5.8 6H8L6.2 7.2L7 9L5 7.8L3 9L3.8 7.2L2 6H4.2L5 4z" fill="#D4AF37" opacity="0.6"/>
            <path d="M19 4L19.8 6H22L20.2 7.2L21 9L19 7.8L17 9L17.8 7.2L16 6H18.2L19 4z" fill="#D4AF37" opacity="0.6"/>
            <circle cx="12" cy="14" r="3" fill="#367588"/>
            <path d="M12 18c-4 0-6 2-6 4v1h12v-1c0-2-2-4-6-4z" fill="#367588"/>
        </svg>
        <div style="margin-top: 15px; text-align: center;">
            <span style="font-family: 'Inter', sans-serif; font-size: 26px; font-weight: 800; color: #E0E0E0; letter-spacing: 2px; text-transform: uppercase;">REVIEWS MASTER</span>
            <span style="font-family: 'Inter', sans-serif; font-size: 26px; font-weight: 300; color: #367588; margin-left: 8px;">PRO</span>
        </div>
    </div>
    """

def apply_custom_styles():
    """
    CSS per il design avanzato: Card Bianca, Sfondo Blu Notte, Pulsante Teal.
    """
    st.markdown("""
    <style>
        /* Sfondo della pagina con sfumatura radiale profonda */
        .stApp {
            background: radial-gradient(circle at center, #1b2735 0%, #090a0f 100%);
        }

        /* La Card: Bianca e arrotondata */
        [data-testid="stForm"] {
            background-color: #ffffff !important;
            border-radius: 24px !important;
            padding: 40px !important;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4) !important;
            border: none !important;
            color: #333333 !important;
        }

        /* Testo delle Label (Username/Password) */
        [data-testid="stForm"] label p {
            color: #444444 !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            margin-bottom: 8px !important;
        }

        /* Campi di Input: Grigio chiaro come nel design */
        input {
            background-color: #f1f3f6 !important;
            color: #1b2735 !important;
            border: 1px solid #e1e4e8 !important;
            border-radius: 12px !important;
            padding: 12px !important;
        }

        /* Pulsante ACCEDI: Grande, Teal e stondato */
        div.stButton > button {
            background-color: #367588 !important;
            color: white !important;
            border: none !important;
            border-radius: 50px !important;
            height: 3.8em !important;
            width: 100% !important;
            font-weight: 800 !important;
            font-size: 18px !important;
            margin-top: 20px !important;
            box-shadow: 0 4px 15px rgba(54, 117, 136, 0.3) !important;
            transition: all 0.3s ease !important;
        }

        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(54, 117, 136, 0.5) !important;
        }

        /* Tabs: Semplici e moderne */
        .stTabs [data-baseweb="tab-list"] {
            gap: 20px;
            margin-bottom: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            color: #8B949E;
            font-weight: 700;
        }
        .stTabs [aria-selected="true"] {
            color: white !important;
            border-bottom-color: #367588 !important;
        }
    </style>
    """, unsafe_allow_html=True)
