from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

print("My AI Chatbot 🤖")
print("Type exit to stop")
messages = [
    {
        "role": "system",
        "content": "You are a friendly AI tutor. Explain everything in simple language with examples."
    }
]

while True:
    question = input("You: ")
    messages.append({
    "role": "user",
    "content": question
})

    if question.lower() == "exit":
        print("Goodbye! 👋")
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    answer = response.choices[0].message.content
    messages.append({
    "role": "assistant",
    "content": answer
})

    print("Bot:", answer)