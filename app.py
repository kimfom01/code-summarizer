import requests
import os
from flask import Flask, request, render_template

app = Flask(__name__)

# Your Hugging Face API key
API_TOKEN = os.getenv('MY_SECRET_TOKEN')
API_URL = "https://api-inference.huggingface.co/models/Salesforce/codegen-350M-mono"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query_huggingface(payload):
    """Send a request to Hugging Face API and get the response."""
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate_summary(code):
    # First prompt: Generate a summary and purpose in less than 100 words
    prompt_summary = f"In less than 100 words, generate a summary and purpose of this code: {code}"
    payload_summary = {"inputs": prompt_summary}
    
    # Query the Hugging Face API for the summary
    response_summary = query_huggingface(payload_summary)
    
    if "error" in response_summary:
        return "Error generating summary. Please try again."
    
    summary = response_summary[0]["generated_text"].strip()

    # Second prompt: Document the purpose of each function or method in less than 700 words
    prompt_detailed = f"In less than 700 words, describe and document the purpose of each function or method in this code: {code}"
    payload_detailed = {"inputs": prompt_detailed}
    
    # Query the Hugging Face API for the detailed function descriptions
    response_detailed = query_huggingface(payload_detailed)
    
    if "error" in response_detailed:
        return "Error generating function details. Please try again."
    
    detailed_description = response_detailed[0]["generated_text"].strip()
    
    # Combine the summary and detailed function description
    full_description = f"Summary: {summary}\n\nDetailed Description:\n{detailed_description}"
    
    return full_description

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ensure 'code' is in the form data
        if 'code' not in request.form:
            return "Error: 'code' field is missing in the form data."

        code = request.form['code']  # Get the code input
        full_description = generate_summary(code)  # Generate the summary and details
        return render_template('result.html', full_description=full_description)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
