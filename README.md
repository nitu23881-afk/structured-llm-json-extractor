
# Structured LLM Prompt Pipeline & JSON Extractor

## Overview

A Python-based application that uses Google's Gemini API to extract structured information from unstructured invoice text.

The application converts invoice information into validated JSON using Pydantic.

## Features

- Gemini API integration
- Dynamic invoice text input
- Reusable prompt templates
- Few-shot prompt engineering
- Structured JSON generation
- Pydantic data validation
- Missing information handling using null
- Quantity and monetary value validation
- Subtotal and GST calculation verification
- Unique JSON output files
- Error handling

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- Pydantic
- JSON

## Project Structure

```text
LLM_JSON_Extractor/
│
├── main.py
├── test_invoice.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── output/
    └── generated_invoice.json
```

Generated invoice files are excluded from Git.

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd LLM_JSON_Extractor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## API Configuration

Set your Gemini API key as an environment variable.

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

Never commit your API key to GitHub.

## Run the Application

```bash
python main.py
```

Enter invoice details in the terminal.

Press Enter on an empty line to submit the invoice.

The extracted JSON file will be saved in the output folder.

## Run Tests

```bash
python -m pytest -v
```

## Limitations

- Extraction accuracy depends on the input text and LLM response.
- Pydantic validates structure and data types, not the factual correctness of every extracted field.
- The application currently focuses on invoice extraction.
- Human review is recommended before using extracted financial information.

## Future Improvements

- Support PDF invoice uploads.
- Support multiple invoice formats.
- Add source evidence for extracted fields.
- Add a user interface.
