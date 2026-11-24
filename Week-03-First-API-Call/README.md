# Week 3 Assignment — Your First API Call

## Project Description

This project demonstrates how to make API calls to two AI providers, OpenAI and Google Gemini, using Python and the OpenAI SDK.

The script sends a system prompt and a user prompt, displays the model's response, retrieves token usage, and calculates the estimated cost of each API call.

## Technologies Used

- Python
- OpenAI Python SDK
- python-dotenv
- OpenAI API
- Google Gemini API

## Models Tested

- OpenAI: `gpt-6-luna`
- Google Gemini: `gemini-3.1-flash-lite`

## How to Run

1. Install the required libraries:

   `pip install -r requirements.txt`

2. Create a `.env` file containing your API keys:

   `OPENAI_API_KEY=your_key`

   `GEMINI_API_KEY=your_key`

3. Select the provider in `first_api_call.py` by changing `PROVIDER` to `"openai"` or `"gemini"`.

4. Run:

   `python first_api_call.py`

## Results

| Metric | OpenAI | Gemini |
|---|---:|---:|
| Input Tokens | 42 | 35 |
| Output Tokens | 114 | 237 |
| Total Tokens | 156 | 272 |
| Estimated Cost | $0.00006120 | $0.00036425 |

The results show that OpenAI produced a shorter response with fewer tokens and a lower estimated cost in this test, while Gemini provided a longer and more detailed response.

These results represent individual test calls. Actual token usage and cost may vary between runs.

## Security

API keys are stored in a `.env` file, which is excluded from Git using `.gitignore`. No API keys are included in the source code.

## Output Files

- `outputs/openai_output.txt`
- `outputs/gemini_output.txt`

Both files contain the model responses, token usage, and estimated costs.