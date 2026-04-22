import streamlit as st
import base64
import os

def apply_custom_font(font_name="Ubuntu"):
    font_url = font_name.replace(" ", "+")
    st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family={font_url}:wght@300;400;700;800&display=swap');
            
            /* Font globale */
            html, body, [class*="css"], .stMarkdown, p, div, span, h1, h2, h3, h4, h5 {{
                font-family: '{font_name}', sans-serif !important;
            }}
        </style>
    """, unsafe_allow_html=True)

def get_logo_html(size=100):
    logo_filename = "logo_pro.png" 
    logo_path = os.path.join(os.path.dirname(__file__), logo_filename)
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        return f'''
            <div style="display: flex; justify-content: center; align-items: center; padding-bottom: 10px; margin-bottom: 10px;">
                <img src="data:image/png;base64,{data}" style="width: {size*5}px; height: auto; object-fit: contain;">
            </div>
        '''
    return "<div style='height:0px;'></div>"

def apply_custom_styles():
    st.markdown("""
    <style>
        /* =========================================================
            1. PROTEZIONE IP: RIMOZIONE TOTALE HEADER E MENU
        ========================================================= */
        header[data-testid="stHeader"] {
            display: none !important;
            visibility: hidden !important;
        }
        
        #MainMenu { display: none !important; }
        .stAppDeployButton { display: none !important; }
        footer { display: none !important; }

        /* =========================================================
            2. SIDEBAR FISSA E RIMOZIONE CURSORE SPOSTAMENTO
        ========================================================= */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            width: 350px !important;
            transform: none !important;
            transition: none !important;
        }
        
        /* RIMOZIONE DEFINITIVA DELLE FRECCE DI RIDIMENSIONAMENTO/SPOSTAMENTO */
        /* Nasconde l'elemento di drag e disabilita il cursore orizzontale */
        [data-testid="stSidebarResizer"] {
            display: none !important;
            visibility: hidden !important;
        }
        
        [data-testid="stSidebar"] svg, 
        [data-testid="sidebar-close-button"], 
        button[kind="headerNoPadding"] {
            display: none !important;
        }

        /* =========================================================
            3. SIDEBAR: COLORE SCRITTE BIANCO (RICHIESTA SPECIFICA)
        ========================================================= */
        [data-testid="stSidebar"], [data-testid="stSidebarContent"] {
            background-color: #4a5568 !important;
        }

        /* Forza bianco per titoli, paragrafi, caption e label widget */
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, [data-testid="stSidebar"] h4, 
        [data-testid="stSidebar"] h5, [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label, [data-testid="stSidebar"] .stCaption,
        [data-testid="stSidebar"] span, [data-testid="stSidebar"] .stMarkdown p {
            color: #FFFFFF !important;
            opacity: 1 !important;
            font-weight: 600 !important;
        }

        /* =========================================================
            4. AREA PRINCIPALE E SFONDO GRADIENTE
        ========================================================= */
        .stApp {
            background: linear-gradient(135deg, #cbd5e0 0%, #a0aec0 100%) !important;
        }

        /* Titoli area destra e login in verde petrolio */
        .main h1, .main h2, .main h3, .main h4, .main h5, 
        .main label p, .stApp .main .stMarkdown p, .stApp .main span {
            color: #367588 !important;
            font-weight: bold !important;
        }

        /* =========================================================
            5. WIDGET (INPUT BIANCHI / TESTO NERO)
        ========================================================= */
        div[data-baseweb="base-input"] input, 
        div[data-baseweb="base-input"] textarea,
        div[data-baseweb="select"] > div,
        .stTextInput input, .stTextArea textarea {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            border-radius: 12px !important;
        }

        /* =========================================================
            6. PULSANTI (ACCESSO E REGISTRAZIONE - VERDE PETROLIO)
        ========================================================= */
        div.stButton > button, div.stFormSubmitButton > button {
            background-color: #367588 !important;
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
            border-radius: 10px !important;
            font-weight: 700 !important;
            border: none !important;
            width: 100%;
        }

        div.stButton > button:hover {
            background-color: #2a5d6d !important;
        }

        /* =========================================================
            7. CARD E NOTIFICHE
        ========================================================= */
        .main-card {
            background-color: #FFFFFF !important;
            border-radius: 20px !important;
            padding: 40px !important;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08) !important;
        }

        [data-testid="stNotification"] {
            background-color: #fff9c4 !important;
            color: #5d4037 !important;
            border-radius: 10px !important;
        }
    </style>
    """, unsafe_allow_html=True)