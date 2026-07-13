from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "¡Hola Mundo!"

@app.route("/exito")
def exito():
    return "¡Éxito!"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return "¡hola {nombre}!"

@app.route("/color/<nombre>/<color>")
def color_favorito(nombre, color):
    return "¡hola {nombre}, tu color favorito es {color}!"

@app.route("/saludo/<nombre>/int:veces")
def repetir(nombre, veces):
    return "¡hola {nombre}!" * veces


## 🚀 Desafíos adicionales

@app.route("/bye/<nombre>")
def bye(nombre, veces):
    return "¡Hasta luego {nombre}!" 

@app.route("/bye/<nombre>")
def bye(nombre, veces):
    return "¡Hasta luego {nombre}!" 


if __name__ == "__main__":
    app.run(debug=True) 