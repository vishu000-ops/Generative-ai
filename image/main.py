#gen ai
from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()

key = os.getenv("GOOGLE_API_KEY")

client = OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

user_query = input(">")

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite",
    messages=[
        {"role": "user", "content": user_query}
    ]
)

print(response.choices[0].message.content)


