# AI Web Scraper with Ollama

This project allows you to scrape websites and analyze their content using Ollama's Llama3 AI model. The scraper fetches and processes data from websites, allowing you to ask questions about the extracted DOM content and download the results.

If you prefer the Italian version of this project, you can find it [here](https://github.com/dddevid/AI-Web-Scraper-Ollama/tree/Italian).

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.8 or higher
- `pip` (Python package installer)

### Step 1: Install Ollama and Llama3

1. **Download Ollama**:
   - Ollama is a platform that runs AI models like Llama3. You can download Ollama for your system from the official website:  
     [Ollama Download](https://ollama.com/download)

2. **Install Llama3 model**:
   - After downloading Ollama, you need to install the Llama3 model. Open a terminal or command prompt and run the following command to install the Llama3 model:
     ```
     ollama install llama3
     ```

### Step 2: Clone the Repository

1. **Clone the repository**:
   - First, clone the GitHub repository to your local machine by running the following command:
     ```
     git clone https://github.com/dddevid/AI-Web-Scraper-Ollama.git
     ```

2. **Navigate into the project directory**:
   - Change into the project directory by running:
     ```
     cd AI-Web-Scraper-Ollama
     ```

### Step 3: Set up the Python Environment

1. **Create a virtual environment (optional but recommended)**:
   - Create a virtual environment to manage the project's dependencies:
     ```
     python -m venv venv
     ```

2. **Activate the virtual environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

3. **Install required dependencies**:
   - The `requirements.txt` file is located in the `ddbqscript` folder. Install the necessary Python libraries by running:
     ```
     pip install -r ddbqscript/requirements.txt
     ```

### Step 4: Run the Application

#### On Windows:

- **Run the script using the batch file**:
  - Use the `Executethescript.bat` file to start the application:
    ```
    Executethescript.bat
    ```

#### On macOS/Linux:

- **Run the script using Streamlit**:
  - Start the Streamlit app by running the following command:
    ```
    streamlit run ddbqscript/main.py
    ```

2. **Access the app**:
   - The Streamlit interface should open in your web browser. You can now enter a website URL, scrape its content, and analyze it using Llama3.

### Step 5: Usage

- **Scraping a website**: Enter a URL and click on "Scrape the website" to scrape the site's content.
- **Analyzing content**: After scraping, you can input a description of what you want to analyze, and the AI will process the content.
- **Downloading results**: Once the analysis is complete, you can download the results in both JSON and TXT formats.

### Troubleshooting

- **Ollama not found**: If you encounter an error related to Ollama, make sure it is correctly installed and added to your system's PATH.
- **Missing dependencies**: Ensure all required Python packages are installed by running `pip install -r ddbqscript/requirements.txt`.

---

### If you enjoyed this project, you can buy me a coffee! ☕

[![Buy me a coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://buymeacoffee.com/devidd)

By clicking the link, you can choose to donate any amount or subscribe for 30€ per month to support the ongoing development of this project.
