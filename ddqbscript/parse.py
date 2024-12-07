#parse.py

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "Sei incaricato di estrarre informazioni specifiche dal seguente contenuto testuale: {dom_content}. "
    "Segui attentamente queste istruzioni: \n\n"
    "1. **Estrazione Informazioni:** Estrai solo le informazioni che corrispondono direttamente alla descrizione fornita: {parse_description}. "
    "2. **Nessun Contenuto Aggiuntivo:** Non includere testo, commenti o spiegazioni aggiuntive nella tua risposta. "
    "3. **Risposta Vuota:** Se nessuna informazione corrisponde alla descrizione, restituisci una stringa vuota ('')."
    "4. **Solo Dati Diretti:** L'output deve contenere solo i dati esplicitamente richiesti, senza altro testo."
)

model = OllamaLLM(model="llama3")


def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Batch analizzato: {i} di {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)