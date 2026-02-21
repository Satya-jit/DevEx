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
    try:
        response = requests.get("https://dummyjson.com/products", timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104
