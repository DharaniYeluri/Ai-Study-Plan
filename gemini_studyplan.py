from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(_name_)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def adjust_plan(progress):
    prompt = f"The student has a progress score of {progress}%. Adjust their study plan accordingly with specific recommendations."
    response = genai.generate_text(model="gemini-pro", prompt=prompt)
    return response.result

@app.route('/update_plan', methods=['POST'])
def update_plan():
    data = request.json
    progress = data.get("progress", 0)
    updated_plan = adjust_plan(progress)
    return jsonify({"updated_plan": updated_plan})

if _name_ == "_main_":
    app.run(debug=True)
