from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "clave_secreta_destino"

PREDICCIONES = [
    {"tipo": "buena", "icono": "⭐", "mensaje": "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría."},
    {"tipo": "buena", "icono": "🚀", "mensaje": "Un éxito profesional inesperado llegará pronto. Prepárate para grandes cambios."},
    {"tipo": "mala", "icono": "⚠️", "mensaje": "Cuidado con los gastos impulsivos esta semana, las estrellas prevén turbulencias financieras."},
    {"tipo": "mala", "icono": "🌧️", "mensaje": "Alguien del pasado intentará volver a tu vida para probar tu paciencia. Mantén la calma."}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    session["nombre"] = request.form.get("nombre")
    session["edad"] = request.form.get("edad")
    session["color"] = request.form.get("color")
    session["animal"] = request.form.get("animal")
    
    # Generar predicción aleatoria y número de la suerte
    session["prediccion"] = random.choice(PREDICCIONES)
    session["numero_suerte"] = random.randint(1, 99)
    
    return redirect(url_for("futuro"))

@app.route("/futuro")
def futuro():
    if "prediccion" not in session:
        return redirect(url_for("index"))

    return render_template(
        "futuro.html",
        nombre=session.get("nombre"),
        edad=session.get("edad"),
        color=session.get("color"),
        animal=session.get("animal"),
        prediccion=session.get("prediccion"),
        numero_suerte=session.get("numero_suerte")
    )

if __name__ == "__main__":
    app.run(debug=True)