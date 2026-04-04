import streamlit as st
import base64

def apply_custom_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
        .variant-card { background: white; padding: 20px; border-radius: 12px; border: 1px solid #E2E8F0; margin-bottom: 10px; color: #1E293B; }
        .stButton>button { border-radius: 8px; font-weight: 600; }
        .login-box { text-align: center; padding: 20px; border: 1px solid #E2E8F0; border-radius: 15px; background: #F8FAFC; }
        </style>
    """, unsafe_allow_html=True)

def get_logo_html(size=100):
    # Logo Opzione 1 (Bussola/Check)
    logo_svg = f"""
    <svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="45" fill="#1E3A8A"/>
        <path d="M30 50 L45 65 L70 35" stroke="#FBBF24" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    """
    b64 = base64.b64encode(logo_svg.encode()).decode()
    return f'<div style="text-align:center;"><img src="data:image/svg+xml;base64,{b64}" width="{size}"></div>'