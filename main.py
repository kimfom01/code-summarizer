import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Your Hugging Face API key
API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query_huggingface(payload):
    """Send a request to Hugging Face API and get the response."""
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate_summary(code):
    prompt = f"Summarize this Python code in one sentence: {code}"
    payload = {"inputs": prompt}
    
    # Send the code to Hugging Face API and get the summary
    response = query_huggingface(payload)
    
    if "error" in response:
        return "Error generating summary. Please try again."
    
    # Extract the generated text from the response
    summary = response[0]["generated_text"].strip()
    return summary

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']  # Get the code input from the form
        summary = generate_summary(code)  # Generate the summary using Hugging Face API
        return render_template('result.html', summary=summary)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
