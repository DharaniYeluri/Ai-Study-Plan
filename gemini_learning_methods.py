import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()  
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("🚨 GEMINI_API_KEY is missing! Check your .env file.")

genai.configure(api_key=api_key)

def recommend_learning_method(topic):
    prompt = f"Suggest the best learning method (video, quiz, text) for learning '{topic}', and recommend a specific resource."
    
    model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Correct Gemini model
    response = model.generate_content(prompt)

    return response.text

if _name_ == "_main_":
    topic = input("Enter topic: ")
    print(f"🎓 Recommended Learning Method: {recommend_learning_method(topic)}")
