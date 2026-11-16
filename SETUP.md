# Setup and Run

## Requirements

- Python 3.13.2, used for development.
- An OpenAI API key with access to gpt-4.1-mini.
- An internet connection.

## Installation

Open the project folder in a terminal and install the libraries:

```powershell
python -m pip install openai==3.46.0 python-dotenv==1.2.4
```

## Configuration

Create a file named .env in the project root:

```dotenv
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4.1-mini
```

Replace the placeholder with your own key.
Keep .env excluded from Git.

## Run

From the project root, execute:

```powershell
python week11_api.py
```

The program prints the model name, question, and model answer.
To try another question, edit the question variable in week11_api.py.

## Manual Verification

Two real requests were completed:

1. Explain the meaning of the median.
2. Calculate the median of 10, 20, 30, 40.

The second request returned the correct result of 25.

## Current Development Stage

The Week 11 prototype answers general statistics questions
in the terminal. CSV loading, analysis tools, and the Streamlit
interface are planned for later development stages.

## AI Assistance

ChatGPT assisted with the prototype and documentation.
The student ran the program locally and reviewed its answers.