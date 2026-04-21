import streamlit as st

# Mappa delle lingue per i codici brevi
LANG_MAP = {
    "🇮taliano": "it",
    "English": "en",
    "🇫rançais": "fr",
    "Deutsch": "de",
    "🇪spagnol": "es"
}

# Liste per i menu a tendina (Categorie e Toni)
LISTS = {
    "categories": {
        "it": ["Hotel / B&B", "Ristorante / Bar", "E-commerce", "Negozio Fisico", "Studio Professionale", "Servizi alla Persona", "Altro..."],
        "en": ["Hotel / B&B", "Restaurant / Bar", "E-commerce", "Physical Store", "Professional Studio", "Personal Services", "Other..."],
        "fr": ["Hôtel / B&B", "Restaurant / Bar", "E-commerce", "Boutique Physique", "Cabinet Professionnel", "Services à la Personne", "Autre..."],
        "de": ["Hotel / B&B", "Restaurant / Bar", "E-Commerce", "Ladengeschäft", "Professionelles Studio", "Persönliche Dienstleistungen", "Andere..."],
        "es": ["Hotel / B&B", "Restaurante / Bar", "E-commerce", "Tienda Física", "Estudio Profesional", "Servicios Personales", "Otro..."]
    },
    "tones": {
        "it": ["Professionale", "Cordialità", "Elegante", "Empatico", "Ironico", "Deciso"],
        "en": ["Professional", "Friendly", "Elegant", "Empathetic", "Witty", "Firm"],
        "fr": ["Professionnel", "Cordial", "Élégant", "Empathique", "Ironique", "Ferme"],
        "de": ["Professionell", "Freundlich", "Elegant", "Empathisch", "Ironisch", "Bestimmt"],
        "es": ["Profesional", "Cordial", "Elegante", "Empático", "Irónico", "Firme"]
    }
}

