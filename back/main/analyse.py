import os
import requests
from flask import Blueprint, request, jsonify

# from transformers import AutoTokenizer, AutoModelForCausalLM

analyse = Blueprint("analyse", __name__)

API_TOKEN = os.getenv("API_TOKEN")
API_URL = os.getenv("API_URL")

# For local run

#  MODEL_NAME = "path to local model"  # Replace with path to local model"
#  tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
#  model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# def query_huggingface(payload):
#     inputs = tokenizer(payload["inputs"], return_tensors="pt")
#     outputs = model.generate(**inputs, max_length=700)
#     result = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return {"generated_text": result}


headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query_huggingface(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def init_prompt(code, language="python", summary_size=100, description_size=700):

    sum_prompt = {
        "inputs": f"in {summary_size} words what does this code do?:{code}\nOverall Description:"
    }
    summary = query_huggingface(sum_prompt)

    if "Overall Description:" in summary[0]["generated_text"].strip():
        summary = (
            summary[0]["generated_text"].split("Overall Description:", 1)[-1].strip()
        )

    desc_prompt = {
        "inputs": f"document the functions in the following code:{code}\nDocumentation:"
    }

    description = query_huggingface(desc_prompt)
    if "Documentation:" in description[0]["generated_text"].strip():
        description = (
            description[0]["generated_text"].split("Documentation:", 1)[-1].strip()
        )

    full_description = jsonify({"summary": summary}, {"description": description})
    return full_description


@analyse.route("/analyse", methods=["POST"])
def analyse_code():
    try:
        data = request.json
        code_snippet = data.get("code")

        if not code_snippet:
            return jsonify({"error": "No code snippet provided"}), 400
        analysis_result = init_prompt(code_snippet)
        return analysis_result, 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
