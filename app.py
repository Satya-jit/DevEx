from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "service": "devex-sample",
        "status": "ok"
    })

@app.get("/products")
def products():
    response = requests.get("https://dummyjson.com/products", timeout=10)
    response.raise_for_status()
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