# Dizionario traduzioni testuali
TRANSLATIONS = {
    # ADMIN PANEL
    "admin_panel": {"it": "🛡️ Pannello Amministratore", "en": "🛡️ Admin Panel", "fr": "🛡️ Panneau Admin", "de": "🛡️ Admin-Bereich", "es": "🛡️ Panel de Admin"},
    "admin_desc": {"it": "Gestione attivazione utenti (Trial 14gg):", "en": "User activation management (14-day Trial):", "fr": "Gestion des utilisateurs (Essai 14j) :", "de": "Benutzerverwaltung (14 Tage Testversion):", "es": "Gestión de usuarios (Prueba 14 días):"},
    "no_users": {"it": "Non ci sono ancora utenti registrati oltre all'admin.", "en": "There are no registered users besides the admin.", "fr": "Il n'y a pas encore d'utilisateurs inscrits à part l'admin.", "de": "Es gibt noch keine registrierten Benutzer außer dem Admin.", "es": "Aún no hay usuarios registrados además del administrador."},
    
    # GENERATORE & DASHBOARD
    "dash_title": {"it": "### ✨ Generatore di Risposte:", "en": "### ✨ Reply Generator:", "fr": "### ✨ Générateur :", "de": "### ✨ Generator:", "es": "### ✨ Generador:"},
    "btn_gen": {"it": "GENERA 3 VARIANTI ✨", "en": "GENERATE 3 VARIANTS ✨", "fr": "GÉNÉRER 3 VARIANTES ✨", "de": "3 VARIANTEN GENERIEREN ✨", "es": "GENERAR 3 VARIANTES ✨"},
    "txt_rec": {"it": "Testo della recensione:", "en": "Review text:", "fr": "Texte de l'avis :", "de": "Bewertungstext:", "es": "Texto de la reseña:"},
    "extra_ctx": {"it": "Contesto extra / Note specifiche:", "en": "Extra context / Specific notes:", "fr": "Contexte supplémentaire / Notes :", "de": "Extra-Kontext / Spezifische Notizen:", "es": "Contexto extra / Notas específicas:"},
    "success_msg": {"it": "✅ Risposte generate e archiviate!", "en": "✅ Replies generated!", "fr": "✅ Réponses générées !", "de": "✅ Generiert!", "es": "✅ ¡Generadas!"},
    
    # SIDEBAR
    "prof_biz": {"it": "Profilo Attività", "en": "Business Profile", "fr": "Profil Entreprise", "de": "Unternehmensprofil", "es": "Perfil de Empresa"},
    "biz_name": {"it": "Nome Business:", "en": "Business Name:", "fr": "Nom de l'entreprise :", "de": "Name des Unternehmens:", "es": "Nombre de la empresa:"},
    "cat_label": {"it": "Categoria", "en": "Category", "fr": "Catégorie", "de": "Kategorie", "es": "Categoría"},
    "tone_label": {"it": "Tono della risposta", "en": "Response Tone", "fr": "Ton de la réponse", "de": "Antwortton", "es": "Tono de la respuesta"},
    "punti_forza": {"it": "Punti di forza", "en": "Strengths", "fr": "Points forts", "de": "Stärken", "es": "Puntos fuertes"},
    "policy_firma": {"it": "Policy e Firma", "en": "Policy & Signature", "fr": "Politique et Signature", "de": "Richtlinien & Signatur", "es": "Política y Firma"},
    "lang_app": {"it": "Lingua App", "en": "App Language", "fr": "Langue de l'App", "de": "App-Sprache", "es": "Idioma de la App"},
    "last_analyses": {"it": "Ultime analisi", "en": "Last analyses", "fr": "Dernières analyses", "de": "Letzte Analysen", "es": "Últimas análisis"},
    "no_analyses": {"it": "Nessuna analisi salvata", "en": "No saved analyses", "fr": "Aucune analyse enregistrée", "de": "Keine gespeicherten Analysen", "es": "No hay análisis guardados"},
    "confirm_del": {"it": "Eliminare?", "en": "Delete?", "fr": "Supprimer?", "de": "Löschen?", "es": "¿Eliminar?"},

    # AUTH & LOGIN
    "login_tab": {"it": "🔑 ACCESSO", "en": "🔑 LOGIN", "fr": "🔑 CONNEXION", "de": "🔑 ANMELDEN", "es": "🔑 ACCESO"},
    "reg_tab": {"it": "📝 REGISTRAZIONE", "en": "📝 REGISTER", "fr": "📝 INSCRIPTION", "de": "📝 REGISTRIEREN", "es": "📝 REGISTRO"},
    "user_label": {"it": "Username", "en": "Username", "fr": "Nom d'utilisateur", "de": "Benutzername", "es": "Usuario"},
    "pass_label": {"it": "Password", "en": "Password", "fr": "Mot de passe", "de": "Passwort", "es": "Contraseña"},
    "btn_login": {"it": "ACCEDI AL PORTALE", "en": "LOGIN TO PORTAL", "fr": "ACCÉDER AU PORTAIL", "de": "ZUM PORTAL ANMELDEN", "es": "ACCEDER AL PORTAL"},
    "btn_reg": {"it": "REGISTRA", "en": "REGISTER", "fr": "S'INSCRIRE", "de": "REGISTRIEREN", "es": "REGISTRARSE"},
    "auth_error": {"it": "Credenziali errate o Trial scaduto.", "en": "Invalid credentials or Trial expired.", "fr": "Identifiants invalides ou essai expiré.", "de": "Ungültige Anmeldedaten oder Testversion abgelaufen.", "es": "Credenciales inválidas o prueba expirada."}
}

def t(key):
    """ Ottiene la traduzione testuale """
    lang_code = st.session_state.get("current_lang_code", "it")
    # Fallback all'italiano se la lingua non esiste per quella chiave, poi alla chiave stessa
    return TRANSLATIONS.get(key, {}).get(lang_code, TRANSLATIONS.get(key, {}).get("it", key))

def t_list(key):
    """ Ottiene le liste tradotte (Categorie/Toni) """
    lang_code = st.session_state.get("current_lang_code", "it")
    # Fallback all'inglese, poi italiano
    return LISTS.get(key, {}).get(lang_code, LISTS.get(key, {}).get("en", LISTS.get(key, {}).get("it", [])))