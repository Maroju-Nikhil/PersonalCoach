import streamlit as st
import sqlite3
import uuid
import requests
from datetime import datetime
import time
import random
import os

# =========================================================
# CONFIGURATION
# =========================================================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:1b"
DB_PATH = "chat_history.db"

# =========================================================
# DATABASE
# =========================================================
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages (
                    id TEXT PRIMARY KEY,
                    sender TEXT,
                    message TEXT,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

def add_message(sender, message):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO messages VALUES (?, ?, ?, ?)",
              (str(uuid.uuid4()), sender, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_messages():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT sender, message, timestamp FROM messages ORDER BY timestamp ASC")
    data = c.fetchall()
    conn.close()
    return data

def clear_messages():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM messages")
    conn.commit()
    conn.close()

# =========================================================
# OLLAMA CALL
# =========================================================
def query_model(prompt, persona="Friendly"):
    try:
        system_prompt = {
            "Friendly": "You're a warm and engaging conversational partner.",
            "Serious": "You're calm, professional, and concise.",
            "Coach": "You're a fitness and life coach who motivates with clarity.",
            "Motivational": "You're inspiring, energetic, and focused on positivity."
        }[persona]

        payload = {
            "model": MODEL_NAME,
            "prompt": f"{system_prompt}\nUser: {prompt}\nAssistant:",
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "").strip()
        else:
            return f"⚠️ Error contacting model: {response.text}"
    except Exception as e:
        return f"⚠️ Model error: {e}"

# ---- PWA Setup ----
def serve_pwa_files():
    # Path to static files
    manifest_path = os.path.join("static", "manifest.json")
    service_worker_path = os.path.join("static", "service-worker.js")

    # Inject manifest + service worker
    if os.path.exists(manifest_path):
        st.markdown(
            f"""
            <link rel="manifest" href="/static/manifest.json">
            <meta name="theme-color" content="#000000">
            <script>
                if ("serviceWorker" in navigator) {{
                    window.addEventListener("load", function() {{
                        navigator.serviceWorker.register("/static/service-worker.js");
                    }});
                }}
            </script>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ manifest.json not found in static folder.")


serve_pwa_files()
# =========================================================
# STREAMLIT CONFIG
# =========================================================
st.set_page_config(page_title="🖤 Pocket Coach", layout="centered")
init_db()

# =========================================================
# STYLES
# =========================================================
st.markdown("""
<style>
body, .stApp {
    background-color: #000;
    color: #e0e0e0;
    font-family: 'Inter', sans-serif;
}

/* Message Bubbles */
.message {
    border-radius: 12px;
    padding: 10px 16px;
    margin-bottom: 12px;
    max-width: 80%;
    line-height: 1.6;
    word-wrap: break-word;
    box-shadow: 0 1px 4px rgba(255,255,255,0.05);
}

/* User message (dark gray bubble with subtle glow) */
.user {
    background: linear-gradient(145deg, #0f0f0f, #1a1a1a);
    color: #f0f0f0;
    margin-left: auto;
    border: 1px solid #222;
    box-shadow: 0 0 8px rgba(0, 128, 255, 0.1);
}

/* Bot message (slightly lighter gray) */
.bot {
    background: linear-gradient(145deg, #151515, #1e1e1e);
    color: #e6e6e6;
    border: 1px solid #222;
}

/* Timestamp */
.timestamp {
    font-size: 11px;
    color: #777;
    margin-top: 4px;
    text-align: right;
}

/* Input area styling */
textarea {
    background-color: #0f0f0f !important;
    color: white !important;
    border: 1px solid #333 !important;
}

/* Buttons */
button {
    border-radius: 6px !important;
}

/* Persona selector */
.persona {
    background-color: #111;
    padding: 8px;
    border-radius: 8px;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.title("⚙️ Settings")
    persona = st.radio("🧠 Persona", ["Friendly", "Serious", "Coach", "Motivational"], key="persona")
    if st.button("🧹 Clear Chat"):
        clear_messages()
        st.session_state["starter_displayed"] = False
        st.rerun()
    st.caption("💬 Pocket Coach (Minimal Black)")

# =========================================================
# MAIN CHAT
# =========================================================
st.title("🖤 Pocket Coach")

if "starter_displayed" not in st.session_state:
    st.session_state["starter_displayed"] = False

# Starter questions shown only for new chat
if not get_messages() and not st.session_state["starter_displayed"]:
    st.subheader("✨ Quick Start")
    starter_qs = [
        "How are you feeling today?",
        "What’s one thing on your mind?",
        "Do you want to plan your day?",
        "What do you want to improve this week?",
    ]
    cols = st.columns(2)
    for i, q in enumerate(starter_qs):
        if cols[i % 2].button(q, key=f"starter_{i}"):
            add_message("user", q)
            bot_reply = query_model(q, persona)
            add_message("bot", bot_reply)
            st.session_state["starter_displayed"] = True
            st.rerun()

messages = get_messages()

# Show messages neatly spaced
for i, (sender, message, timestamp) in enumerate(messages):
    msg_class = "user" if sender == "user" else "bot"
    with st.container():
        st.markdown(
            f"""
            <div class="message {msg_class}">
                {message}
                <div class="timestamp">{timestamp}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Input area
st.markdown("---")
user_input = st.text_area("💭 Type your message...", key="input_area")

col1, col2 = st.columns([5, 1])
with col2:
    if st.button("Send ➤"):
        if user_input.strip():
            add_message("user", user_input.strip())
            with st.spinner("Thinking..."):
                bot_reply = query_model(user_input.strip(), persona)
                add_message("bot", bot_reply)
            st.rerun()
