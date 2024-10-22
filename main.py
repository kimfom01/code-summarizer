import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Your Hugging Face API key
API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/codeparrot/codeparrot-small-v2"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query_huggingface(payload):
    """Send a request to Hugging Face API and get the response."""
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
def generate_summary(code, language):
    # Customize the prompt based on the selected language
    if language == "python":
        prompt = f"Summarize this Python code in one sentence: {code}"
    elif language == "java":
        prompt = f"Summarize this Java code in one sentence: {code}"
    elif language == "javascript":
        prompt = f"Summarize this JavaScript code in one sentence: {code}"
    elif language == "cpp":
        prompt = f"Summarize this C++ code in one sentence: {code}"
    else:
        prompt = f"Summarize this code in one sentence: {code}"
    
    payload = {"inputs": prompt}
    
    response = query_huggingface(payload)
    
    if "error" in response:
        return "Error generating summary. Please try again."
    
    summary = response[0]["generated_text"].strip()
    return summary


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        language = request.form['language']  # Get the selected language
        code = request.form['code']  # Get the code input
        summary = generate_summary(code, language)  # Generate the summary using the selected language
        return render_template('result.html', summary=summary)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
