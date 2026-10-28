# 🌐 BhashaMitra AI

### Your AI Language Companion — Breaking Language Barriers with AI

BhashaMitra AI is an AI-powered multilingual assistant designed to help users communicate, learn, summarize, translate, and improve text in different languages. It aims to make AI more accessible through a simple and user-friendly interface.

## ✨ Features

- 💬 **AI Chat Assistant** — Ask questions and receive AI-generated responses.
- 🌍 **Multilingual Support** — Select Hindi, Marathi, or English.
- 🎙️ **Voice Input** — Speak your message using browser speech recognition where supported.
- 🔊 **Text-to-Speech** — Listen to AI responses using browser speech synthesis.
- 📚 **Study Mode** — Get help understanding topics and learning concepts.
- 📝 **Summarization** — Summarize text into concise information.
- 🔄 **Translation Mode** — Get help translating text between languages.
- ✍️ **Text Improvement** — Improve the clarity and wording of your text.
- 🎨 **User-Friendly Interface** — A modern, responsive interface designed for ease of use.

## 🛠️ Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript
- Browser Speech Recognition and Speech Synthesis APIs

**Backend**
- Python
- FastAPI
- Uvicorn

**AI Integration**
- Sarvam AI API

**Deployment**
- Vercel — Frontend
- Render — Backend
- GitHub — Source code and version control

## 📁 Project Structure

```text
bhashamitra-ai/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── index.html
│   └── app.html
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd bhashamitra-ai
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Set Up the Backend

Open a terminal in the project directory:

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure the API Key

Create a `.env` file inside the `backend` folder:

```env
SARVAM_API_KEY=your_sarvam_api_key
```

Replace the placeholder with your own Sarvam AI API key.

**Security:** Never publish your API key in GitHub or commit your `.env` file.

### 4. Run the Backend

From the `backend` directory, run:

```bash
uvicorn main:app --reload
```

The backend should be available at:

`http://127.0.0.1:8000`

### 5. Open the Frontend

Open `frontend/index.html` in your browser to access the homepage. Open `frontend/app.html` to access the AI assistant.

For local development, ensure the frontend's configured API URL points to your running backend.

## 🌍 Live Demo

- **Frontend:** https://bhashamitra-ai-frontend.vercel.app/
- **Backend:** https://bhashamitra-ai.onrender.com

## 🔐 Environment Variables

The backend requires the following environment variable:

| Variable | Description |
|---|---|
| `SARVAM_API_KEY` | API key used for Sarvam AI integration |

Configure this variable in the backend hosting provider's environment settings for production.

## 🎯 Project Goal

The goal of BhashaMitra AI is to make AI-powered communication and learning easier for people who prefer Indian languages, especially Hindi and Marathi, alongside English.

## 🔮 Future Improvements

- Persistent chat history and conversation management
- Improved voice conversations
- More Indian language options
- Document upload and summarization
- Better error handling and loading indicators
- Accessibility and mobile usability improvements

## 🤝 Contributing

Contributions and suggestions are welcome. Fork the repository, create a branch, make your changes, and submit a pull request.

## 📄 License

No license has been specified yet. Add a license file if you want to define the terms under which others may use, modify, or distribute this project.

---

**Built with ❤️ by Team BhashaMitra AI**
