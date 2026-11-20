# Setup and Run

## Requirements

- Python 3.13.2, used for development.
- An OpenAI API key with access to gpt-4.1-mini.
- An internet connection for LLM requests.

## Installation

Open the project folder in a terminal and install:

```powershell
python -m pip install openai==3.46.0 python-dotenv==1.2.4 pandas==2.3.2 pytest==9.2.0
```

## Configuration

Create a file named .env in the project root:

```dotenv
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4.1-mini
```

Replace the placeholder with your own key.
Keep .env excluded from Git.

## Week 11 — LLM Prototype

Run from the project root:

```powershell
python week11_api.py
```

The program prints the model name, question, and model answer.
To try another question, edit the question variable in week11_api.py.

Two real requests were completed:

1. Explain the meaning of the median.
2. Calculate the median of 10, 20, 30, 40.

The second request returned the correct result of 25.

## Week 12 — CSV Analysis

Run the CSV demonstration:

```powershell
python csv_tools.py
```

The program loads data/test_sales.csv and displays:

- Row and column counts.
- Column names and data types.
- Missing-value counts.
- Total rows and valid numeric observations.
- Mean, median, minimum, maximum, and sum.

The CSV demonstration runs locally without an API key.

The sample file contains synthetic data.
For the sales column, the expected results are:

- Total rows: 4
- Valid values: 3
- Missing values: 1
- Mean: 200
- Median: 200
- Minimum: 100
- Maximum: 300
- Sum: 600

## Automated Tests

Run:

```powershell
python -m pytest test_csv_tools.py -v
```

The latest local run completed with:

```text
8 passed in 0.60s
```

The tests cover CSV loading, missing values, statistics,
unknown columns, text columns, all-missing numeric columns,
empty files, and header-only files.

## Current Development Stage

The project includes a working LLM API prototype
and CSV analysis functions with eight passing tests.

LLM-selected analysis tools, educational explanations,
charts, and the Streamlit interface are planned
for subsequent development stages.

## AI Assistance

ChatGPT assisted with the code, tests, and documentation.
The student ran the programs and tests locally
and reviewed the results.