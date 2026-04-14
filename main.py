import streamlit as st
import os
import auth_handler as auth 
from styles import get_logo_html, apply_custom_styles, apply_custom_font

# ==============================================================================
# 1. SISTEMA DI TRADUZIONE INTEGRALE
# ==============================================================================
LANG_MAP = {
    "🇮taliano": "it",
    "English": "en",
    "🇫rançais": "fr",
    "Allemand": "de",
    "🇪spagnol": "es"
}

TRANSLATIONS = {
    # --- LOGIN & AUTH ---
    "page_title": {
        "it": "Reviews Master Pro - Gestione Intelligente", 
        "en": "Reviews Master Pro - Smart Management", 
        "fr": "Reviews Master Pro - Gestion Intelligente", 
        "de": "Reviews Master Pro - Smartes Management", 
        "es": "Reviews Master Pro - Gestión Inteligente"
    },
    "tab_login": {
        "it": "🔑 Accesso Utente", 
        "en": "🔑 User Login", 
        "fr": "🔑 Connexion Utilisateur", 
        "de": "🔑 Benutzer-Login", 
        "es": "🔑 Acceso Usuario"
    },
    "tab_reg": {
        "it": "📝 Registrazione Business", 
        "en": "📝 Business Registration", 
        "fr": "📝 Inscription Entreprise", 
        "de": "📝 Firmenregistrierung", 
        "es": "📝 Registro de Empresa"
    },
    "login_welcome": {
        "it": "##### Bentornato! Accedi al tuo account", 
        "en": "##### Welcome back! Log in to your account", 
        "fr": "##### Bon retour ! Connectez-vous", 
        "de": "##### Willkommen zurück! Einloggen", 
        "es": "##### ¡Bienvenido! Accede a tu cuenta"
    },
    "user_email": {"it": "Username o Email", "en": "Username or Email", "fr": "Nom d'utilisateur o Email", "de": "Benutzername oder E-Mail", "es": "Usuario o Email"},
    "user_placeholder": {"it": "Inserisci il tuo nome utente...", "en": "Enter your username...", "fr": "Entrez votre nom d'utilisateur...", "de": "Geben Sie Ihren Benutzernamen ein...", "es": "Introduce tu usuario..."},
    "password": {"it": "Password", "en": "Password", "fr": "Mot de passe", "de": "Passwort", "es": "Contraseña"},
    "pwd_placeholder": {"it": "Inserisci la tua password...", "en": "Enter your password...", "fr": "Entrez votre mot de passe...", "de": "Geben Sie Ihr Passwort ein...", "es": "Introduce tu contraseña..."},
    "btn_login": {"it": "ACCEDI AL PORTALE", "en": "LOGIN TO PORTAL", "fr": "ACCÉDER AU PORTAIL", "de": "ZUM PORTAL ANMELDEN", "es": "ACCEDER AL PORTAL"},
    "err_login": {"it": "Credenziali non valide. Verifica i dati e riprova.", "en": "Invalid credentials. Please verify and try again.", "fr": "Identifiants invalides. Veuillez réessayer.", "de": "Ungültige Anmeldedaten. Bitte überprüfen.", "es": "Credenciales inválidas. Verifica los datos."},
    
    # --- REGISTRATION ---
    "reg_title": {"it": "##### Crea il tuo profilo Master Pro", "en": "##### Create your Master Pro profile", "fr": "##### Créez votre profil Master Pro", "de": "##### Erstellen Sie Ihr Profil", "es": "##### Crea tu perfil Master Pro"},
    "reg_user": {"it": "Scegli un Username unico", "en": "Choose a unique Username", "fr": "Nom d'utilisateur unique", "de": "Benutzername wählen", "es": "Elige un Usuario"},
    "reg_pwd": {"it": "Imposta una Password sicura", "en": "Set a secure Password", "fr": "Mot de passe sécurisé", "de": "Sicheres Passwort", "es": "Contraseña segura"},
    "btn_reg": {"it": "REGISTRATI ORA", "en": "REGISTER NOW", "fr": "S'INSCRIRE", "de": "REGISTRIEREN", "es": "REGÍSTRATE"},

    # --- SIDEBAR ---
    "hello": {"it": "### Ciao, **{}**", "en": "### Hello, **{}**", "fr": "### Bonjour, **{}**", "de": "### Hallo, **{}**", "es": "### Hola, **{}**"},
    "prof_biz": {"it": "##### 🏢 Profilo dell'Attività", "en": "##### 🏢 Business Profile", "fr": "##### 🏢 Profil de l'Entreprise", "de": "##### 🏢 Profil", "es": "##### 🏢 Perfil de la Empresa"},
    "biz_name": {"it": "Nome Business:", "en": "Business Name:", "fr": "Nom de l'entreprise :", "de": "Name:", "es": "Nombre Empresa:"},
    "cat_merc": {"it": "Categoria Merceologica:", "en": "Business Category:", "fr": "Catégorie :", "de": "Kategorie:", "es": "Categoría:"},
    "exp_str": {"it": "✨ Punti di Forza Unici", "en": "✨ Unique Strengths", "fr": "✨ Points Forts", "de": "✨ Stärken", "es": "✨ Puntos Fuertes"},
    "exp_srv": {"it": "🚗 Servizi & Logistica", "en": "🚗 Services & Logistics", "fr": "🚗 Services & Logistique", "de": "🚗 Service", "es": "🚗 Servicioss"},
    "exp_pol": {"it": "🛡️ Policy & Reclami", "en": "🛡️ Policies & Complaints", "fr": "🛡️ Politique & Réclamations", "de": "🛡️ Richtlinien", "es": "🛡️ Políticas"},
    "exp_sign": {"it": "🖋️ Firma Personalizzata", "en": "🖋️ Custom Signature", "fr": "🖋️ Signature", "de": "🖋️ Signatur", "es": "🖋️ Firma"},
    "hist_title": {"it": "##### 📜 Cronologia Ultime Analisi", "en": "##### 📜 Recent History", "fr": "##### 📜 Historique", "de": "##### 📜 Verlauf", "es": "##### 📜 Historial"},
    "btn_new": {"it": "✍️ NUOVA ANALISI", "en": "✍️ NEW ANALYSIS", "fr": "✍️ NOUVELLE ANALYSE", "de": "✍️ NEUE ANALYSE", "es": "✍️ NUEVO ANÁLISIS"},
    "btn_logout": {"it": "Log out / Esci", "en": "Log out", "fr": "Déconnexion", "de": "Abmelden", "es": "Cerrar sesión"},

    # --- MAIN ---
    "dash_title": {"it": "### ✨ Generatore di Risposte:", "en": "### ✨ Reply Generator:", "fr": "### ✨ Générateur :", "de": "### ✨ Generator:", "es": "### ✨ Generador:"},
    "dati_rec": {"it": "##### 📝 Dati della Recensione", "en": "##### 📝 Review Data", "fr": "##### 📝 Données de l'Avis", "de": "##### 📝 Daten", "es": "##### 📝 Datos de la Reseña"},
    "sel_tone": {"it": "Seleziona il tono:", "en": "Select tone:", "fr": "Choisir le ton :", "de": "Ton wählen:", "es": "Elige el tono:"},
    "txt_rec": {"it": "Testo della recensione:", "en": "Review text:", "fr": "Texte de l'avis :", "de": "Bewertungstext:", "es": "Texto de la reseña:"},
    "det_spec": {"it": "##### 💡 Dettagli Specifici", "en": "##### 💡 Specific Details", "fr": "##### 💡 Détails", "de": "##### 💡 Details", "es": "##### 💡 Detalles"},
    "extra_ctx": {
        "it": "Contesto extra / Note specifiche:", 
        "en": "Extra context / Specific notes:", 
        "fr": "Contexte supplémentaire / Notes :", 
        "de": "Extra-Kontext / Spezifische Notizen:", 
        "es": "Contexto extra / Notas específicas:"
    },
    "btn_gen": {"it": "GENERA 3 VARIANTI ✨", "en": "GENERATE 3 VARIANTS ✨", "fr": "GÉNÉRER 3 VARIANTES ✨", "de": "3 VARIANTEN GENERIEREN ✨", "es": "GENERAR 3 VARIANTES ✨"},
    "spin_ai": {"it": "L'IA sta elaborando...", "en": "AI is processing...", "fr": "L'IA traite...", "de": "KI verarbeitet...", "es": "La IA está procesando..."},
    "success_msg": {"it": "✅ Risposte generate e archiviate nello storico!", "en": "✅ Replies generated and archived in history!", "fr": "✅ Réponses générées et archivées !", "de": "✅ Antworten generiert und archiviert!", "es": "✅ ¡Respuestas generadas e archivadas!"},
    
    # --- VARIANTI ---
    "var_a": {"it": "BOZZA A", "en": "DRAFT A", "fr": "BROUILLON A", "de": "ENTWURF A", "es": "BORRADOR A"},
    "var_b": {"it": "BOZZA B", "en": "DRAFT B", "fr": "BROUILLON B", "de": "ENTWURF B", "es": "BORRADOR B"},
    "var_c": {"it": "BOZZA C", "en": "DRAFT C", "fr": "BROUILLON C", "de": "ENTWURF C", "es": "BORRADOR C"}
}

