import requests


def local_ai(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.2", "prompt": prompt, "stream": False},
    )

    data = response.json()

    if "response" in data:
        return data["response"]

    return f"Ollama Error: {data}"


timeout = 30.0
