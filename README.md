# Code Summarizer

- [English Instructions](#running-the-project)
- [Документация на Русском](#запуск-проекта)

## Running the project

### Requirements

- `Python 3.11`

> Before starting, install `poetry`
>
> ```bash
> pip install poetry
> ```

### Install dependencies

Install poetry dependencies using the following command

```bash
poetry install
```

### (A) Running the Flask API

#### (1) Set API TOKEN for Llama model

- In the `./back` directory add a `.env` file with the following fields

  ```bash
  API_TOKEN="api token from hugging face"
  API_URL="https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct"
  ```

- You can get a free hugging face access token from here [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

- Run the API using

  ```bash
  poetry run flask run
  ```

- or

  ```bash
  python app/py
  ```

#### (2) Running the API with a local model

- To run the API and model locally, download the llama 3.2 model files from [https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)
- Make sure you have transformers and pytorch installed:

  ```bash
  poetry add transformers torch flask
  ```

- To run the model locally make the following change to the model init function

  ```bash
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

  ```bash
  poetry run flask run
  ```

### (B) Running the streamlite app

- In the `./front` directory add a `.env` with the following fields

  ```bash
  API_ENDPOINT=http://localhost:5000 # or the flask API url
  ```

- Run streamlit app

  ```bash
  streamlit run main.py
  ```

## Запуск проекта

## Требования

- `Python 3.11`

> Перед началом работы установите `poetry`
>
> ```bash
> pip install poetry
> ```

### Установить зависимости

Установите зависимости poetry с помощью следующей команды

```bash
poetry install
```

### (А) Запуск API Flask

#### (1) Запуск API с использованием модели Llama от hugging face

- В каталог `./back` добавьте файл `.env` со следующими полями

  ```bash
  API_TOKEN="ваш api-токен от hugging face"
  API_URL="https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct"
  ```

- Вы можете получить бесплатный токен доступа к hugging face здесь [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

- Запустите API с помощью

  ```bash
  poetry run flask run
  ```

- или

  ```bash
  python app/py
  ```

#### (2) Запуск API с локальной моделью

- Чтобы запустить API и модель локально, загрузите файлы модели llama 3.2 с веб-сайта [https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)
- Убедитесь, что у вас установлены трансформаторы и pytorch:

  ```bash
  poetry add transformers torch flask
  ```

- Чтобы запустить модель локально, внесите следующие изменения в функцию инициализации модели

  ```bash
  MODEL_NAME = "your_model_name_here"  # Заменить на название модели с Hugging Face, например, "facebook/llama-7b".
  tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
  model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

  def query_huggingface(payload):
      inputs = tokenizer(payload["inputs"], return_tensors="pt")
      outputs = model.generate(**inputs, max_length=700)
      result = tokenizer.decode(outputs[0], skip_special_tokens=True)
      return {"generated_text": result}
  ```

- Запустите приложение flask

  ```bash
  poetry run flask run
  ```

### (B) Запуск приложения streamlit

- В каталоге `./front` добавьте файл `.env` со следующими полями

  ```bash
  API_ENDPOINT=http://localhost:5000 # или URL-адрес flask API
  ```

- Запустите приложение streamlit

  ```bash
  streamlit run main.py
  ```
