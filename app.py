from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Camiseta", "preco": 49.90},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos", methods=["POST"])
def adicionar_produto():
    novo = request.json
    novo["id"] = len(produtos) + 1
    produtos.append(novo)
    return jsonify(novo)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
