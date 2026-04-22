import streamlit as st
import auth_handler as auth 
from openai import OpenAI  # Import corretto
from styles import get_logo_html, apply_custom_styles, apply_custom_font

# --- 1. CONFIGURAZIONE INIZIALE & CLIENT ---
st.set_page_config(page_title="Reviews Master Pro", layout="wide", page_icon="⭐")

# Inizializza il client OpenAI usando i Secrets di Streamlit
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception as e:
    st.error("Errore: API Key non configurata nei Secrets di Streamlit.")

# --- 2. COLLEGAMENTO MODULI ESTERNI ---
import translations 
from translations import t, LANG_MAP, t_list
from sidebar import render_sidebar
from admin_panel import render_admin_zone

# Applica stili e font
apply_custom_font("Ubuntu")
apply_custom_styles()

# --- 3. INIZIALIZZAZIONE SESSION STATE ---
if "current_lang_code" not in st.session_state: 
    st.session_state.current_lang_code = "it"
if "auth" not in st.session_state: 
    st.session_state.auth = False
if "username" not in st.session_state: 
    st.session_state.username = ""
if "history_item" not in st.session_state: 
    st.session_state.history_item = None

# --- 4. FUNZIONE GENERAZIONE AI (3 VARIANTI) ---
def genera_risposte_ai(review_text, extra_context, tone, biz_name, category):
    varianti = []
    
    prompt_base = f"""
    Sei un esperto di customer care per un'attività di tipo {category} chiamata {biz_name}.
    Rispondi a questa recensione: "{review_text}"
    Tono richiesto: {tone}.
    Dettagli aggiuntivi da includere: {extra_context}.
    """

    for i in range(3):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Sei un assistente professionale che scrive risposte alle recensioni."},
                    {"role": "user", "content": f"{prompt_base}\nGenera la variante numero {i+1}. Deve essere diversa dalle altre."}
                ],
                temperature=0.8 # Leggermente più alta per favorire la diversità tra varianti
            )
            varianti.append(response.choices[0].message.content)
        except Exception as e:
            varianti.append(f"Errore variante {i+1}: {str(e)}")
            
    return varianti

# --- 5. LOGICA DI ACCESSO (LOGIN/REGISTRAZIONE) ---
if not st.session_state.auth:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    
    with col_r:
        lang_list = list(LANG_MAP.keys())
        current_code = st.session_state.current_lang_code
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
        
        tab_login, tab_reg = st.tabs([t("login_tab"), t("reg_tab")])
        
        with tab_login:
            with st.form("login_form"):
                u = st.text_input(t("user_label"), key="login_user")
                p = st.text_input(t("pass_label"), type="password", key="login_pass")
                submit_l = st.form_submit_button(t("btn_login"), use_container_width=True)
                
                if submit_l:
                    success, status, rem = auth.check_auth(u, p)
                    if success:
                        st.session_state.auth = True
                        st.session_state.username = u
                        st.rerun()
                    else: 
                        st.error(t("auth_error"))
        
        with tab_reg:
            with st.form("registration_form"):
                new_u = st.text_input(t("user_label"), key="reg_user")
                new_p = st.text_input(t("pass_label"), type="password", key="reg_pass")
                submit_r = st.form_submit_button(t("btn_reg"), use_container_width=True)
                
                if submit_r:
                    ok, msg = auth.register_user(new_u, new_p)
                    if ok: st.success(msg)
                    else: st.error(msg)
    st.stop()

# --- 6. APP PRINCIPALE (DOPO LOGIN) ---
render_sidebar()
st.markdown(get_logo_html(60), unsafe_allow_html=True)

# Pannello Admin
if st.session_state.username.lower() == "admin":
    render_admin_zone()
    st.markdown("---")

# Visualizzazione Storico o Dashboard
if st.session_state.history_item:
    item = st.session_state.history_item
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader(f"📜 {t('last_analyses')}: {item[3]}")
    st.info(f"**{t('txt_rec')}**\n\n{item[1]}")
    st.success(f"**Risposta salvata:**\n\n{item[2]}")
    if st.button("🔙 Torna"):
        st.session_state.history_item = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown(f"## {t('dash_title')}")
    
    col1, col2 = st.columns(2)
    with col1:
        rev_text = st.text_area(t("txt_rec"), height=180, placeholder="Incolla qui la recensione...")
    with col2:
        ctx_text = st.text_area(t("extra_ctx"), height=180, placeholder="Esempio: Offri uno sconto del 10%...")

    if st.button(t("btn_gen"), use_container_width=True):
        if rev_text:
            with st.spinner(t("loading_msg") if "loading_msg" in translations.TRANSLATIONS else "Generazione in corso..."):
                # Recupero dati dai widget della sidebar
                # Usiamo chiavi dinamiche basate sulla lingua se hai applicato il fix della key
                lang = st.session_state.current_lang_code
                b_name = st.session_state.get("sb_name", "Business")
                b_cat = st.session_state.get(f"sb_cat", "General")
                b_tone = st.session_state.get(f"sb_tone_{lang}", st.session_state.get("sb_tone", "Professional"))
                
                # Generazione
                varianti = genera_risposte_ai(rev_text, ctx_text, b_tone, b_name, b_cat)
                
                # Salva la prima variante nel database come default
                auth.save_review(st.session_state.username, b_cat, b_name, rev_text, varianti[0])
                
                st.success(t("success_msg"))
                
                # Visualizzazione delle 3 varianti in colonne
                v_cols = st.columns(3)
                for i, v in enumerate(varianti):
                    with v_cols[i]:
                        st.markdown(f"#### Variante {i+1}")
                        st.info(v)
                        if st.button(f"Copia Opzione {i+1}", key=f"copy_{i}"):
                            st.code(v) # Comodo per copiare il testo con un click
        else:
            st.warning("Per favore, inserisci il testo di una recensione.")
            
    st.markdown('</div>', unsafe_allow_html=True)