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

    # ------------------------------------------------------
    # OBTENER MASCOTAS DESDE MYSQL
    # ------------------------------------------------------

    mascotas = Mascota.get_all()


    # ------------------------------------------------------
    # MOSTRAR RESULTADOS EN TERMINAL
    # ------------------------------------------------------

    print(mascotas)


    # ------------------------------------------------------
    # ENVIAR DATOS A JINJA2
    # ------------------------------------------------------

    return render_template(

        "index.html",

        todas_mascotas=mascotas

    )
# ==========================================================
# RUTA: MASCOTAS DE TIPO PERRO
# ==========================================================

@app.route("/mascotas/perros")
def perros():
    """
    Obtiene únicamente las mascotas de tipo 'Perro'
    y las envía a la plantilla.
    """
    # Consultar al modelo solo los perros
    lista_perros = Mascota.get_by_tipo("Perro")

    # Renderizar index.html (o una plantilla dedicada) enviando los resultados
    return render_template(
        "index.html",
        todas_mascotas=lista_perros
    )

# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)
