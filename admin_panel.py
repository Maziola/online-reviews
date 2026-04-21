import streamlit as st
from translations import t
import auth_handler as auth

def render_admin_zone():
    st.markdown(f"### {t('admin_panel')}")
    
    # Inizio del contenitore per lo stile grafico
    with st.container():
        st.markdown(f'<div class="admin-box">', unsafe_allow_html=True)
        st.write(f"**{t('admin_desc')}**")
        st.divider() 

        try:
            # 1. Recupero la lista utenti
            users = auth.get_all_users()
            
            # Filtro per escludere l'admin dalla lista (opzionale, ma pulisce la vista)
            users_list = [u for u in users if u['username'].lower() != "admin"]
            
            if not users_list:
                st.info(t("no_users"))
            else:
                # 2. Intestazione tabella tradotta
                h1, h2, h3 = st.columns([2, 2, 1])
                
                # Traduzioni al volo per le intestazioni colonna
                col_utente = {"it": "UTENTE", "en": "USER", "fr": "UTILISATEUR", "de": "BENUTZER", "es": "USUARIO"}
                col_stato = {"it": "STATO", "en": "STATUS", "fr": "ÉTAT", "de": "STATUS", "es": "ESTADO"}
                col_azione = {"it": "AZIONE", "en": "ACTION", "fr": "ACTION", "de": "AKTION", "es": "ACCIÓN"}
                
                lang = st.session_state.get("current_lang_code", "it")
                
                h1.caption(col_utente.get(lang, "USER"))
                h2.caption(col_stato.get(lang, "STATUS"))
                h3.caption(col_azione.get(lang, "ACTION"))

                # 3. Ciclo su ogni utente
                for user in users_list:
                    with st.container():
                        c1, c2, c3 = st.columns([2, 2, 1])
                        
                        # Nome utente
                        c1.markdown(f"👤 **{user['username']}**")
                        
                        # Data iscrizione tradotta
                        label_iscritto = {"it": "Iscritto il", "en": "Joined on", "fr": "Inscrit le", "de": "Beigetreten am", "es": "Registrado el"}
                        c1.caption(f"{label_iscritto.get(lang, 'Joined')}: {user['signup_date']}")
                        
                        # Stato attuale tradotto
                        if user['active']:
                            status_txt = {"it": "✅ Attivo", "en": "✅ Active", "fr": "✅ Actif", "de": "✅ Aktiv", "es": "✅ Activo"}
                        else:
                            status_txt = {"it": "⏳ In Prova", "en": "⏳ Trial Mode", "fr": "⏳ En Essai", "de": "⏳ Testversion", "es": "⏳ En Prueba"}
                        
                        c2.write(status_txt.get(lang, "Status"))
                        
                        # Pulsante per cambiare stato (Tradotto)
                        if user['active']:
                            btn_label = {"it": "Disattiva", "en": "Deactivate", "fr": "Désactiver", "de": "Deaktivieren", "es": "Desactivar"}
                        else:
                            btn_label = {"it": "Attiva", "en": "Activate", "fr": "Activer", "de": "Aktivieren", "es": "Activar"}
                            
                        if c3.button(btn_label.get(lang, "Toggle"), key=f"toggle_{user['username']}", use_container_width=True):
                            auth.toggle_user_status(user['username'])
                            st.rerun() 
                        
                        st.markdown("---") 
        
        except Exception as e:
            st.error(f"Error: {e}")
            
        st.markdown('</div>', unsafe_allow_html=True)