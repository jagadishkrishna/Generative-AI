# Multi-Provider LLM Client & Token Economics Planner

A lightweight Python toolkit featuring a unified command-line interface for interacting with both cloud-based (Google Gemini) and local (Ollama) Large Language Models, alongside a Token Economics & Capacity Planner to estimate API costs and rate-limit readiness before deployment.

## Features

### 1. Multi-Provider LLM Client (`main.py`, `llm_client.py`)
* **Unified Interface:** Uses the Strategy design pattern (`LLMProvider` abstract base class) to switch seamlessly between different LLM backends.
* **Cloud Integration:** Connects to Google's Gemini models via the official `google-genai` SDK.
* **Local Execution:** Supports running local open-source models (e.g., Llama 3.2, Mistral) via `ollama`.

### 2. Token Economics & Budget Planner (`budget.py`, `test_budget.py`)
* **Cost Estimation:** Calculates daily and monthly token consumption and USD costs based on per-million token pricing.
* **Capacity & Rate-Limit Checks:** Evaluates peak Requests Per Minute (RPM) and Tokens Per Minute (TPM) against provider rate limits, factoring in a configurable safety margin.
* **Automated Validation:** Includes a unit test suite (`test_budget.py`) to verify cost calculations, capacity thresholds, and budget boundaries.

## Project Structure

```text
├── .gitignore          # Specifies intentionally untracked files (e.g., .env, .venv)
├── llm_client.py       # Core abstraction and provider implementations (Gemini & Ollama)
├── main.py             # CLI entry point for selecting a provider and prompting the LLM
├── budget.py           # Token economics, cost estimation, and rate-limit validation tool
├── test_budget.py      # Unit tests for the FeatureBudget calculator
├── requirements.txt    # Primary Python package dependencies
├── requirements_2.txt  # Minimal dependencies for the standalone budget calculator
└── README.md           # Project documentation
```

## Prerequisites

* **Python 3.8+**
* **Google Gemini API Key** (if using the `gemini` provider)
* **Ollama** installed and running locally (if using the `ollama` provider) with the desired model pulled (e.g., `ollama pull llama3.2`).

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
   *(Note: If you only want to run the budget calculator, you can install `pip install -r requirements_2.txt`. If using Ollama locally, ensure `pip install ollama` is also installed.)*

## Configuration

Create a `.env` file in the root directory of the project to configure your API keys, usage assumptions, pricing, and budget limits:

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

### 3. Running Unit Tests

Run the test suite to verify the budget and capacity calculations:

```bash
python -m unittest test_budget.py
```
or using `pytest`:
```bash
pytest
```

## Extending the Project

To add a new LLM provider (such as OpenRouter, which is already referenced in `.env`):
1. Create a new class in `llm_client.py` that inherits from `LLMProvider`.
2. Implement the `generate(self, prompt)` method.
3. Add the new provider option to the selection logic in `main.py`.