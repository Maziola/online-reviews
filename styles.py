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
        /* 1. PROTEZIONE IP: RIMOZIONE TOTALE HEADER E MENU */
        header[data-testid="stHeader"], #MainMenu, .stAppDeployButton, footer {
            display: none !important;
            visibility: hidden !important;
        }

        /* 2. SIDEBAR FISSA (FIX TAGLIO LATERALE) */
        [data-testid="stSidebar"] {
            display: flex !important;
            visibility: visible !important;
            min-width: 350px !important;
            max-width: 350px !important;
            z-index: 999999 !important;
        }

        /* Rimuove i pulsanti di chiusura/apertura */
        [data-testid="sidebar-close-button"], button[kind="headerNoPadding"] {
            display: none !important;
        }

        /* 3. RIMOZIONE TESTI SOVRAPPOSTI (FIX ICONE BLUASTRE) */
        [data-testid="stExpander"] svg + div,
        [data-testid="stSelectbox"] svg + div,
        div:contains("keyboard_double"),
        div:contains("arrow_right"),
        span:contains("keyboard_double"),
        span:contains("arrow_right") {
            display: none !important;
            font-size: 0px !important;
            color: transparent !important;
        }

        /* 4. DESIGN SIDEBAR (TESTO BIANCO) */
        [data-testid="stSidebar"], [data-testid="stSidebarContent"] {
            background-color: #4a5568 !important;
            background-image: none !important;
        }

        [data-testid="stSidebar"] label p, [data-testid="stSidebar"] .stMarkdown p, 
        [data-testid="stSidebar"] h3, [data-testid="stSidebar"] span {
            color: #FFFFFF !important;
            font-weight: 600 !important;
        }

        /* 5. DESIGN AREA PRINCIPALE E SFONDO */
        .stApp {
            background: linear-gradient(135deg, #cbd5e0 0%, #a0aec0 100%) !important;
        }

        h1, h2, h3, h4, h5, label p, .stApp .stMarkdown p, .stApp span {
            color: #367588 !important;
            font-weight: bold !important;
        }

        /* 6. INPUT E SELECTBOX (SFONDO BIANCO / TESTO NERO) */
        div[data-baseweb="base-input"] input, div[data-baseweb="base-input"] textarea,
        div[data-baseweb="select"] > div, .stTextInput input, .stTextArea textarea {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            border-radius: 12px !important;
            border: 1px solid #CBD5E1 !important;
        }

        div[data-testid="stSelectbox"] p, div[data-testid="stSelectbox"] div {
            color: #000000 !important;
        }

        /* 7. PULSANTI (RIPRISTINO TESTO BIANCO FORZATO) */
        div.stButton > button, div.stFormSubmitButton > button {
            background-color: #367588 !important;
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important; /* Forza il bianco su Chrome/Safari */
            border-radius: 10px !important;
            font-weight: 700 !important;
            border: none !important;
        }

        div.stButton > button:hover {
            background-color: #2a5d6d !important;
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
        }

        /* 8. CARD E NOTIFICHE */
        .main-card {
            background-color: #FFFFFF !important;
            border-radius: 20px !important;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08) !important;
            padding: 40px !important;
        }

        [data-testid="stNotification"] {
            background-color: #fff9c4 !important;
            color: #5d4037 !important;
            border: 1px solid #fff176 !important;
            border-radius: 10px !important;
        }
        
        [data-testid="stNotification"] p {
            color: #5d4037 !important;
        }
    </style>
    """, unsafe_allow_html=True)