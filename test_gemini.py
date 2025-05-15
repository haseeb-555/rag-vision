import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-2.0-flash-001")

response = model.generate_content([{"text": "write poem about real madrid ynadamas"}])

print("Response:", response.text)