LISTS = {
    "categories": {
        "it": ["Hotel / B&B", "Ristorante / Bar", "E-commerce", "Negozio Fisico", "Servizi", "Altro..."],
        "en": ["Hotel / B&B", "Restaurant / Bar", "E-commerce", "Physical Store", "Services", "Other..."],
        "fr": ["Hôtel / B&B", "Restaurant / Bar", "E-commerce", "Boutique", "Services", "Autre..."],
        "de": ["Hotel / B&B", "Restaurant / Bar", "E-commerce", "Laden", "Dienstleistungen", "Anderes..."],
        "es": ["Hotel / B&B", "Restaurante / Bar", "E-commerce", "Tienda", "Servicios", "Otro..."]
    },
    "tones": {
        "it": ["Professionale", "Cordialità", "Elegante", "Empatico", "Ironico", "Deciso"],
        "en": ["Professional", "Friendly", "Elegant", "Empathetic", "Witty", "Firm"],
        "fr": ["Professionnel", "Amical", "Élégant", "Empathique", "Spirituel", "Ferme"],
        "de": ["Professionell", "Freundlich", "Elegant", "Empathisch", "Witzig", "Entschlossen"],
        "es": ["Profesional", "Amigable", "Elegante", "Empático", "Ingenioso", "Firme"]
    }
}

