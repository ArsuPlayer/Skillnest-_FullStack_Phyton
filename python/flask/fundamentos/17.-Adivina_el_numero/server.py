# ==========================================================
# ADIVINA EL NÚMERO
# Juego desarrollado con Flask
# ==========================================================

# ----------------------------------------------------------
# IMPORTACIONES
# ----------------------------------------------------------
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)
import random

# ----------------------------------------------------------
# CREAR APLICACIÓN
# ----------------------------------------------------------
app = Flask(__name__)

# ----------------------------------------------------------
# SECRET KEY
# ----------------------------------------------------------
app.secret_key = "clave-secreta-adivina-numero"

# ----------------------------------------------------------
# RUTA PRINCIPAL
# ----------------------------------------------------------
@app.route("/")
def index():
    """
    Muestra la página principal del juego.
    """

    # INICIALIZAR NÚMERO SECRETO
    if "numero_secreto" not in session:
        session["numero_secreto"] = random.randint(1, 10)

    # INICIALIZAR INTENTOS
    if "intentos" not in session:
        session["intentos"] = 0

    # INICIALIZAR LÍMITE DE INTENTOS (MODIFICACIÓN)
    if "max_intentos" not in session:
        session["max_intentos"] = 5

    # INICIALIZAR MENSAJE
    if "mensaje" not in session:
        session["mensaje"] = "Adivina un número entre 1 y 10."

    # INICIALIZAR ESTADO DEL JUEGO
    if "resultado" not in session:
        session["resultado"] = ""

    # ENVIAR INFORMACIÓN A LA PLANTILLA
    mensaje = session["mensaje"]
    resultado = session["resultado"]
    intentos = session["intentos"]
    max_intentos = session["max_intentos"]

    return render_template(
        "index.html",
        mensaje=mensaje,
        resultado=resultado,
        intentos=intentos,
        max_intentos=max_intentos
    )

# ----------------------------------------------------------
# PROCESAR INTENTO
# ----------------------------------------------------------
@app.route("/adivinar", methods=["POST"])
def adivinar():
    """
    Procesa el número ingresado por el usuario
    y lo compara con el número secreto.
    """

    # RECIBIR DATO DEL FORMULARIO
    numero = int(request.form["numero"])

    # OBTENER NÚMERO SECRETO Y LÍMITE
    numero_secreto = session["numero_secreto"]

    # AUMENTAR INTENTOS
    session["intentos"] += 1

    # COMPARAR NÚMEROS (MODIFICADO CON VALIDACIÓN DE DERROTA)
    if numero == numero_secreto:
        session["mensaje"] = f"¡Correcto! El número secreto era {numero_secreto}."
        session["resultado"] = "correcto"

    elif session["intentos"] >= session["max_intentos"]:
        session["mensaje"] = f"¡Agotaste tus {session['max_intentos']} intentos! El número era {numero_secreto}."
        session["resultado"] = "derrota"

    elif numero < numero_secreto:
        session["mensaje"] = f"El número secreto es mayor que {numero}."
        session["resultado"] = "mayor"

    else:
        session["mensaje"] = f"El número secreto es menor que {numero}."
        session["resultado"] = "menor"

    # VOLVER A LA PÁGINA PRINCIPAL
    return redirect(url_for("index"))

# ----------------------------------------------------------
# REINICIAR JUEGO
# ----------------------------------------------------------
@app.route("/reiniciar")
def reiniciar():
    """
    Elimina la información actual de la sesión
    y redirige al inicio.
    """
    session.clear()
    return redirect(url_for("index"))

# ----------------------------------------------------------
# EJECUTAR SERVIDOR
# ----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)