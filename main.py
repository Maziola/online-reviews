import streamlit as st
import auth_handler as auth 
import openai
from styles import get_logo_html, apply_custom_styles, apply_custom_font

# --- COLLEGAMENTO A TRANSLATIONS E MODULI ---
from translations import t, LANG_MAP, t_list
from sidebar import render_sidebar
from admin_panel import render_admin_zone

# --- SETUP PAGINA ---
st.set_page_config(page_title="Reviews Master Pro", layout="wide", page_icon="⭐")
apply_custom_font("Ubuntu")
apply_custom_styles()

# --- CONFIGURAZIONE OPENAI (Secrets) ---
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
except:
    pass

# Inizializzazione sessione
if "current_lang_code" not in st.session_state: st.session_state.current_lang_code = "it"
if "auth" not in st.session_state: st.session_state.auth = False
if "username" not in st.session_state: st.session_state.username = ""
if "history_item" not in st.session_state: st.session_state.history_item = None

# Funzione per generare le risposte reali
def genera_risposte_ai(recensione, contesto, tono, business_name, categoria):
    prompt = f"""
    Sei un esperto di Customer Care per un'attività di tipo {categoria} chiamata {business_name}.
    Il tono della risposta deve essere: {tono}.
    Recensione del cliente: "{recensione}"
    Note aggiuntive/Contesto: "{contesto}"
    
    Genera 3 varianti di risposta diverse. 
    Separa rigorosamente le varianti con il simbolo '###'.
    """
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Sei un assistente professionale che scrive risposte alle recensioni."},
                      {"role": "user", "content": prompt}],
            temperature=0.7
        )
        testo_totale = response.choices[0].message.content
        return testo_totale.split('###')
    except Exception as e:
        return [f"Errore API: {str(e)}", "", ""]

# --- LOGICA DI ACCESSO ---
if not st.session_state.auth:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    
    with col_r:
        lang_list = list(LANG_MAP.keys())
        current_code = st.session_state.get("current_lang_code", "it")
        try:
            current_index = list(LANG_MAP.values()).index(current_code)
        except:
            current_index = 0
            
        sel_lang = st.selectbox("🌐", lang_list, index=current_index, key="login_lang_picker")
        if LANG_MAP[sel_lang] != st.session_state.current_lang_code:
            st.session_state.current_lang_code = LANG_MAP[sel_lang]
            st.rerun()

    with col_m:
        st.markdown(get_logo_html(80), unsafe_allow_html=True)
        
        # Tabs tradotte: richiamano correttamente la funzione t()
        tab_login, tab_reg = st.tabs([t("login_tab"), t("reg_tab")])
        
        with tab_login:
            with st.form("login_form"):
                u = st.text_input(t("user_label"))
                p = st.text_input(t("pass_label"), type="password")
                if st.form_submit_button(t("btn_login"), use_container_width=True):
                    success, status, rem = auth.check_auth(u, p)
                    if success:
                        st.session_state.auth = True
                        st.session_state.username = u
                        st.rerun()
                    else: 
                        st.error(t("auth_error"))
        
        with tab_reg:
            with st.form("registration_form"):
                new_u = st.text_input(t("user_label"))
                new_p = st.text_input(t("pass_label"), type="password")
                if st.form_submit_button(t("btn_reg"), use_container_width=True):
                    ok, msg = auth.register_user(new_u, new_p)
                    if ok: 
                        st.success(msg)
                    else: 
                        st.error(msg)
    st.stop()

# --- APP INTERNA ---
render_sidebar()
st.markdown(get_logo_html(60), unsafe_allow_html=True)

if st.session_state.username.lower() == "admin":
    render_admin_zone()
    st.markdown("---")

# Visualizzazione Storico o Generatore
if st.session_state.history_item:
    item = st.session_state.history_item
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader(f"📜 {t('last_analyses')}: {item[3]}")
    st.info(f"**{t('txt_rec')}**\n\n{item[1]}")
    st.success(f"**Risposta:**\n\n{item[2]}")
    if st.button("🔙 Torna al Generatore"):
        st.session_state.history_item = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown(t("dash_title"))

    col1, col2 = st.columns(2)
    with col1:
        rev_text = st.text_area(t("txt_rec"), height=180)
    with col2:
        ctx_text = st.text_area(t("extra_ctx"), height=180)

    if st.button(t("btn_gen"), use_container_width=True):
        if rev_text:
            with st.spinner("..."):
                b_name = st.session_state.get("sb_name", "Business")
                b_cat = st.session_state.get("sb_cat", "General")
                b_tone = st.session_state.get("sb_tone", "Professional")
                
                varianti = genera_risposte_ai(rev_text, ctx_text, b_tone, b_name, b_cat)
                auth.save_review(st.session_state.username, b_cat, b_name, rev_text, varianti[0])

                st.markdown("---")
                st.success(t("success_msg"))
                v_cols = st.columns(3)
                for i, v in enumerate(varianti[:3]):
                    with v_cols[i]:
                        st.markdown(f"#### Opzione {i+1}")
                        st.write(v)
                        st.button(f"Copia {i+1}", key=f"cp_{i}")
        else:
            st.warning(t("txt_rec"))
    st.markdown('</div>', unsafe_allow_html=True)