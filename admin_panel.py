import streamlit as st
from translations import t
import auth_handler as auth

def render_admin_zone():
    st.markdown(f"### {t('admin_panel')}")
    
    # Inizio del contenitore bianco che vedi nell'immagine
    with st.container():
        st.markdown(f'<div class="admin-box">', unsafe_allow_html=True)
        st.write(f"**{t('admin_desc')}**")
        st.divider() # Linea di separazione estetica

        # 1. Recupero la lista aggiornata degli utenti dal database
        try:
            users = auth.get_all_users()
            
            if not users:
                st.info("Non ci sono ancora utenti registrati oltre all'admin.")
            else:
                # 2. Creo l'intestazione della tabella
                h1, h2, h3 = st.columns([2, 2, 1])
                h1.caption("UTENTE")
                h2.caption("STATO")
                h3.caption("AZIONE")

                # 3. Ciclo su ogni utente per creare una riga
                for user in users:
                    with st.container():
                        c1, c2, c3 = st.columns([2, 2, 1])
                        
                        # Nome utente e data iscrizione
                        c1.markdown(f"👤 **{user['username']}**")
                        c1.caption(f"Iscritto il: {user['signup_date']}")
                        
                        # Stato attuale
                        status_label = "✅ Attivo" if user['active'] else "⏳ In Prova (Trial)"
                        c2.write(status_label)
                        
                        # Pulsante per cambiare stato
                        btn_label = "Disattiva" if user['active'] else "Attiva"
                        if c3.button(btn_label, key=f"toggle_{user['username']}", use_container_width=True):
                            auth.toggle_user_status(user['username'])
                            st.rerun() # Ricarica per vedere il cambio di stato
                        
                        st.markdown("---") # Separatore tra utenti
        
        except Exception as e:
            st.error(f"Errore nel caricamento utenti: {e}")
            
        st.markdown('</div>', unsafe_allow_html=True)