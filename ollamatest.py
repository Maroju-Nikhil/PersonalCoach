import requests, json
URL = "http://localhost:11434/api/generate"   # match OLLAMA_URL in the app
MODEL = "gemma3:1b"                           # or phi4-mini:latest
r = requests.post(URL, json={"model": MODEL, "messages": [{"role":"user","content":"Hello"}], "stream": True}, stream=True, timeout=30)
print("STATUS", r.status_code)
for i, line in enumerate(r.iter_lines()):
    if line:
        print(i, line.decode('utf-8'))
    if i > 20:
        break
