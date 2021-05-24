import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Meu nome é Lucas da Silva Santos, estudante da faculdade Impacta"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
