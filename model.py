import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

client = OpenAI(api_key=api_key)

def predict_category(description):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Categorize expense into Food, Travel, Shopping, Bills, Other"},
                {"role": "user", "content": description}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "Other"
