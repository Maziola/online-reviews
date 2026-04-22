import streamlit as st
import base64
import os

def apply_custom_font(font_name="Ubuntu"):
    font_url = font_name.replace(" ", "+")
    st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family={font_url}:wght@300;400;700;800&display=swap');
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
        /* 1. PROTEZIONE IP E RIMOZIONE HEADER */
        header[data-testid="stHeader"], #MainMenu, .stAppDeployButton, footer {
            display: none !important;
        }

        /* 2. SIDEBAR FISSA E LARGHEZZA */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            width: 350px !important;
            background-color: #4a5568 !important;
        }
        
        [data-testid="stSidebarResizer"], [data-testid="sidebar-close-button"], 
        button[kind="headerNoPadding"], [data-testid="stSidebar"] svg {
            display: none !important;
        }

        /* 3. RIMOZIONE BUG ICONE BLUASTRE */
        div[data-testid="stExpander"] svg + div, div[data-testid="stSelectbox"] svg + div,
        *:contains("keyboard_double"), *:contains("arrow_right") {
            display: none !important;
            font-size: 0px !important;
            color: transparent !important;
        }

        /* =========================================================
            4. COLORI SIDEBAR (FORZATURA BIANCO)
        ========================================================= */
        /* Colpisce tutto ciò che è dentro la Sidebar */
        [data-testid="stSidebar"] * {
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
        }

        /* =========================================================
            5. COLORI BLOCCO MAIN (FORZATURA VERDE)
        ========================================================= */
        .stApp {
            background: linear-gradient(135deg, #cbd5e0 0%, #a0aec0 100%) !important;
        }

        /* Questa regola sovrascrive le variabili interne di Streamlit solo nel Main */
        .main {
            --text-color: #28a745 !important;
            --header-color: #28a745 !important;
        }

        /* Colpiamo ogni tag testuale dentro l'area main */
        .main p, .main span, .main label, .main h1, .main h2, .main h3, .main div {
            color: #28a745 !important;
            -webkit-text-fill-color: #28a745 !important;
        }

        /* =========================================================
            6. RIPRISTINO COLORI INPUT E BOTTONI (DA NON RENDERE VERDI)
        ========================================================= */
        /* Testo dentro i campi di input (deve restare Nero) */
        .main input, .main textarea, .main [data-baseweb="select"] div {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
        }

        /* Testo dentro i pulsanti (deve restare Bianco) */
        .main button p, .main button span, .main button div {
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
        }

        div.stButton > button, div.stFormSubmitButton > button {
            background-color: #367588 !important;
            border-radius: 10px !important;
            border: none !important;
        }

        .main-card {
            background-color: #FFFFFF !important;
            border-radius: 20px !important;
            padding: 40px !important;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08) !important;
        }
    </style>
    """, unsafe_allow_html=True)