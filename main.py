import os
from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Create a chat completion request
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Can you translate hallo from Dutch into French?",
        }
    ],
    model="gpt-3.5-turbo",
)

if chat_completion.choices:
    response_message = chat_completion.choices[0].message
    print(response_message)