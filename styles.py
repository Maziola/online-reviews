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
        # MODIFICA: margin-bottom riportato a 10px per evitare sovrapposizioni con login/tab
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
            PATCH SPAZIATURA: EVITA SOVRAPPOSIZIONI
        ========================================================= */
        /* MODIFICA: padding-top aumentato a 2.5rem per dare respiro al logo */
        .block-container {
            padding-top: 2.5rem !important;
            padding-bottom: 1rem !important;
        }
        
        /* MODIFICA: gap riportato a 1rem per separare titoli e campi input */
        [data-testid="stVerticalBlock"] > div:has(div[class*="stMarkdown"]) {
            gap: 1rem !important;
        }

        /* =========================================================
            PATCH: ELIMINAZIONE SCRITTE SOVRAPPOSTE
        ========================================================= */
        div[data-baseweb="select"] ~ span > div:last-child,
        div[data-baseweb="select"] + div svg,
        div[data-testid="stSelectbox"] div[role="button"] > div:last-child,
        div[data-testid="stExpander"] svg {
            display: none !important;
            visibility: hidden !important;
        }

        /* =========================================================
            1. SFONDO GENERALE APP
        ========================================================= */
        .stApp {
            background: linear-gradient(135deg, #cbd5e0 0%, #a0aec0 100%) !important;
        }

        /* =========================================================
            2. SIDEBAR (SINISTRA)
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
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h3 {
            color: #FFFFFF !important;
        }

        /* =========================================================
            3. AREA DESTRA E LOGIN - VERDE PETROLIO
        ========================================================= */
        h1, h2, h3, h4, h5,
        label p,
        button[data-baseweb="tab"] p,
        .stApp .stMarkdown p,
        .stApp span {
            color: #367588 !important;
            font-weight: bold !important;
        }

        /* =========================================================
            4. INPUT, TEXTAREA E SELECTBOX
        ========================================================= */
        div[data-baseweb="base-input"] input, 
        div[data-baseweb="base-input"] textarea,
        div[data-baseweb="select"] > div, 
        .stTextInput input,
        .stTextArea textarea {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            border-radius: 12px !important;
            border: 1px solid #CBD5E1 !important;
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
            border-radius: 10px !important;
            font-weight: 700 !important;
            border: none !important;
        }

        div.stButton > button:hover {
            background-color: #2a5d6d !important;
        }

        /* =========================================================
            7. NOTIFICHE
        ========================================================= */
        [data-testid="stNotification"] {
            background-color: #fff9c4 !important;
            color: #5d4037 !important;
            border-radius: 10px !important;
        }
    </style>
    """, unsafe_allow_html=True)