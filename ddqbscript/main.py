import streamlit as st
import json
import os
import zipfile
import io

from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

# Interfaccia utente Streamlit
st.title("Scraper Web con IA")
url = st.text_input("Inserisci URL del sito web")

# Passaggio 1: Scraping del sito web
if st.button("Scrapa sito web"):
    if url:
        st.write("Scraping del sito web in corso...")

        # Scraping del sito web
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)

        # Salvataggio del contenuto DOM nello stato della sessione di Streamlit
        st.session_state.dom_content = cleaned_content

        # Visualizzazione del contenuto DOM in una casella espandibile
        with st.expander("Visualizza contenuto DOM"):
            st.text_area("Contenuto DOM", cleaned_content, height=300)

# Passaggio 2: Fare domande sul contenuto DOM
if "dom_content" in st.session_state:
    parse_description = st.text_area("Descrivi cosa vuoi analizzare")

    if st.button("Analizza contenuto"):
        if parse_description:
            st.write("Analisi del contenuto in corso...")

            # Analisi del contenuto con Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.session_state.parsed_result = parsed_result
            st.write(parsed_result)

# Tasto per scaricare i risultati
if "parsed_result" in st.session_state:
    if st.button("Scarica risultati"):
        # Crea un file JSON
        json_data = {
            "url": url,
            "parse_description": parse_description,
            "parsed_result": st.session_state.parsed_result
        }

        # Crea un file ZIP in memoria
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Aggiunge risultato.json
            zip_file.writestr('risultato.json', json.dumps(json_data, indent=2, ensure_ascii=False))
            
            # Aggiunge risultato.txt
            zip_file.writestr('risultato.txt', st.session_state.parsed_result)

        # Prepara il download
        zip_buffer.seek(0)
        st.download_button(
            label="Scarica risultati (JSON + TXT)",
            data=zip_buffer,
            file_name="risultati_scraping.zip",
            mime="application/zip"
        )