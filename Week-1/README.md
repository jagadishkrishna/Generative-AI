# Gemini API Python Demo

A small Python project that sends a prompt to Google's Gemini API and
prints the generated response. The current prompt asks Gemini to explain
the fundamentals of Object-Oriented Programming (OOP) in Java.

## Features

-   Loads configuration from a `.env` file.
-   Reads the Gemini API key from `GEMINI_API_KEY`.
-   Allows the model name to be configured with `GEMINI_MODEL`.
-   Tries a list of candidate model names if a model is unavailable.
-   Retries temporary API availability or rate-limit errors, with a
    short delay.
-   Prints the generated response in the terminal.

## Project structure

``` text
project/
├── main.py
├── requirements.txt
├── .env                 # Local secrets; do not commit
└── README.md
```

## Requirements

-   Python 3.9 or newer
-   A Google Gemini API key

Install the dependencies:

``` bash
pip install -r requirements.txt
```

The project dependencies currently listed in `requirements.txt` are:

-   `google-genai` --- Google Gemini API client
-   `python-dotenv` --- loads environment variables from `.env`
-   `openai` --- OpenAI API client (not currently used by `main.py`)
-   `pytest` --- testing framework

## Configuration

Create a `.env` file in the project root:

``` env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_available_gemini_model
```

`GEMINI_MODEL` is optional. If it is not set, `main.py` uses its
configured default and fallback model list.

**Keep your API key private.** Do not paste it into source code, publish
it, or commit `.env` to Git. Add the following to `.gitignore`:

``` gitignore
.env
.venv/
__pycache__/
.pytest_cache/
```

If a real API key has been shared or exposed, revoke or rotate it in the
provider's console and update your local `.env` file.

## Run the project

From the project directory, run:

``` bash
python main.py
```

The script sends the configured prompt to Gemini and prints the
response. An internet connection and a valid API key are required.

## Error handling

The script includes handling for common API issues:

-   **Missing API key:** stops with an error explaining that
    `GEMINI_API_KEY` must be configured.
-   **Model not found:** moves on to the next candidate model.
-   **Temporary unavailability or rate limiting:** retries with a short
    delay.
-   **Other errors:** raises the exception so the underlying problem is
    visible.

Model names and availability can change. Set `GEMINI_MODEL` to a model
currently available to your API key if the configured candidates do not
work.

## Notes

-   The prompt is currently hard-coded in `main.py`. Edit the `contents`
    value passed to `client.models.generate_content()` to ask a
    different question.
-   `openai` and `pytest` are listed as dependencies, but the current
    `main.py` does not use them.
-   No test files are included in the provided project files.

## Troubleshooting

1.  Confirm that `.env` is in the same directory from which you run the
    project.

2.  Check that the variable is spelled exactly `GEMINI_API_KEY`.

3.  Confirm that the API key is valid and has access to the selected
    model.

4.  Upgrade the dependencies if needed:

    ``` bash
    pip install --upgrade -r requirements.txt
    ```

5.  Run the script again:

    ``` bash
    python main.py
    ```

## License

No license file was included with the project. Add a license if you
intend to distribute or publish this project.
