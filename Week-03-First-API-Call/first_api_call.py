
import os
from dotenv import load_dotenv
from openai import OpenAI

# Step 1: Load API keys from .env
load_dotenv()

# Step 2: Choose your provider
PROVIDER = "gemini"  # Change to "gemini" to test Gemini

# Step 3: Provider configuration

if PROVIDER == "openai":
    api_key = os.getenv("OPENAI_API_KEY")
    model = "gpt-6-luna"
    base_url = None

    input_price = 0.10
    output_price = 0.50

elif PROVIDER == "gemini":
    api_key = os.getenv("GEMINI_API_KEY")
    model = "gemini-3.1-flash-lite"
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

    input_price = 0.25
    output_price = 1.50

else:
    raise ValueError("Invalid provider selected.")

if not api_key:
    raise ValueError(f"Missing API key for {PROVIDER}. Check your .env file.")

# Step 4: Create the API client
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

# Step 5: Define your prompts
system_prompt = (
    "You are a helpful academic advisor. "
    "Explain academic concepts in simple English."
)

user_prompt = (
    "Explain how GPA affects course registration "
    "in a credit-hour university system. "
    "Keep your answer short."
)

# Step 6: Send the API request
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

# Step 7: Print the response
print("\n" + "=" * 50)
print(f"Provider: {PROVIDER.upper()}")
print(f"Model: {model}")
print("=" * 50)

print("\nModel Response:\n")
print(response.choices[0].message.content)



# Step 8: Read token usage
usage = response.usage

if usage is not None:
    input_tokens = usage.prompt_tokens
    output_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens

    if None not in (input_tokens, output_tokens, total_tokens):

        # Step 9: Calculate estimated cost
        estimated_cost = (
            (input_tokens * input_price) +
            (output_tokens * output_price)
        ) / 1_000_000

        # Step 10: Display results
        print("\n" + "=" * 50)
        print("TOKEN USAGE & COST")
        print("=" * 50)

        print(f"Input Tokens:   {input_tokens}")
        print(f"Output Tokens:  {output_tokens}")
        print(f"Total Tokens:   {total_tokens}")
        print(f"Estimated Cost: ${estimated_cost:.8f}")

    else:
        print("Token counts are incomplete.")

else:
    print("Token usage is not available.")
