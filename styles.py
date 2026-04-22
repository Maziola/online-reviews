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
        # MODIFICA: Eliminato margin-bottom negativo per evitare sovrapposizioni
        return f'''
            <div style="display: flex; justify-content: center; align-items: center; padding-bottom: 10px; margin-bottom: 10px;">
                <img src="data:image/png;base64,{data}" style="width: {size*5}px; height: auto; object-fit: contain;">
            </div>
        '''
    return "<div style='height:0px;'></div>"

def apply_custom_styles():
    # CSS Ultra-aggressivo per nascondere header, menu, pulsanti deploy e GitHub
    st.markdown("""
    <style>
        /* =========================================================
            PROTEZIONE IP: RIMOZIONE TOTALE HEADER E MENU
        ========================================================= */
        header[data-testid="stHeader"] {
            display: none !important;
            visibility: hidden !important;
            height: 0px !important;
        }
        
        #MainMenu {
            display: none !important;
            visibility: hidden !important;
        }
        
        .stAppDeployButton {
            display: none !important;
            visibility: hidden !important;
        }
        
        footer {
            display: none !important;
            visibility: hidden !important;
        }

        /* =========================================================
            FIX EMERGENZA: RIPRISTINO PULSANTE APERTURA SIDEBAR
        ========================================================= */
        /* Questo blocca la scomparsa del tasto per riaprire la sidebar quando è chiusa */
        section[data-testid="stSidebar"] + div > button, 
        button[kind="headerNoPadding"] {
            display: flex !important;
            visibility: visible !important;
            opacity: 1 !important;
            background-color: #367588 !important; /* Verde petrolio per vederlo bene */
            color: white !important;
            z-index: 999999 !important;
            left: 10px !important;
            top: 10px !important;
        }

        /* =========================================================
            PATCH: FIX SPAZIATURA E SOVRAPPOSIZIONI
        ========================================================= */
        /* MODIFICA: padding-top a 2rem per distanziare il logo dal bordo superiore */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 0rem !important;
        }
        
        /* MODIFICA: gap impostato a 1rem per evitare che le scritte si attacchino agli input */
        [data-testid="stVerticalBlock"] > div:has(div[class*="stMarkdown"]) {
            gap: 1rem !important;
        }

        /* =========================================================
            PATCH: ELIMINAZIONE SCRITTE SOVRAPPOSTE (SOLUZIONE RADICALE)
        ========================================================= */
        /* 1. Rimozione standard */
        div[data-baseweb="select"] ~ span > div:last-child,
        div[data-baseweb="select"] + div svg,
        div[data-testid="stSelectbox"] div[role="button"] > div:last-child,
        div[data-testid="stExpander"] svg {
            display: none !important;
            visibility: hidden !important;
        }

        /* 2. Forzatura invisibilità (Trasparenza e dimensione zero) per scritte residue */
        /* Invece di display:none, usiamo font-size:0 così il tasto rimane cliccabile ma il testo sparisce */
        div[data-testid="stExpander"] p:empty,
        div[aria-expanded="true"] > div > svg + div,
        div[aria-expanded="false"] > div > svg + div,
        *:contains("arrow_right"), 
        *:contains("keyboard_double") {
            color: transparent !important;
            font-size: 0px !important;
            line-height: 0 !important;
            visibility: hidden !important;
            opacity: 0 !important;
            user-select: none !important;
            pointer-events: none !important;
            text-indent: -9999px !important;
        }

        /* =========================================================
            1. SFONDO GENERALE APP
        ========================================================= */
        .stApp {
            background: linear-gradient(135deg, #cbd5e0 0%, #a0aec0 100%) !important;
        }

        /* =========================================================
            2. SIDEBAR (SINISTRA) - FORZA TESTO BIANCO
        ========================================================= */
        [data-testid="stSidebar"], [data-testid="stSidebarContent"] {
            background-color: #4a5568 !important;
            background-image: none !important;
        }

        [data-testid="stSidebar"] div[data-testid="stWidgetLabel"] p,
        [data-testid="stSidebar"] label p,
        [data-testid="stSidebar"] label {
            color: #FFFFFF !important;
            font-weight: 700 !important;
            opacity: 1 !important;
        }

        [data-testid="stSidebar"] .stMarkdown p, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] .stCaption,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] h4, 
        [data-testid="stSidebar"] h5 {
            color: #FFFFFF !important;
            font-weight: 600 !important;
        }

        /* =========================================================
            3. AREA DESTRA E LOGIN - TUTTO VERDE PETROLIO
        ========================================================= */
        h1, h2, h3, h4, h5,
        label p,
        button[data-baseweb="tab"] p,
        .stApp .stMarkdown p,
        .stApp span {
            color: #367588 !important;
            font-weight: bold !important;
        }

        [data-testid="stSidebar"] label p,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] .stMarkdown p {
            color: #FFFFFF !important;
        }

        /* =========================================================
            4. INPUT, TEXTAREA E SELECTBOX - SFONDO BIANCO E TESTO NERO
        ========================================================= */
        div[data-baseweb="base-input"] input, 
        div[data-baseweb="base-input"] textarea,
        div[data-baseweb="select"] > div, 
        .stTextInput input,
        .stTextArea textarea {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            caret-color: #000000 !important;
            border-radius: 12px !important;
            border: 1px solid #CBD5E1 !important;
        }

        div[data-testid="stSelectbox"] p, div[data-testid="stSelectbox"] div {
            color: #000000 !important;
        }

        /* =========================================================
            5. CARD BIANCA (Dashboard)
        ========================================================= */
        .main-card {
            background-color: #FFFFFF !important;
            border-radius: 20px !important;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08) !important;
            padding: 40px !important;
        }
        
        .main-card .stMarkdown p {
            color: #000000 !important;
        }

        /* =========================================================
            6. PULSANTI
        ========================================================= */
        div.stButton > button, 
        div.stFormSubmitButton > button {
            background-color: #367588 !important;
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
            border-radius: 10px !important;
            font-weight: 700 !important;
            border: none !important;
        }

        div.stButton > button:hover {
            background-color: #2a5d6d !important;
        }

        /* =========================================================
            7. FIX NOTIFICHE (GIALLO CHIARO) E VARIANTI
        ========================================================= */
        [data-testid="stNotification"] {
            background-color: #fff9c4 !important;
            color: #5d4037 !important;
            border: 1px solid #fff176 !important;
            border-radius: 10px !important;
        }
        
        [data-testid="stNotification"] p {
            color: #5d4037 !important;
            font-weight: 600 !important;
        }

        .variant-card p {
            color: #367588 !important;
        }
    </style>
    """, unsafe_allow_html=True)