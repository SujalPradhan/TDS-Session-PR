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


@app.route("/chat", methods=["POST"])
def chat():
#Endpoint with system prompt and user message
    data = request.json
    system_prompt = data.get("system_prompt", "You are a helpful assistant.")
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


@app.route("/secret", methods=["GET"])
def secret():
    secret_key = os.getenv("my-secret-key")
    return jsonify({"secret": secret_key})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)