# 🌐 BhashaMitra AI: Your AI Language Companion

**HackFront India | Problem Statement: Open Source and Innovation**

BhashaMitra AI is an AI-powered multilingual assistant that helps people communicate, learn, summarize, translate and improve text in **Hindi, Marathi and English**. It breaks language barriers by letting users talk to AI in the language they are most comfortable with, by typing or by speaking, and by listening to the answers.

## Links

| What | Link |
|------|------|
| Source code | https://github.com/khushiiiiiiii153/bhashamitra-ai |
| Live demo (web app) | https://bhashamitra-ai-frontend-tm2z.vercel.app |

## Team Visionaries (Dream · Innovate · Build)

| Name | Role |
|------|------|
| Yogesh Mondhe | Team Leader |
| Khushi Wanjari | Team Member |

## Problem statement

Most AI tools work best in English. Many students, families and small business owners in India are more comfortable in Hindi or Marathi, and for them typing long English prompts or reading English answers is a barrier. Because of this, a lot of people cannot fully use the benefits of AI for learning, writing and everyday communication.

## Our solution

BhashaMitra AI is a simple, open-source web assistant where the user picks a language (Hindi, Marathi or English), chooses what they want to do (chat, study, summarize, translate or improve text) and gets an AI answer in that language. The user can speak the question instead of typing it and can listen to the answer instead of reading it.

1. The user selects a language and a mode.
2. The user types a message or speaks it using the microphone.
3. The frontend sends the request to our FastAPI backend.
4. The backend calls the Sarvam AI API, which is built for Indian languages, and returns the answer.
5. The answer is shown on screen and can be read aloud with the browser's text-to-speech.

**Key idea:** one friendly interface that combines chat, study help, summarization, translation and text improvement for Indian languages, with voice in and voice out, built entirely with open-source tools.

## Key features

- 💬 **AI chat assistant:** ask questions and get AI-generated answers
- 🌍 **Multilingual support:** Hindi, Marathi and English
- 🎙️ **Voice input:** speak your message using browser speech recognition (where supported)
- 🔊 **Text-to-speech:** listen to AI answers using browser speech synthesis
- 📚 **Study mode:** get help understanding topics and learning concepts
- 📝 **Summarization:** turn long text into short, clear information
- 🔄 **Translation mode:** translate text between languages
- ✍️ **Text improvement:** improve the clarity and wording of your text
- 🎨 **User-friendly interface:** modern, responsive design that is easy to use
- 🔐 **Secure API key handling:** the Sarvam API key stays on the backend and is never exposed in the browser

## Who can use it and why

| User | Use |
|------|-----|
| School and college students | Understand topics, get explanations in Hindi or Marathi, and summarize notes |
| Hindi and Marathi speakers | Use AI comfortably in their own language, by voice or text |
| Teachers and educators | Simplify content, translate material and prepare short summaries |
| Writers, job seekers and professionals | Improve the wording and clarity of emails, applications and documents |
| Small business owners and shopkeepers | Translate and rewrite messages for customers in different languages |
| Elderly and low-typing-comfort users | Speak instead of typing and listen to answers instead of reading |
| Developers and open-source contributors | Reuse and extend a simple FastAPI + HTML/JS project that integrates the Sarvam AI API |

## Tech stack

**Frontend**

| Tool | Used for |
|------|----------|
| HTML, CSS, JavaScript | Web interface (homepage and AI assistant page) |
| Browser Speech Recognition API | Voice input |
| Browser Speech Synthesis API | Listening to AI answers |

**Backend**

| Tool | Used for |
|------|----------|
| Python | Backend language |
| FastAPI | REST API |
| Uvicorn | API server |

**AI integration**

| Tool | Used for |
|------|----------|
| Sarvam AI API | Language model for Indian languages (chat, study, summarize, translate, improve) |

**Platforms and tools**

| Platform / tool | Used for |
|------|----------|
| Vercel | Hosting the frontend |
| Render | Hosting the backend |
| GitHub | Source control and version history |
| Git | Version control |

## System architecture

```
 Browser (HTML + CSS + JavaScript)               Backend (FastAPI)
 +-----------------------------+   request    +---------------------------+
 | Home page (index.html)      | -----------> | main.py                   |
 | AI assistant (app.html)     |              |  - reads SARVAM_API_KEY   |
 | Language + mode selection   |              |  - builds the prompt      |
 | Voice input (Speech Recog.) | <----------- |  - returns AI answer      |
 | Voice output (Speech Synth.)|   response   +-------------+-------------+
 +-----------------------------+                            |
        hosted on Vercel                                    v
                                                  +-------------------+
                                                  |   Sarvam AI API   |
                                                  +-------------------+
                                                  backend hosted on Render
```

