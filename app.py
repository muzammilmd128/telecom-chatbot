from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# Set your OpenRouter API key here
openai.api_key = "Type_APIkey_Here"
openai.api_base = "https://openrouter.ai/api/v1"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    try:
        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {"role": "system", "content": "You are a helpful telecom assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response['choices'][0]['message']['content'].strip()
        return jsonify({'reply': reply})
    except Exception as e:
        print("Chatbot error:", e)
        return jsonify({'reply': "Error: " + str(e)})

if __name__ == '__main__':
    app.run(debug=True)
