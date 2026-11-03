from flask import Flask, render_template
from mascota import Mascota
from usuario import Usuario

app = Flask(__name__)

# ==========================================================
# RUTAS DE MASCOTAS
# ==========================================================

@app.route("/")
@app.route("/mascotas")
def listar_mascotas():
    """Muestra todas las mascotas."""
    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas)


@app.route("/mascotas/<int:mascota_id>")
def detalle_mascota(mascota_id):
    """Muestra el detalle de una mascota específica por ID."""
    mascota = Mascota.get_by_id(mascota_id)
    return render_template("mascota_detalle.html", mascota=mascota)


# ==========================================================
# RUTAS DE USUARIOS
# ==========================================================

@app.route("/usuarios")
def listar_usuarios():
    """Muestra todos los usuarios registrados."""
    usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=usuarios)


@app.route("/usuarios/<int:usuario_id>")
def detalle_usuario(usuario_id):
    """Muestra el detalle de un usuario por ID."""
    usuario = Usuario.get_by_id(usuario_id)
    return render_template("usuario_detalle.html", usuario=usuario)


if __name__ == "__main__":
    app.run(debug=True)