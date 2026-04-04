import streamlit as st

def get_logo_html(size=250):
    """
    Inserisce il logo ufficiale ad alta definizione.
    Il link punta alla versione 'raw' su GitHub per caricarla correttamente nell'app.
    """
    # NOTA: Assicurati che l'indirizzo qui sotto corrisponda al tuo username e repo su GitHub
    logo_url = "https://raw.githubusercontent.com/Maziola/online-reviews/main/logo_pro.png"
    
    return f'''
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 30px;">
        <img src="{logo_url}" width="{size}px" style="filter: drop-shadow(0px 4px 8px rgba(0,0,0,0.1));">
    </div>
    '''

def apply_custom_styles():
    """
    Applica il tema grafico avanzato per Reviews Master Pro.
    Include ottimizzazione per schermi larghi, box di login eleganti e bottoni moderni.
    """
    st.markdown("""
    <style>
        /* 1. Layout Wide - Sfrutta tutto lo spazio dello schermo */
        .main .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        /* 2. Box di Login - Stile moderno e pulito */
        .stForm {
            border: 1px solid #e6e9ef !important;
            border-radius: 15px !important;
            padding: 30px !important;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05) !important;
            background-color: #ffffff;
        }

        /* 3. Bottoni - Colore Corporate Blu e angoli smussati */
        div.stButton > button:first-child {
            background-color: #1F4788;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 0.6rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        div.stButton > button:first-child:hover {
            background-color: #367588;
            border: none;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }

        /* 4. Titoli e Font */
        h1, h2, h3 {
            font-family: 'Inter', sans-serif;
            color: #1F4788;
        }

        /* 5. Card Risultati (Dashboard) */
        .result-card {
            background-color: #f8f9fa;
            border-radius: 12px;
            padding: 20px;
            border-left: 6px solid #367588;
            margin-bottom: 15px;
        }

        /* Nascondi il menu di Streamlit per un look più 'App' */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
