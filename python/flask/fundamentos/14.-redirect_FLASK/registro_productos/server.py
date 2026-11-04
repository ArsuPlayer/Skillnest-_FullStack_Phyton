# ==========================================
# IMPORTACIONES
# ==========================================

from flask import Flask, render_template, request, redirect, url_for


# ==========================================
# CREACIÓN DE LA APLICACIÓN
# ==========================================

app = Flask(__name__)


# ==========================================
# RUTA PRINCIPAL (Formulario)
# ==========================================

@app.route("/")
def index():
    """
    Muestra el formulario de registro de productos.
    """
    return render_template("index.html")


# ==========================================
# PROCESAR FORMULARIO (POST)
# ==========================================

@app.route("/registrar", methods=["POST"])
def registrar():
    """
    Recibe los datos del producto mediante POST,
    los muestra en la terminal y redirige.
    """
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    print("==============================")
    print("Producto recibido")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Categoría: {categoria}")
    print("==============================")

    # Redirección utilizando url_for hacia la ruta GET de resultado
    return redirect(url_for("resultado"))


# ==========================================
# MOSTRAR RESULTADO (GET)
# ==========================================

@app.route("/resultado")
def resultado():
    """
    Muestra la página de confirmación después de la redirección.
    """
    return render_template("resultado.html")


# ==========================================
# RUTA DE AYUDA (Desafío adicional)
# ==========================================

@app.route("/ayuda")
def ayuda():
    """
    Explica los conceptos clave de la lección.
    """
    return render_template("ayuda.html")


# ==========================================
# EJECUTAR SERVIDOR
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)