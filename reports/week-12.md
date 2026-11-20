# Semester Week 12 Progress Report

## Completed Work

I implemented CSV loading, dataset inspection, and
descriptive statistics in csv_tools.py.

I created a synthetic sales dataset and eight automated tests.
I also added the total row count to the statistics output.

## Important Commits

- Commit hash: 4e2652a63a6c59434e3760ad08babe78093c1e82
- Description: Added CSV loading, statistics, and eight tests.
- Link: https://github.com/aknurerjankyzy14-spec/css4007-ai-agents-final/commit/4e2652a63a6c59434e3760ad08babe78093c1e82

- Commit hash: c8cccbf
- Description: Added the total row count and updated its test.
- Link: https://github.com/aknurerjankyzy14-spec/css4007-ai-agents-final/commit/c8cccbf



## Current Functionality

The program loads a local CSV file and reports:

- Row and column counts.
- Column names and data types.
- Missing values in each column.
- Total rows and valid numeric observations.
- Mean, median, minimum, maximum, and sum.

For the test sales column, the verified results are:

- Total rows: 4
- Valid values: 3
- Missing values: 1
- Mean: 200
- Median: 200
- Minimum: 100
- Maximum: 300
- Sum: 600

The results are returned as Python dictionaries.
LLM-selected tool calls and educational explanations
are planned for the next development stage.

## Problems Encountered

I initially called the statistics function before loading
the dataframe.

Later, one test failed because it expected total_rows,
but the function did not yet return this field.

## Solutions

I loaded the dataframe before using it.

I added total_rows to the function output and reran
the tests. All eight tests passed.

Missing values are excluded from calculations,
and their count is reported separately.

## What I Learned

I learned how to load and inspect CSV data with pandas,
handle missing values, and calculate descriptive statistics.

I also learned how to use pytest and read a failed assertion
to identify a difference between expected and actual output.

## Next Week

I will register dataset inspection and statistics
as LLM-callable tools.

The model will select tools, receive their results,
and explain them in simple language.

I will add argument validation, tool execution logs,
integration tests, and begin chart creation.

## Test Results

Command:

python -m pytest test_csv_tools.py -v

Environment:

- Python 3.13.2
- pandas 2.3.2
- pytest 9.2.0

Latest result:

8 passed in 0.60s

The tests cover valid CSV loading, missing-value inspection,
correct statistics, unknown columns, text columns,
all-missing numeric columns, empty files, and header-only files.

File-size and row-limit checks are implemented.
Their automated tests are still planned.

## AI Assistance

ChatGPT helped prepare the code, tests, and report,
and explained the implementation.

I ran the program and tests locally and reviewed the results.
