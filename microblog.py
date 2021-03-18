from flask import Flask

app = Flask("Microblog")

#aqui vai comentário
@app.route("/")
def index():
    return "Olá Mundo"

app.run()