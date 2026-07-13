from flask import Flask

app = Flask(__name__)

@app.route("/nosotros")
def nosotros():
    return "¡Conócenos un poco más!"

#productos
@app.route("/eli")
def eli():
    return "¡Gracias por el proyecto!"

#contactos
@app.route("/isi")
def isi():
    return "¡ola!"


if __name__ == "__main__":
    app.run(debug=True)