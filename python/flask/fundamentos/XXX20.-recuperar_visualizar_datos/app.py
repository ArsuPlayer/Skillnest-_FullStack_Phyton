# ==========================================================
# SERVIDOR FLASK
# ==========================================================

from flask import Flask, render_template
from mascota import Mascota


# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Consulta todas las mascotas y las envía
    hacia la plantilla index.html.
    """

    mascotas = Mascota.get_all()
    print(mascotas)

    return render_template(
        "index.html",
        todas_mascotas=mascotas
    )


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)