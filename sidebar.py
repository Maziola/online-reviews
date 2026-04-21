import streamlit as st
from translations import t, t_list, LANG_MAP
import auth_handler as auth

def render_sidebar():
    with st.sidebar:
        # 1. SELETTORE LINGUA (Con aggiornamento immediato della sessione)
        # Cerchiamo la chiave corrispondente al codice attuale per impostare l'indice corretto
        current_code = st.session_state.get("current_lang_code", "it")
        lang_list = list(LANG_MAP.keys())
        try:
            current_index = list(LANG_MAP.values()).index(current_code)
        except ValueError:
            current_index = 0

        selected_lang = st.selectbox("🌐 Lingua App", lang_list, index=current_index)
        
        # Se la lingua selezionata è diversa da quella in sessione, aggiorniamo e ricarichiamo
        if LANG_MAP[selected_lang] != st.session_state.current_lang_code:
            st.session_state.current_lang_code = LANG_MAP[selected_lang]
            st.rerun()
        
        st.markdown("---")
        st.markdown(f"### 👤 {st.session_state.username}")
        
        # --- PROFILO BUSINESS ---
        st.markdown(f"##### 🏢 {t('prof_biz')}")
        
        st.text_input(t("biz_name"), placeholder="Es: Pizzeria da Mario", key="sb_name")
        st.selectbox(t("cat_merc"), t_list("categories"), key="sb_cat")
        st.selectbox("🎭 Tono della risposta", t_list("tones"), key="sb_tone")
        
        # Utilizziamo label esplicite per evitare che il CSS anti-sovrapposizione nasconda troppo
        with st.expander("✨ Punti di Forza", expanded=False):
            st.text_area("Vantaggi competitivi:", key="sb_kf", label_visibility="visible", height=100)
            
        with st.expander("🛡️ Policy & Firma", expanded=False):
            st.text_input("Firma finale:", placeholder="Il Team di...", key="sb_sig")

        st.markdown("---")
        
        # --- STORICO CON RINOMINA ED ELIMINA ---
        st.markdown("##### 📜 Ultime Analisi")
        history_data = auth.get_history(st.session_state.username)
        
        if history_data:
            for i, item in enumerate(history_data):
                # item[3] è il nome/data dell'analisi salvata
                col_btn, col_edit, col_del = st.columns([3, 1, 1])
                
                # 1. Tasto per visualizzare l'analisi nel main
                if col_btn.button(f"🕒 {item[3]}", key=f"hi_{i}", use_container_width=True):
                    st.session_state.history_item = item
                    st.rerun()
                
                # 2. Popover per rinominare (✏️)
                with col_edit:
                    with st.popover("✏️"):
                        new_name = st.text_input("Rinomina analisi:", value=item[3], key=f"edit_val_{i}")
                        if st.button("Conferma", key=f"save_edit_{i}", use_container_width=True):
                            if new_name:
                                auth.rename_history_item(st.session_state.username, item[3], new_name)
                                st.rerun()
                
                # 3. Popover per eliminare (🗑️)
                with col_del:
                    with st.popover("🗑️"):
                        st.error("Eliminare?")
                        if st.button("Sì, elimina", key=f"del_{i}", type="primary", use_container_width=True):
                            auth.delete_history_item(st.session_state.username, item[3])
                            # Pulizia se l'analisi eliminata è quella aperta
                            if st.session_state.get("history_item") and st.session_state.history_item[3] == item[3]:
                                st.session_state.history_item = None
                            st.rerun()
        else:
            st.caption("Nessuna analisi salvata.")

        st.markdown("---")
        if st.button("🚪 Log out", use_container_width=True):
            st.session_state.auth = False
            st.session_state.username = ""
            st.session_state.history_item = None
            st.rerun()