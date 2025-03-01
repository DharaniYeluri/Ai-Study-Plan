import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("🚨 GEMINI_API_KEY is missing! Check your .env file.")

genai.configure(api_key=api_key)

def predict_performance(hours_studied):
    prompt = f"If a student studies {hours_studied} hours daily, predict their performance and suggest improvements."
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text

if _name_ == "_main_":
    hours = input("Enter hours studied: ")
    print(f"📈 Performance Prediction: {predict_performance(hours)}")
