from flask import Flask, jsonify

app = Flask(__name__)

# Banco de dados fake
produtos = [
    {"id": 1, "nome": "Camiseta", "preco": 49.90},
    {"id": 2, "nome": "Tênis", "preco": 199.90},
    {"id": 3, "nome": "Boné", "preco": 39.90}
]

@app.route("/")
def home():
    return "<h1>Loja Genérica do JOTAGE 🛒🔥</h1>"

@app.route("/produtos")
def listar_produtos():
    return jsonify(produtos)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
