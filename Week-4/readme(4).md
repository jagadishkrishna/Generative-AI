# LLM Toolkit: Multi-Provider Client, Token Economics & Tokenizer Comparison

A modular Python toolkit for working with Large Language Models. It provides a unified CLI for interacting with cloud (Google Gemini) and local (Ollama) models, a Token Economics & Capacity Planner for pre-deployment cost and rate-limit estimation, and a Multilingual Tokenizer Comparison utility to analyze how different tokenization algorithms handle English, Telugu, and Hindi text.

## Features

### 1. Multi-Provider LLM Client (`main.py`, `llm_client.py`)
* **Unified Interface:** Uses the Strategy design pattern (`LLMProvider` abstract base class) to switch seamlessly between different LLM backends.
* **Cloud Integration:** Connects to Google's Gemini models via the official `google-genai` SDK.
* **Local Execution:** Supports running local open-source models (e.g., Llama 3.2, Mistral) via `ollama`.

### 2. Token Economics & Budget Planner (`budget.py`, `test_budget.py`)
* **Cost Estimation:** Calculates daily and monthly token consumption and USD costs based on per-million token pricing.
* **Capacity & Rate-Limit Checks:** Evaluates peak Requests Per Minute (RPM) and Tokens Per Minute (TPM) against provider rate limits, factoring in a configurable safety margin.
* **Automated Validation:** Includes a unit test suite (`test_budget.py`) to verify cost calculations, capacity thresholds, and budget boundaries.

### 3. Multilingual Tokenizer Comparison (`tokenizer_comparison.py`)
* **Algorithm Comparison:** Compares three major tokenization strategies using Hugging Face `transformers`:
  * **BPE (Byte-Pair Encoding):** `gpt2`
  * **WordPiece:** `bert-base-multilingual-cased`
  * **SentencePiece:** `xlm-roberta-base`
* **Multilingual Benchmarking:** Evaluates token splits, token IDs, and total token counts across **English**, **Telugu**, and **Hindi** sample sentences to highlight tokenization efficiency across scripts.

## Project Structure

```text
├── .gitignore                 # Specifies intentionally untracked files (e.g., .env, .venv)
├── llm_client.py              # Core abstraction and provider implementations (Gemini & Ollama)
├── main.py                    # CLI entry point for selecting a provider and prompting the LLM
├── budget.py                  # Token economics, cost estimation, and rate-limit validation tool
├── test_budget.py             # Unit tests for the FeatureBudget calculator
├── tokenizer_comparison.py    # Compares BPE, WordPiece, and SentencePiece across languages
├── requirements.txt           # Dependencies for the LLM Client
├── requirements_2.txt         # Minimal dependencies for the Token Economics Planner
├── requirements_3.txt         # Dependencies for the Tokenizer Comparison script
└── README.md                  # Project documentation
```

## Prerequisites

* **Python 3.8+**
* **Google Gemini API Key** (if using the `gemini` provider in `main.py`)
* **Ollama** installed and running locally (if using the `ollama` provider) with the desired model pulled (e.g., `ollama pull llama3.2`).
* **Internet Connection** on first run of `tokenizer_comparison.py` to download pretrained tokenizer vocabularies from Hugging Face.

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
   Install the packages for the specific modules you plan to run (or install all three):
   ```bash
   # For the Multi-Provider LLM Client
   pip install -r requirements.txt

   # For the Token Economics & Budget Planner
   pip install -r requirements_2.txt

   # For the Multilingual Tokenizer Comparison
   pip install -r requirements_3.txt
   ```
   *(Note: If using Ollama locally, ensure `pip install ollama` is also installed.)*

## Configuration

Create a `.env` file in the root directory of the project to configure your API keys, usage assumptions, pricing, and budget limits for `main.py` and `budget.py`:

```env
# --- LLM Provider API Keys ---
GEMINI_API_KEY=your_actual_gemini_api_key_here
OPEN_ROUTE_KEY=your_actual_openroute_key_here

# --- Token Economics & Pricing (USD per 1,000,000 tokens) ---
INPUT_PRICE_PER_MILLION=0.30
OUTPUT_PRICE_PER_MILLION=1.20

# --- Traffic & Token Usage Assumptions ---
REQUESTS_PER_DAY=2000
AVG_INPUT_TOKENS=1200
AVG_OUTPUT_TOKENS=300
PEAK_REQUESTS_PER_MINUTE=30

# --- Provider Rate Limits (Illustrative — verify actual limits) ---
RPM_LIMIT=60
TPM_LIMIT=100000

# --- Budget & Safety Thresholds ---
MONTHLY_BUDGET_USD=50
DAILY_BUDGET_USD=2
SAFETY_MARGIN_PERCENT=20
```

> **Security Warning:** Never commit your `.env` file or expose your actual API keys in public repositories. Ensure `.env` remains listed in your `.gitignore`.

## Usage

### 1. Running the LLM Client

Run the main interactive CLI script:
```bash
python main.py
```

Follow the prompts to choose your provider (`gemini` or `ollama`) and enter your question:
```text
Choose provider (gemini/ollama): gemini
Enter your question: Explain the Strategy design pattern in one sentence.

LLM Response:
The Strategy design pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime.
```

### 2. Running the Token Economics Report

Evaluate whether your projected traffic and token usage fit within your budget and rate limits:
```bash
python budget.py
```

#### Example Output
```text
TOKEN ECONOMICS REPORT
-----------------------------------
Input tokens/day:  2,400,000
Output tokens/day: 600,000
Total tokens/day:  3,000,000
Estimated daily cost:   $1.4400
Estimated monthly cost: $43.20
Peak RPM with margin: 36.0
Peak TPM with margin: 54000

CHECKS
RPM capacity: PASS
TPM capacity: PASS
Daily budget: PASS
Monthly budget: REVIEW

Recommendation: REVISE assumptions, limits, or design before build.
```

#### Running Budget Unit Tests
```bash
python -m unittest test_budget.py
# Or using pytest:
pytest
```

### 3. Running the Multilingual Tokenizer Comparison

Compare how GPT-2 (BPE), Multilingual BERT (WordPiece), and XLM-RoBERTa (SentencePiece) tokenize English, Telugu, and Hindi text:
```bash
python tokenizer_comparison.py
```

#### Example Output
```text
Loading BPE - GPT-2...
Loading WordPiece - Multilingual BERT...
Loading SentencePiece - XLM-R...

===========================================================================
LANGUAGE: English
INPUT TEXT: Artificial intelligence is changing the world.
===========================================================================

BPE - GPT-2
Tokens     : ['Art', 'ificial', 'Ġintelligence', 'Ġis', 'Ġchanging', 'Ġthe', 'Ġworld', '.']
Token IDs  : [8001, 9542, 4430, 318, 5609, 262, 995, 13]
Token count: 8
...
```

## Extending the Project

* **Add a New LLM Provider:** Subclass `LLMProvider` in `llm_client.py`, implement the `generate(self, prompt)` method, and register it in `main.py`.
* **Add More Languages or Tokenizers:** Add new entries to the `TOKENIZERS` or `TEXTS` dictionaries in `tokenizer_comparison.py` to benchmark additional models or scripts.