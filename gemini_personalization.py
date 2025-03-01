import google.generativeai as genai
import os

# Configure Gemini API

api_key = os.getenv("GEMINI_API_KEY")
  # Get API key from environment variables
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please set it before running the script.")

genai.configure(api_key=api_key)

def analyze_study_pattern(student_input):
    prompt = f"Analyze the student's strengths and weaknesses based on: '{student_input}'. Provide personalized recommendations."
    
    # Correct API call
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)

    return response.text  # Extracting text from the response

if _name_ == "_main_":
    student_text = input("Enter student's learning feedback: ")
    result = analyze_study_pattern(student_text)
    print(f"📚 Study Recommendation: {result}")
