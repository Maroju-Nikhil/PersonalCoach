🧠 Pocket Coach

Your Personal AI Coach — Powered by Local LLMs & Streamlit

Pocket Coach is a lightweight Progressive Web App (PWA) built with Streamlit that integrates with Ollama to run local large language models (LLMs) such as Gemma, LLaMA, or Mistral.
It’s designed to act as your on-device AI companion — accessible on both desktop and mobile (as a standalone PWA).

🚀 Features

💬 Conversational AI: Interact with locally running LLMs for guidance or coaching.

⚡ Local Inference: Runs through Ollama — no cloud dependency for model execution.

📱 PWA Support: Add it to your mobile home screen and use it like a native app.

🧩 Minimalist UI: Built with Streamlit’s modern components and styled for dark/black themes.

🧠 Modular Design: Clean structure with separate files for frontend, backend, and manifest.

📁 Project Structure
File / Folder	Purpose
app.py	Main entry point for Streamlit. Handles UI rendering, chat logic, and model integration.
static/	Contains static assets like icons, manifest file, and styles.
├── manifest.json	Defines PWA behavior (name, theme, icon, standalone mode, etc.).
├── app-icon.png	PWA icon used when installed on mobile or desktop.
requirements.txt	Python dependencies for deployment (Streamlit, requests, etc.).
README.md	Documentation file (this one).
🧩 How It Works

Frontend (Streamlit)

Renders the chat interface, message history, and PWA-related assets.

Uses dark/black theme styling for a clean, mobile-friendly interface.

Backend (Ollama)

The app sends requests to the Ollama API (running locally on port 11434).

Ollama handles inference for models like gemma, llama3, or mistral.

Deployment

On local systems, Ollama must be running with the selected model pre-loaded.

When deployed to Streamlit Cloud, the model API won’t connect (as Ollama cannot run remotely).

PWA Integration

The manifest.json and service worker (served through Streamlit) enable installable PWA functionality.

Once installed, you can use it offline for UI, though AI inference still requires a running Ollama backend.

⚙️ Setup & Local Run

Install Ollama on your machine.

Pull your desired model, e.g.

ollama pull gemma


Run Ollama locally:

ollama serve


Start the Streamlit app:

streamlit run app.py


Open in your browser at http://localhost:8501 and use it like an AI coach.

☁️ Deployment Notes

Streamlit Cloud / Hugging Face Spaces currently cannot host local models (Ollama).

You can deploy the UI to Streamlit Cloud but need a hosted inference backend if you want the model to respond.

Alternatives include:

Hosting Ollama on a VPS or local server and exposing the endpoint via ngrok or Cloudflare Tunnel.

Switching to a cloud LLM API (OpenAI, Groq, Anthropic) for remote deployment.

📱 Using as a PWA

Open the app in your mobile browser.

Tap “Add to Home Screen” or “Install App”.

It will appear as a standalone application with your custom theme and icon.

🧾 Notes

You can customize model names, themes, or chat prompts easily in app.py.

The PWA manifest is fully configurable for brand name, colors, and icons.

For true on-device inference, the app depends on Ollama’s local runtime.

🧰 Tech Stack

Frontend: Streamlit

Backend: Ollama (Local LLM Engine)

PWA Support: manifest.json + static asset serving

Language: Python 3.10+