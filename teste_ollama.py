import requests

def consulta_ollama(prompt, model="phi3"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    print(response.json()['response'])
    return response.json()['response']

if __name__ == "__main__":
    consulta_ollama("Fale um fato curioso sobre inteligência artificial.")
