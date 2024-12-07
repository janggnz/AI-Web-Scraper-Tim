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

# Streamlit User Interface
st.title("Web Scraper with AI")
url = st.text_input("Insert the website URL")

# Step 1: Scraping the website
if st.button("Scrape the website"):
    if url:
        st.write("Scraping website...")

        # Scraping the website
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)

        # Saving DOM content in the Streamlit session state
        st.session_state.dom_content = cleaned_content

        # Displaying the DOM content in a collapsible box
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)

# Step 2: Ask questions about the DOM content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to analyze")

    if st.button("Analyze content"):
        if parse_description:
            st.write("Analyzing content...")

            # Analyzing the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.session_state.parsed_result = parsed_result
            st.write(parsed_result)

# Button to download results
if "parsed_result" in st.session_state:
    if st.button("Download results"):
        # Create a JSON file
        json_data = {
            "url": url,
            "parse_description": parse_description,
            "parsed_result": st.session_state.parsed_result
        }

        # Create a ZIP file in memory
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Add result.json
            zip_file.writestr('result.json', json.dumps(json_data, indent=2, ensure_ascii=False))
            
            # Add result.txt
            zip_file.writestr('result.txt', st.session_state.parsed_result)

        # Prepare for download
        zip_buffer.seek(0)
        st.download_button(
            label="Download Results (JSON + TXT)",
            data=zip_buffer,
            file_name="scraping_results.zip",
            mime="application/zip"
        )
