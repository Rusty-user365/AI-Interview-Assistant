import subprocess, json

def run_ollama(prompt, model="gemma3:270m"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()
