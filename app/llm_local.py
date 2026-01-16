import subprocess

def ask_llm(context, question):
    prompt = f"""
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()
