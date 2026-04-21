import streamlit as st

# Mappa delle lingue per i codici brevi
LANG_MAP = {
    "🇮taliano": "it",
    "English": "en",
    "🇫rançais": "fr",
    "Allemand": "de",
    "🇪spagnol": "es"
}

# Liste per i menu a tendina
LISTS = {
    "categories": {
        "it": ["Hotel / B&B", "Ristorante / Bar", "E-commerce", "Negozio Fisico", "Studio Professionale", "Servizi alla Persona", "Altro..."],
        "en": ["Hotel / B&B", "Restaurant / Bar", "E-commerce", "Physical Store", "Professional Studio", "Personal Services", "Other..."]
    },
    "tones": {
        "it": ["Professionale", "Cordialità", "Elegante", "Empatico", "Ironico", "Deciso"],
        "en": ["Professional", "Friendly", "Elegant", "Empathetic", "Witty", "Firm"]
    }
}

# Dizionario traduzioni testuali
TRANSLATIONS = {
    "admin_panel": {"it": "🛠️ Pannello Amministratore", "en": "🛠️ Admin Panel", "fr": "🛠️ Panneau Admin", "de": "🛠️ Admin-Bereich", "es": "🛠️ Panel de Admin"},
    "admin_desc": {"it": "Gestione attivazione utenti (Trial 14gg):", "en": "User activation management (14-day Trial):", "fr": "Gestion des utilisateurs (Essai 14j) :", "de": "Benutzerverwaltung (14 Tage Testversion):", "es": "Gestión de usuarios (Prueba 14 días):"},
    "btn_gen": {"it": "GENERA 3 VARIANTI ✨", "en": "GENERATE 3 VARIANTS ✨", "fr": "GÉNÉRER 3 VARIANTES ✨", "de": "3 VARIANTEN GENERIEREN ✨", "es": "GENERAR 3 VARIANTES ✨"},
    "dash_title": {"it": "### ✨ Generatore di Risposte:", "en": "### ✨ Reply Generator:", "fr": "### ✨ Générateur :", "de": "### ✨ Generator:", "es": "### ✨ Generador:"},
    "txt_rec": {"it": "Testo della recensione:", "en": "Review text:", "fr": "Texte de l'avis :", "de": "Bewertungstext:", "es": "Texto de la reseña:"},
    "extra_ctx": {"it": "Contesto extra / Note specifiche:", "en": "Extra context / Specific notes:", "fr": "Contexte supplémentaire / Notes :", "de": "Extra-Kontext / Spezifische Notizen:", "es": "Contexto extra / Notas específicas:"},
    "success_msg": {"it": "✅ Risposte generate e archiviate!", "en": "✅ Replies generated!", "fr": "✅ Réponses générées !", "de": "✅ Generiert!", "es": "✅ ¡Generadas!"},
    "biz_name": {"it": "Nome Business:", "en": "Business Name:", "fr": "Nom :", "de": "Name:", "es": "Nombre:"},
    "cat_merc": {"it": "Categoria Merceologica:", "en": "Category:", "fr": "Catégorie :", "de": "Kategorie:", "es": "Categoría:"},
    "prof_biz": {"it": "Profilo Attività", "en": "Business Profile", "fr": "Profil Entreprise", "de": "Unternehmensprofil", "es": "Perfil de Empresa"}
}

# Funzione per ottenere la traduzione semplice
def t(key):
    lang_code = st.session_state.get("current_lang_code", "it")
    return TRANSLATIONS.get(key, {}).get(lang_code, key)

# Funzione per ottenere le liste tradotte
def t_list(key):
    lang_code = st.session_state.get("current_lang_code", "it")
    # Se la lingua non è presente nella lista, usa l'italiano come fallback
    return LISTS.get(key, {}).get(lang_code, LISTS.get(key, {}).get("it", []))