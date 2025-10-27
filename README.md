# 🧠 Pocket Coach  
**Your Personal AI Coach — Powered by Local LLMs & Streamlit**

Pocket Coach is a lightweight Progressive Web App (PWA) built with **Streamlit** that integrates with **Ollama** to run local large language models (LLMs) such as **Gemma**, **LLaMA**, or **Mistral**.  
It’s designed to act as your on-device AI companion — accessible on both desktop and mobile (as a standalone PWA).

---

## 🚀 Features

- 💬 Conversational AI — Interact with locally running LLMs for guidance or coaching.  
- ⚡ Local Inference — Runs through Ollama, no cloud dependency for model execution.  
- 📱 PWA Support — Add it to your mobile home screen and use it like a native app.  
- 🧩 Minimalist UI — Built with Streamlit’s modern components and styled for dark/black themes.  
- 🧠 Modular Design — Clean structure with separate files for frontend, backend, and manifest.  

---

## 📁 Project Structure

| File / Folder | Purpose |
|----------------|----------|
| `app.py` | Main entry point for Streamlit. Handles UI rendering, chat logic, and model integration. |
| `static/` | Contains static assets like icons, manifest file, and styles. |
| ├── `manifest.json` | Defines PWA behavior (name, theme, icon, standalone mode, etc.). |
| ├── `app-icon.png` | PWA icon used when installed on mobile or desktop. |
| `requirements.txt` | Python dependencies for deployment (Streamlit, requests, etc.). |
| `README.md` | Documentation file (this one). |

---

## 🧩 How It Works

1. **Frontend (Streamlit)**  
   - Renders the chat interface, message history, and PWA-related assets.  
   - Uses dark/black theme styling for a clean, mobile-friendly interface.  

2. **Backend (Ollama)**  
   - The app sends requests to the Ollama API (running locally on port `11434`).  
   - Ollama handles inference for models like `gemma`, `llama3`, or `mistral`.  

3. **Deployment**  
   - On local systems, Ollama must be running with the selected model pre-loaded.  
   - When deployed to Streamlit Cloud, the model API won’t connect (as Ollama cannot run remotely).  

4. **PWA Integration**  
   - The `manifest.json` and service worker (served through Streamlit) enable installable PWA functionality.  
   - Once installed, you can use it offline for UI, though AI inference still requires a running Ollama backend.  

---

## 🔁 System Flow (Architecture Overview)

User ↔ Streamlit UI ↔ Ollama API ↔ Local LLM Model
│
└── Static Files (manifest.json, icons)


---

## ⚙️ Setup & Local Run

1. **Install Ollama** on your machine:  
   https://ollama.ai/download  

2. **Pull your desired model:**  
    >> ollama pull gemma

3. Run Ollama locally:
    >> ollama serve

4. Start the Streamlit app:
    >> streamlit run app.py


Open in your browser:
http://localhost:8501


# ☁️ Deployment & Usage Guide — Pocket Coach

## ☁️ Deployment Notes

- **Streamlit Cloud** or **Hugging Face Spaces** currently **cannot host Ollama models**.  
- You can deploy only the **UI (Streamlit app)** to these platforms —  
  but it will need a **hosted inference backend** if you want responses from the model.

### 🔄 Alternatives

1. **Host Ollama on a VPS or Local Server**
   - Run Ollama on your own machine or cloud VM.
   - Expose the endpoint securely using:
     - [ngrok](https://ngrok.com)
     - or [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)
   - Update your app’s `OLLAMA_API_URL` to point to that endpoint.

2. **Use a Cloud LLM API**
   - Replace Ollama with a hosted API:
     - [OpenAI](https://platform.openai.com)
     - [Groq](https://groq.com)
     - [Anthropic Claude](https://www.anthropic.com)
   - This ensures your app works fully online on Streamlit Cloud.

---

## 📱 Using as a PWA

1. Open the app in your **mobile browser** (e.g., Chrome, Safari).  
2. Tap **“Add to Home Screen”** or **“Install App.”**  
3. Once installed, it appears as a **standalone mobile app** with:
   - Custom icon  
   - Theme color  
   - Fullscreen experience (no browser UI)

✅ The PWA setup is powered by `manifest.json` and static assets included in the `/static` folder.

---

## 🧾 Notes

- You can **customize model names**, **themes**, and **chat prompts** directly in `app.py`.  
- The **PWA manifest** is fully configurable:
  - Change app name, short name, and theme colors.
  - Replace the app icon for branding.
- For **true on-device inference**, Pocket Coach depends on **Ollama’s local runtime**.  

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **Backend** | Ollama (Local LLM Engine) |
| **PWA Support** | manifest.json + static asset serving |
| **Language** | Python 3.10+ |

---

## 🧭 Future Improvements

- 🗂️ Add **persistent chat history** across sessions.  
- 🎙️ Integrate **voice input/output** for a conversational feel.  
- ☁️ Provide **remote model fallback** when Ollama is unavailable.  

---

## ⚠️ Limitations

- ⚙️ **Ollama must be running locally** to generate responses.  
- ☁️ **Streamlit Cloud deployment** runs only the UI — no local model execution.  
- 📴 **Offline usage** supports the interface,  
  but AI generation still requires an **active connection to Ollama**.  

---

## 👨‍💻 Author

**Pocket Coach** was built to bring the power of local LLMs to your pocket —  
simple, sleek, and private.  

Contributions and improvements are always welcome! 🚀

---


## Deployed link (Although this will not work since model will not get deployed there in streamlit): 
https://personal-coach-of-nikhil.streamlit.app/