def t(key):
    lang_code = st.session_state.get("current_lang_code", "it")
    return TRANSLATIONS.get(key, {}).get(lang_code, key)

def t_list(key):
    lang_code = st.session_state.get("current_lang_code", "it")
    return LISTS.get(key, {}).get(lang_code, [])

# ==============================================================================
# 2. CONFIGURAZIONE & CALLBACKS
# ==============================================================================
st.set_page_config(page_title="Reviews Master Pro", layout="wide", page_icon="⭐")
apply_custom_font("Ubuntu")
apply_custom_styles()

def on_lang_change():
    st.session_state.current_lang_code = LANG_MAP[st.session_state.lang_picker]

def on_lang_change_side():
    st.session_state.current_lang_code = LANG_MAP[st.session_state.lang_picker_side]

# ==============================================================================
# 3. GESTIONE SESSIONE
# ==============================================================================
auth.init_db()
if "current_lang_code" not in st.session_state: st.session_state.current_lang_code = "it"
if "auth" not in st.session_state: st.session_state.auth = False
if "username" not in st.session_state: st.session_state.username = ""
if "history_item" not in st.session_state: st.session_state.history_item = None

# ==============================================================================
# 4. AUTENTICAZIONE
# ==============================================================================
if not st.session_state.auth:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m: st.markdown(get_logo_html(80), unsafe_allow_html=True)
    with col_r: st.selectbox("🌐", list(LANG_MAP.keys()), key="lang_picker", on_change=on_lang_change)
    
    tab_login, tab_reg = st.tabs([t("tab_login"), t("tab_reg")])
    with tab_login:
        with st.form("login_form"):
            st.markdown(t("login_welcome"))
            u = st.text_input(t("user_email"), key="l_u", placeholder=t("user_placeholder"))
            p = st.text_input(t("password"), type="password", key="l_p", placeholder=t("pwd_placeholder"))
            if st.form_submit_button(t("btn_login"), use_container_width=True):
                success, _, _ = auth.check_auth(u, p, "Matteo", "123")
                if success:
                    st.session_state.auth = True
                    st.session_state.username = u
                    st.rerun()
                else: st.error(t("err_login"))
    
    with tab_reg:
        with st.form("reg_form"):
            st.markdown(t("reg_title"))
            new_u = st.text_input(t("reg_user"))
            new_p = st.text_input(t("reg_pwd"), type="password")
            if st.form_submit_button(t("btn_reg"), use_container_width=True):
                if new_u and new_p:
                    ok, msg = auth.register_user(new_u, new_p)
                    if ok: st.success(msg)
                    else: st.error(msg)
    st.stop()

