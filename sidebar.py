import streamlit as st
from translations import t, t_list, LANG_MAP
import auth_handler as auth

def render_sidebar():
    # CSS per bloccare la sidebar e rimuovere i tasti di chiusura (X e Chevron)
    st.markdown("""
        <style>
            /* Rimuove il tasto 'X' all'interno della sidebar */
            [data-testid="sidebar-close-button"] {
                display: none !important;
            }
            /* Rimuove il tasto '>' (chevron) che appare nell'header quando la sidebar è chiusa */
            button[kind="headerNoPadding"] {
                display: none !important;
            }
            /* Forza la sidebar a mantenere la sua larghezza senza transizioni di chiusura */
            [data-testid="stSidebar"] {
                min-width: 350px !important;
                margin-left: 0px !important;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        # 1. SELETTORE LINGUA
        current_code = st.session_state.get("current_lang_code", "it")
        lang_list = list(LANG_MAP.keys())
        try:
            current_index = list(LANG_MAP.values()).index(current_code)
        except ValueError:
            current_index = 0

        selected_lang = st.selectbox(f"🌐 {t('lang_app')}", lang_list, index=current_index)
        
        if LANG_MAP[selected_lang] != st.session_state.current_lang_code:
            st.session_state.current_lang_code = LANG_MAP[selected_lang]
            st.rerun()
        
        st.markdown("---")
        st.markdown(f"### 👤 {st.session_state.username}")
        
        # --- PROFILO BUSINESS ---
        st.markdown(f"##### 🏢 {t('prof_biz')}")
        
        lang = st.session_state.current_lang_code
        
        # Nome Business
        ph_biz = {"it": "Es: Pizzeria da Mario", "en": "Ex: Mario's Pizza", "fr": "Ex: Pizzeria chez Mario", "de": "Z.B. Marios Pizzeria", "es": "Ej: Pizzería de Mario"}
        st.text_input(t("biz_name"), placeholder=ph_biz.get(lang, ""), key="sb_name")

        # Categoria (Si aggiorna con la lingua)
        st.selectbox(
            t("cat_label"), 
            options=t_list("categories"), 
            key="sb_cat"
        )

        # Tono della risposta
        st.selectbox(
            t("tone_label"), 
            options=t_list("tones"), 
            key=f"sb_tone_{lang}"
        )
        
        # --- PUNTI DI FORZA ---
        with st.expander(f"✨ {t('punti_forza')}", expanded=False):
            label_vantaggi = {"it": "Vantaggi competitivi:", "en": "Competitive advantages:", "fr": "Avantages compétitifs :", "de": "Wettbewerbsvorteile:", "es": "Ventajas competitivas:"}
            st.text_area(label_vantaggi.get(lang, "Info:"), key="sb_kf", height=100)
            
        # --- POLICY & FIRMA ---
        with st.expander(f"🛡️ {t('policy_firma')}", expanded=False):
            label_firma = {"it": "Firma finale:", "en": "Final signature:", "fr": "Signature finale :", "de": "Abschlussunterschrift:", "es": "Firma final:"}
            st.text_input(label_firma.get(lang, "Signature:"), placeholder="Il Team di...", key="sb_sig")

        st.markdown("---")
        
        # --- STORICO ---
        st.markdown(f"##### 📜 {t('last_analyses')}")
        history_data = auth.get_history(st.session_state.username)
        
        if history_data:
            for i, item in enumerate(history_data):
                col_btn, col_edit, col_del = st.columns([3, 1, 1])
                if col_btn.button(f"🕒 {item[3]}", key=f"hi_{i}", use_container_width=True):
                    st.session_state.history_item = item
                    st.rerun()
                
                with col_edit:
                    with st.popover("✏️"):
                        st.text_input("Rename:", value=item[3], key=f"edit_val_{i}")
                        if st.button("OK", key=f"save_edit_{i}"):
                            auth.rename_history_item(st.session_state.username, item[3], st.session_state[f"edit_val_{i}"])
                            st.rerun()
                
                with col_del:
                    with st.popover("🗑️"):
                        label_del = t("confirm_del")
                        if st.button(label_del, key=f"del_{i}", type="primary"):
                            auth.delete_history_item(st.session_state.username, item[3])
                            st.rerun()
        else:
            st.caption(t("no_analyses"))

        st.markdown("---")
        # Logout tradotto
        btn_logout = {"it": "🚪 Esci", "en": "🚪 Log out", "fr": "🚪 Déconnexion", "de": "🚪 Abmelden", "es": "🚪 Cerrar sesión"}
        if st.button(btn_logout.get(lang, "Exit"), use_container_width=True):
            st.session_state.auth = False
            st.session_state.username = ""
            st.rerun()