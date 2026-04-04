import streamlit as st

def get_logo_html(size=120):
    """
    Riproduce il logo scelto (Omino e Stelle) direttamente in SVG.
    Vantaggio: Caricamento istantaneo, nessun link rotto, alta definizione.
    """
    return f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="width: {size}px; height: {size}px;">
            <path d="M12 2l1.5 4.5h4.5l-3.5 3 1.5 5-4-3-4 3 1.5-5-3.5-3h4.5z" fill="#D4AF37" stroke="none"/>
            <path d="M5 6l1 2.5h2.5l-2 1.5.5 2.5-2-1.5-2 1.5.5-2.5-2-1.5h2.5z" fill="#D4AF37" stroke="none" opacity="0.7"/>
            <path d="M19 6l1 2.5h2.5l-2 1.5.5 2.5-2-1.5-2 1.5.5-2.5-2-1.5h2.5z" fill="#D4AF37" stroke="none" opacity="0.7"/>
            <circle cx="12" cy="11" r="2" fill="#1F4788" stroke="none"/>
            <path d="M12 14c-4 0-5 2-5 4v1h10v-1c0-2-1-4-5-4z" fill="#1F4788" stroke="none"/>
            <path d="M7 15l-2-2M17 15l2-2" stroke="#1F4788" stroke-width="2"/>
        </svg>
        <div style="font-family: 'Open Sans', sans-serif; font-size: {size/3.5}px; font-weight: bold; margin-top: 10px;">
            <span style="color: #1F4788;">REVIEWS MASTER</span> <span style="color: #367588;">PRO</span>
        </div>
    </div>
    """

def apply_custom_styles():
    """
    Ripristina il look originale wide e pulito.
    """
    st.markdown("""
    <style>
        .main .block-container {
            max-width: 1000px;
            padding-top: 2rem;
        }
        .stForm {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        div.stButton > button {
            background-color: #1F4788;
            color: white;
            border-radius: 8px;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)
