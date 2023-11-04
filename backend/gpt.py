import openai
from decouple import config  # If you're using a .env file

# Load your API key from the environment variable or .env file
api_key = config('OPENAI_API_KEY')

# Initialize the OpenAI client
openai.api_key = api_key

# Define a function to send a message to ChatGPT
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300  # Adjust this as needed
    )
    return response.choices[0].text