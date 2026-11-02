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

from usuario import Usuario

app = Flask(__name__)


# ==========================================================
# READ: MOSTRAR LISTADO DE USUARIOS
# ==========================================================

@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template(
        "usuarios.html",
        usuarios=todos_los_usuarios
    )


# ==========================================================
# FORMULARIO DE CREACIÓN
# ==========================================================

@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("usuario_nuevo.html")


# ==========================================================
# CREATE: PROCESAR FORMULARIO Y GUARDAR EN MYSQL
# ==========================================================

@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    nombre = request.form["nombre"].strip()
    apellido = request.form["apellido"].strip()
    email = request.form["email"].strip()

    if not nombre or not apellido or not email:
        return render_template(
            "usuario_nuevo.html",
            error="Todos los campos son obligatorios."
        )

    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email
    }

    resultado = Usuario.save(data)

    if resultado is False:
        return render_template(
            "usuario_nuevo.html",
            error="No fue posible crear el usuario."
        )

    return redirect(url_for("usuarios"))


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)