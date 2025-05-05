# 📞 Telecom Chatbot

An AI-powered telecom customer support chatbot built using **Flask**, **HTML/CSS**, and the **OpenRouter AI API**. This chatbot can answer telecom-related queries such as recharge help, plan information, and more.

---

## 🚀 Features

- Chat interface for users to ask telecom-related questions
- Backend built with Python (Flask) and integrated with OpenRouter AI
- Real-time responses using LLM (Language Model)
- Fully working local server (`localhost`) environment
- CORS enabled for frontend-backend communication

---

## 🧠 Tech Stack

| Layer        | Tech Used             |
|--------------|------------------------|
| Frontend     | HTML, CSS, JavaScript  |
| Backend      | Python (Flask)         |
| AI Model     | OpenRouter (LLM API)   |
| Hosting (local)| Flask dev server     |

---
*
Install required packages:
bash-
pip install flask flask-cors requests

Run the server:
bash-
python app.py

This project uses OpenRouter AI, which acts as a gateway to access large language models (LLMs).

You’ll need an API key from https://openrouter.ai
*

Limitations-
-Relies entirely on the LLM's ability to generate correct answers (may hallucinate)
-Requires internet connection to work (for API calls)
-Not trained on specific telecom datasets — it uses general knowledge

To Do / Future Improvements-
-Add telecom-specific FAQs
-Add support for multiple languages
-Deploy using services like Render or Railway
