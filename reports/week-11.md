# Semester Week 11 Progress Report

## Completed Work

I implemented the first working LLM prototype in week11_api.py.

The program loads configuration from a local .env file,
sends a question to gpt-4.1-mini through the OpenAI API,
validates that the answer is not empty, and displays it
in the terminal.

I ran two real requests and reviewed their answers.


## Important Commits

- Commit hash: 183b47a2c0a27e204d0c9d8679afdc5378574971
- Description: Added the Week 11 working LLM API prototype.
- Link: https://github.com/aknurerjankyzy14-spec/css4007-ai-agents-final/commit/183b47a2c0a27e204d0c9d8679afdc5378574971



## Current Functionality

The application can answer a general statistics question
through a real LLM API.

The current version uses a terminal interface.

Request 1:
"What is a median? Explain it in two sentences."

Result:
The model explained that the median is the middle value
of sorted data. The explanation did not include the rule
for an even number of observations.

Request 2:
"Find the median of 10, 20, 30, 40.
Explain the calculation in simple English."

Result:
The model correctly calculated (20 + 30) / 2 = 25
and explained the steps.

These were two manual checks of actual model responses.

## Problems Encountered


The Ollama installer download failed because the connection
was interrupted. Another download attempt was very slow.

This prevented me from completing the planned local model setup.


## Solutions


I changed the model connection from local Qwen through Ollama
to gpt-4.1-mini through the OpenAI API.

The Python environment is version 3.13.2.
The installed libraries are openai 3.46.0
and python-dotenv 1.2.4.

API configuration is stored in the local .env file.

## What I Learned

I learned how to load environment variables, construct
system and user messages, and send a request to an LLM API.

I also learned to check the returned answer and compare
numerical results with a manual calculation.

The median of 10, 20, 30, 40 is 25 because it is
the average of the two middle values.

## Next Week
I will implement CSV loading, file validation,
dataset inspection, and descriptive statistics.

I will add initial application tests and continue
developing the planned Streamlit interface.
