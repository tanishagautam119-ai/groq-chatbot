from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

messages = [
    {
        "role": "system",
        "content": """You are a helpful, friendly general-purpose AI assistant.
Answer questions clearly and accurately.
Use simple language when possible.
If the user asks for step-by-step help, explain it step by step."""
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    messages.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    bot_message = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": bot_message
    })

    return jsonify({
        "reply": bot_message
    })


if __name__ == "__main__":
    app.run(debug=True)