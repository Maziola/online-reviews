import streamlit as st

def get_logo_html(size=100):
    """
    Logo Premium: Omino Blu e Stelle Oro.
    Testo separato e ben spaziato.
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
        <div style="margin-top: 15px;">
            <span style="font-family: 'Helvetica', sans-serif; font-size: 22px; font-weight: 800; color: #FFFFFF; letter-spacing: 1.5px;">REVIEWS MASTER</span>
            <span style="font-family: 'Helvetica', sans-serif; font-size: 22px; font-weight: 300; color: #367588; margin-left: 5px;">PRO</span>
        </div>
    </div>
    """

def apply_custom_styles():
    """
    Stile Dark Professionale con contrasti elevati.
    """
    st.markdown("""
    <style>
        .stApp {
            background-color: #0B0E14;
        }
        
        /* Card di sfondo per i form */
        [data-testid="stForm"] {
            background-color: #161B22 !important;
            border: 1px solid #30363D !important;
            border-radius: 15px !important;
            padding: 30px !important;
        }

        /* Label e Testi */
        .stMarkdown p, label {
            color: #C9D1D9 !important;
            font-weight: 500 !important;
        }

        /* Input Fields */
        input {
            background-color: #0D1117 !important;
            color: white !important;
            border-radius: 8px !important;
        }

        /* Pulsanti Semplificati */
        div.stButton > button {
            background-color: #367588 !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            width: 100% !important;
            height: 3em !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            color: #8B949E;
        }
        .stTabs [aria-selected="true"] {
            color: white !important;
            border-bottom-color: #367588 !important;
        }
    </style>
    """, unsafe_allow_html=True)
