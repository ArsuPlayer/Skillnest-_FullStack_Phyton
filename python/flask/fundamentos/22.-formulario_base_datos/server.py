# ==========================================================
# SERVIDOR FLASK
# ==========================================================

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from mascota import Mascota

app = Flask(__name__)


# ==========================================================
# READ: MOSTRAR LISTADO PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    mascotas = Mascota.get_all()
    return render_template(
        "index.html",
        mascotas=mascotas
    )


# ==========================================================
# CREATE: CREAR NUEVA MASCOTA (POST)
# ==========================================================

@app.route("/crear_mascota", methods=["POST"])
def crear_mascota():
    datos = {
        "nombre": request.form["nombre"],
        "tipo": request.form["tipo"],
        "color": request.form["color"]
    }

    Mascota.save(datos)

    return redirect(url_for("index"))


# ==========================================================
# READ: VER DETALLE POR ID
# ==========================================================

@app.route("/mascota/<int:id>")
def mostrar_mascota(id):
    mascota = Mascota.get_by_id(id)

    if mascota is None:
        return "Mascota no encontrada", 404

    return render_template(
        "mascota.html",
        mascota=mascota
    )


# ==========================================================
# READ: BUSCAR POR NOMBRE
# ==========================================================

@app.route("/mascota/nombre/<string:nombre>")
def mostrar_mascota_por_nombre(nombre):
    mascota = Mascota.get_by_name(nombre)

    if mascota is None:
        return "Mascota no encontrada", 404

    return render_template(
        "mascota.html",
        mascota=mascota
    )


# ==========================================================
# READ: FILTRAR POR TIPO
# ==========================================================

@app.route("/mascotas/tipo/<string:tipo>")
def mostrar_por_tipo(tipo):
    mascotas_filtradas = Mascota.get_by_tipo(tipo)
    return render_template(
        "index.html",
        mascotas=mascotas_filtradas
    )


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)