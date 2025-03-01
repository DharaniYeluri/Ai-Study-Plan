from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("🚨 GEMINI_API_KEY is missing! Check your .env file.")

genai.configure(api_key=api_key)

# Initialize Flask App
app = Flask(_name_)
CORS(app)  # Allow frontend to call API

@app.route("/")  
def home():
    return "🎉 AI Study Planner API is running!"

@app.route("/update_plan", methods=["POST"])
def update_plan():
    data = request.json
    progress = data.get("progress", 0)
    
    prompt = f"The student has a progress score of {progress}%. Adjust their study plan accordingly."
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)

    return jsonify({"updated_plan": response.text})

if _name_ == "_main_":
    app.run(debug=True)
