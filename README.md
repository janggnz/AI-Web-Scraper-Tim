# AI Web Scraper con Ollama

Questo progetto ti permette di fare il scraping dei siti web e analizzare il loro contenuto utilizzando il modello Llama3 di Ollama. Il programma estrae e processa i dati dai siti web, permettendoti di fare domande sul contenuto DOM estratto e di scaricare i risultati.

Se preferisci la versione in inglese di questo progetto, puoi trovarla [qui](https://github.com/dddevid/AI-Web-Scraper-Ollama).

## Requisiti

Prima di cominciare, assicurati di avere installato:

- Python 3.8 o superiore
- `pip` (gestore di pacchetti Python)

### Passaggio 1: Installa Ollama e Llama3

1. **Scarica Ollama**:
   - Ollama è una piattaforma che esegue modelli di intelligenza artificiale come Llama3. Puoi scaricare Ollama per il tuo sistema dal sito ufficiale:  
     [Download Ollama](https://ollama.com/download)

2. **Installa il modello Llama3**:
   - Dopo aver scaricato Ollama, devi installare il modello Llama3. Apri un terminale o prompt dei comandi e esegui il seguente comando per installare il modello Llama3:
     ```
     ollama install llama3
     ```

### Passaggio 2: Clona il Repository

1. **Clona il repository**:
   - Per prima cosa, clona il repository GitHub sulla tua macchina locale eseguendo il seguente comando, specificando il branch italiano:
     ```
     git clone --branch Italian https://github.com/dddevid/AI-Web-Scraper-Ollama.git
     ```

2. **Naviga nella cartella del progetto**:
   - Cambia nella cartella del progetto eseguendo:
     ```
     cd AI-Web-Scraper-Ollama
     ```

### Passaggio 3: Configura l'Ambiente Python

1. **Crea un ambiente virtuale (opzionale ma consigliato)**:
   - Crea un ambiente virtuale per gestire le dipendenze del progetto:
     ```
     python -m venv venv
     ```

2. **Attiva l'ambiente virtuale**:
   - Su Windows:
     ```
     venv\Scripts\activate
     ```
   - Su macOS/Linux:
     ```
     source venv/bin/activate
     ```

3. **Installa le dipendenze richieste**:
   - Il file `requirements.txt` si trova nella cartella `ddbqscript`. Installa le librerie Python necessarie eseguendo:
     ```
     pip install -r ddbqscript/requirements.txt
     ```

### Passaggio 4: Esegui l'Applicazione

#### Su Windows:

- **Esegui lo script utilizzando il file batch**:
  - Usa il file `Executethescript.bat` per avviare l'applicazione:
    ```
    Executethescript.bat
    ```

#### Su macOS/Linux:

- **Esegui lo script utilizzando Streamlit**:
  - Avvia l'app Streamlit eseguendo il seguente comando:
    ```
    streamlit run ddbqscript/main.py
    ```

2. **Accedi all'app**:
   - L'interfaccia Streamlit si aprirà nel tuo browser. Ora puoi inserire un URL di un sito web, fare scraping del suo contenuto e analizzarlo usando Llama3.

### Passaggio 5: Utilizzo

- **Fare scraping di un sito web**: Inserisci un URL e clicca su "Scrape the website" per fare scraping del contenuto del sito.
- **Analizzare il contenuto**: Dopo aver fatto lo scraping, puoi inserire una descrizione di cosa vuoi analizzare, e l'IA processerà il contenuto.
- **Scaricare i risultati**: Una volta completata l'analisi, puoi scaricare i risultati nei formati JSON e TXT.

### Risoluzione dei Problemi

- **Ollama non trovato**: Se ricevi un errore relativo a Ollama, assicurati che sia correttamente installato e che sia aggiunto al PATH del sistema.
- **Dipendenze mancanti**: Assicurati di aver installato tutte le librerie Python necessarie eseguendo `pip install -r ddbqscript/requirements.txt`.

---

### Se ti è piaciuto questo progetto, puoi offirmi un caffè! ☕

[![Buy me a coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://buymeacoffee.com/devidd)
