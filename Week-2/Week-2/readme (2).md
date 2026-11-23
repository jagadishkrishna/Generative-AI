# Multi-Provider LLM Client

A lightweight Python command-line application that provides a unified interface for interacting with both cloud-based (Google Gemini) and local (Ollama) Large Language Models.

## Features

- **Unified Interface:** Uses the Strategy design pattern (`LLMProvider` abstract base class) to switch seamlessly between different LLM backends.
- **Cloud Integration:** Connects to Google's Gemini models via the official `google-genai` SDK.
- **Local Execution:** Supports running local open-source models (e.g., Llama 3.2, Mistral) via `ollama`.
- **Environment Management:** Securely loads API keys using `python-dotenv`.

## Project Structure

```text
├── .gitignore          # Specifies intentionally untracked files (e.g., .env, .venv)
├── llm_client.py       # Core abstraction and provider implementations (Gemini & Ollama)
├── main.py             # CLI entry point for selecting a provider and prompting the LLM
├── requirements.txt    # Python package dependencies
└── README.md           # Project documentation
```

## Prerequisites

- **Python 3.8+**
- **Google Gemini API Key** (if using the `gemini` provider)
- **Ollama** installed and running locally (if using the `ollama` provider) with the desired model pulled (e.g., `ollama pull llama3.2`).

## Installation

1. **Clone the repository** (or navigate to your project directory):
   ```bash
   cd your-project-directory
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Ensure the `ollama` Python package is also installed via `pip install ollama` if you plan to use the local provider.)*

## Configuration

1. Create a `.env` file in the root directory of the project.
2. Add your API keys to the `.env` file using the following format:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
OPEN_ROUTE_KEY=your_actual_openroute_key_here
```

> **Security Warning:** Never commit your `.env` file or expose your actual API keys in public repositories. Ensure `.env` remains listed in your `.gitignore`. *(If you have accidentally shared your keys publicly, revoke and regenerate them immediately in your provider dashboards.)*

## Usage

Run the main script from your terminal:

```bash
python main.py
```

Follow the interactive prompts:
1. Choose your provider by typing `gemini` or `ollama`.
2. Enter your question or prompt.
3. View the generated response in the console.

### Example

```text
Choose provider (gemini/ollama): gemini
Enter your question: Explain the Strategy design pattern in one sentence.

LLM Response:
The Strategy design pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime.
```