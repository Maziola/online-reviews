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
        /* 1. PROTEZIONE IP E RIMOZIONE HEADER */
        header[data-testid="stHeader"], #MainMenu, .stAppDeployButton, footer {
            display: none !important;
            visibility: hidden !important;
        }

        /* 2. SIDEBAR FISSA E RIMOZIONE ICONE */
        [data-testid="stSidebar"] {
            min-width: 350px !important;
            max-width: 350px !important;
            width: 350px !important;
            transform: none !important;
            transition: none !important;
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
            4. AREA SIDEBAR: TESTI BIANCHI
        ========================================================= */
        [data-testid="stSidebarContent"] * {
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
        }

        /* =========================================================
            5. AREA MAIN: TESTI VERDI (Pannello, Etichette, Login)
        ========================================================= */
        .stApp {
            background: linear-gradient(135deg, #cbd5e0 0%, #a0aec0 100%) !important;
        }

        /* Tutte le scritte informative e label diventano VERDI */
        .main [data-testid="stVerticalBlock"] * {
            color: #28a745 !important;
            -webkit-text-fill-color: #28a745 !important;
        }

        /* =========================================================
            6. RIPRISTINO NERO PER IL CONTENUTO DEI WIDGET
        ========================================================= */
        
        /* Testo all'interno di Categoria, Tono della risposta, Nome utente, ecc. */
        /* Questo garantisce che il font interno rimanga NERO su sfondo BIANCO */
        div[data-baseweb="base-input"] input, 
        div[data-baseweb="base-input"] textarea,
        div[data-baseweb="select"] [data-testid="stMarkdownContainer"] p,
        div[data-baseweb="select"] span,
        div[data-baseweb="select"] div,
        .stTextInput input, .stTextArea textarea {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            background-color: #FFFFFF !important;
        }

        /* =========================================================
            7. PULSANTI E CARD
        ========================================================= */
        
        /* Forza il bianco solo per il testo dei pulsanti */
        .main .stButton button *, .main .stFormSubmitButton button * {
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
        }

        div.stButton > button, div.stFormSubmitButton > button {
            background-color: #367588 !important;
            border-radius: 10px !important;
            font-weight: 700 !important;
            border: none !important;
            width: 100%;
        }

        .main-card {
            background-color: #FFFFFF !important;
            border-radius: 20px !important;
            padding: 40px !important;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08) !important;
        }
    </style>
    """, unsafe_allow_html=True)