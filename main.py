from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv()
# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

with open("system_prompt.txt", "r") as f:
    system_prompt = f.read()

@app.route("/chat", methods=["POST"])
def chat():
#Endpoint with system prompt and user message
    data = request.json
    system_prompt = system_prompt
    user_message = data.get("user_message", "")
    response = model.generate_content(
        system=system_prompt,
        user=user_message,
    )
    return jsonify({
        "system_prompt": system_prompt,
        "user_message": user_message,
        "response": response.text
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


students = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 22},
    {"id": 3, "name": "Charlie", "age": 21},
    {"id": 4, "name": "David", "age": 23},
    {"id": 5, "name": "Eve", "age": 20},
    {"id": 6, "name": "Frank", "age": 22}
]

app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True, port=5000)