## Project structure

```
bhashamitra-ai/
├── backend/
│   ├── main.py             FastAPI application and Sarvam AI integration
│   ├── requirements.txt    Python dependencies
│   └── .env                API key (local only, never committed)
├── frontend/
│   ├── index.html          Homepage
│   └── app.html            AI assistant interface
├── .gitignore
└── README.md
```

## Prerequisites

| Tool | How to check |
|------|--------------|
| Git | `git --version` |
| Python 3 | `python --version` |
| A recent Chrome or Edge browser (voice input and output work best there) | |
| A Sarvam AI API key | Create an account at Sarvam AI and generate a key |

An internet connection is needed to install packages and to reach the Sarvam AI API.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/khushiiiiiiii153/bhashamitra-ai.git
cd bhashamitra-ai
```

### 2. Set up the backend

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure the API key

Create a file named `.env` inside the `backend` folder:

```
SARVAM_API_KEY=your_sarvam_api_key
```

Replace the placeholder with your own Sarvam AI API key.

> **Security:** never publish your API key on GitHub and never commit your `.env` file.

### 4. Run the backend

From the `backend` directory:

```bash
uvicorn main:app --reload
```

The backend runs at http://127.0.0.1:8000

### 5. Open the frontend

- Open `frontend/index.html` in your browser for the homepage.
- Open `frontend/app.html` for the AI assistant.

For local development, make sure the API URL configured in the frontend points to your running backend (`http://127.0.0.1:8000`).

## Environment variables

| Variable | Description |
|----------|-------------|
| `SARVAM_API_KEY` | API key used for the Sarvam AI integration |

For production, set this variable in the backend hosting provider's environment settings instead of using a `.env` file.

## Quick tour

1. Open the live demo and go to the AI assistant.
2. Choose **Hindi**, **Marathi** or **English**.
3. Type a question, or click the microphone and speak it.
4. Try the modes: Study, Summarization, Translation and Text Improvement.
5. Click the speaker button to listen to the answer.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| PowerShell blocks activating the virtual environment | Run PowerShell as the current user and allow scripts: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then activate again |
| `uvicorn is not recognized` | Activate the virtual environment first and run `pip install -r requirements.txt` |
| Answers are not coming / API error | Check that `SARVAM_API_KEY` is set correctly in `backend/.env` and that the backend is running |
| Frontend cannot reach the backend | Make sure the API URL in the frontend points to your running backend |
| First response on the hosted demo is slow | If the backend is on a free hosting tier it may be sleeping; wait a short while and try again |
| Voice input or voice output does not work | Use Chrome or Edge, allow microphone permission, and click the button once (browsers block automatic audio) |
| Port 8000 is already in use | Run `uvicorn main:app --reload --port 8001` and update the frontend API URL |

## Deployment

- **Backend:** Render web service. Set `SARVAM_API_KEY` in the Render environment settings.
- **Frontend:** Vercel, serving the `frontend` folder.
- **Source code:** GitHub. Pushing changes to the repository keeps the code in sync with the deployments.

## Project goal

To make AI-powered communication and learning easier for people who prefer Indian languages, especially Hindi and Marathi, alongside English, and to do it with a simple, open-source project that anyone can run, study and improve.

## Limitations and safety

- AI answers can sometimes be incorrect or incomplete. Please verify important information (medical, legal, financial) with a qualified person.
- Translations and summaries are AI-generated and may miss nuance, so review them before using them officially.
- The app depends on the Sarvam AI API; if the API is unavailable or the key limit is reached, responses will fail.
- Voice input and output depend on the browser; support and voice quality differ across browsers and devices, and Hindi or Marathi voices may need to be installed on the device.
- Chat history is not saved permanently yet.
- Currently supports three languages: Hindi, Marathi and English.

## Future improvements

- Persistent chat history and conversation management
- Improved voice conversations
- More Indian language options
- Document upload and summarization
- Better error handling and loading indicators
- Accessibility and mobile usability improvements

## Contributing

Contributions and suggestions are welcome. Fork the repository, create a branch, make your changes and submit a pull request.

## License

No license has been specified yet. Add a `LICENSE` file if you want to define the terms under which others may use, modify or distribute this project (for an open-source project, the MIT License is a common choice).

## Acknowledgements

- Sarvam AI for the language model API
- Open-source tools: FastAPI, Uvicorn, Python
- Browser Speech Recognition and Speech Synthesis APIs

Built with ❤️ by **Team Visionaries** for **HackFront India** (Problem Statement: **Open Source and Innovation**).