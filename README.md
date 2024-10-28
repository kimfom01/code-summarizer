# code-summarizer
## Running the project

## (A) Running the flask api
#### (1) Running the API using the Llama model from hugging face

- Before running the API install 
```
python = "^3.11"
flask = "^3.0.3"
python-dotenv = "^1.0.1"
poetry
```

- In the ``/back/code_summarizer_api`` directory add a ``.env`` file with the following fields
```
API_TOKEN="your hugging face api token"
API_URL="https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct"
```
- You can get a free hugging face access token from here ``https://huggingface.co/settings/tokens``
- In the ``/back/code_summarizer_api`` directory install the required dependencies using 
```
poetry install
```
- Run the APi using 
```
poetry run flask run 
```
- or
```
python app/py
```
#### (2) Running the APi with a local model
- To run the Api and model locally, download the llama 3.2 model files from ``https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct``
- Make sure you have transformers and pytorch installed:

```bash
pip install transformers torch flask
```
- To run the model locally make the following change to the model init function

```
MODEL_NAME = "your_model_name_here"  # Replace with the Hugging Face model name, e.g., "facebook/llama-7b"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

def query_huggingface(payload):
    inputs = tokenizer(payload["inputs"], return_tensors="pt")
    outputs = model.generate(**inputs, max_length=700)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"generated_text": result}
```
- Run the flask app 
```
poetry run flask run 
```

## (B) Running the streamlite app

- Before running the streamlite app make sure you have the following installed
```
python = "^3.10"
```
- In the ``/front`` directory add a ``.env`` with the following fields
```
API_ENDPOINT=http://localhost:5000 # or the flask API url
```
- Install required dependencies 
```
pip install -r requirements.txt
```
- Run streamlite app
```
streamlit run .\main.py
```