# ==============================================================================
# 5. SIDEBAR (Con Rinomina)
# ==============================================================================
with st.sidebar:
    st.selectbox("🌐", list(LANG_MAP.keys()), key="lang_picker_side", on_change=on_lang_change_side)
    st.markdown("---")
    st.markdown(t("hello").format(st.session_state.username))
    st.markdown("---")
    st.markdown(t("prof_biz"))
    biz_name = st.text_input(t("biz_name"), placeholder="es. Grand Hotel", key="sb_name")
    biz_cat = st.selectbox(t("cat_merc"), t_list("categories"), key="sb_cat")

    with st.expander(t("exp_str")):
        k_f = st.text_area("...", height=90, key="sb_kf", label_visibility="collapsed")
    with st.expander(t("exp_srv")):
        ame = st.text_area("...", height=90, key="sb_am", label_visibility="collapsed")
    with st.expander(t("exp_pol")):
        pol = st.text_area("...", height=90, key="sb_po", label_visibility="collapsed")
    with st.expander(t("exp_sign")):
        sig = st.text_input("...", key="sb_sig", label_visibility="collapsed")

    st.markdown("---")
    st.markdown(t("hist_title"))
    
    history_data = auth.get_history(st.session_state.username)
    if history_data:
        for i, item in enumerate(history_data):
            old_label = item[3]
            c_btn, c_edit, c_del = st.columns([0.65, 0.17, 0.18])
            
            with c_btn:
                if st.button(f"🕒 {old_label}", key=f"hi_{i}", use_container_width=True):
                    st.session_state.history_item = item
                    st.rerun()
            
            with c_edit:
                with st.popover("✏️"):
                    new_name = st.text_input("Rename:", value=old_label, key=f"ren_input_{i}")
                    if st.button("OK", key=f"confirm_ren_{i}"):
                        auth.rename_history_item(st.session_state.username, old_label, new_name)
                        st.rerun()
            
            with c_del:
                if st.button("🗑️", key=f"del_{i}"):
                    auth.delete_history_item(st.session_state.username, old_label)
                    st.rerun()
    
    st.markdown("---")
    if st.button(t("btn_new"), use_container_width=True):
        st.session_state.history_item = None
        st.rerun()
    if st.button(t("btn_logout")):
        st.session_state.auth = False
        st.rerun()

# ==============================================================================
# 6. DASHBOARD
# ==============================================================================
st.markdown(get_logo_html(60), unsafe_allow_html=True)

if st.session_state.history_item:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    item = st.session_state.history_item
    st.markdown(f"### 📑 {item[3]}")
    st.markdown("---")
    st.markdown(f"**Recensione:**")
    st.info(item[1])
    st.markdown(f"**Risposta:**")
    st.success(item[2])
    if st.button("🔙 Torna"):
        st.session_state.history_item = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown(f"{t('dash_title')} {biz_cat}")
    col_1, col_2 = st.columns(2, gap="large")
    with col_1:
        st.markdown(t("dati_rec"))
        sel_tone = st.selectbox(t("sel_tone"), t_list("tones"), key="main_tone")
        rev_text = st.text_area(t("txt_rec"), height=250, key="main_rev")
    with col_2:
        st.markdown(t("det_spec"))
        # INTEGRATO: Etichetta tradotta per Contesto Extra
        ctx_text = st.text_area(t("extra_ctx"), height=250, key="main_ctx")

    if st.button(t("btn_gen"), use_container_width=True):
        if rev_text:
            with st.spinner(t("spin_ai")):
                # Simulazione tradotta
                d1 = f"[{st.session_state.current_lang_code.upper()}] Opt 1 per {biz_name}."
                d2 = f"[{st.session_state.current_lang_code.upper()}] Opt 2: {ctx_text[:15]}..."
                d3 = f"[{st.session_state.current_lang_code.upper()}] Opt 3 - {sig}"
                
                full_res = f"1:\n{d1}\n\n2:\n{d2}\n\n3:\n{d3}"
                auth.save_review(st.session_state.username, biz_cat, "", rev_text, full_res)
                
                # Messaggio di successo (Giallo chiaro come da styles.py)
                st.success(t("success_msg"))
                
                # VARIANTI TRADOTTE
                v_col1, v_col2, v_col3 = st.columns(3)
                mappa = [(v_col1, t("var_a"), d1), (v_col2, t("var_b"), d2), (v_col3, t("var_c"), d3)]
                
                for col, titolo, testo in mappa:
                    with col:
                        st.markdown(f"""
                            <div class="variant-card" style="background-color: white; padding: 20px; border-radius: 12px; border-top: 6px solid #367588; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%;">
                                <p style="font-weight: bold; font-size: 0.85rem; margin-bottom: 10px; text-transform: uppercase;">{titolo}</p>
                                <p style="font-size: 0.95rem; line-height: 1.5;">{testo}</p>
                            </div>
                        """, unsafe_allow_html=True)
        else: st.warning("Inserire testo!")
    st.markdown('</div>', unsafe_allow_html=True)