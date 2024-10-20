from flask import Flask, request, jsonify
from main.analyse import analyse

app = Flask(__name__)

app.register_blueprint(analyse)

if __name__ == "__main__":
    app.run(debug=True)
