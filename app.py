from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here or from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY_HERE")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a construction industry expert. Answer clearly and professionally."},
                {"role": "user", "content": user_message}
            ]
        )
        answer = response.choices[0].message["content"]
        return jsonify({"reply": answer})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
