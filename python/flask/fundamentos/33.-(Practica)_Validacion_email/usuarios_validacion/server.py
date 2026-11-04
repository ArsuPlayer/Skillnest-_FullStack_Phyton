from flask_app import app

# Importar controladores para registrar las rutas
from flask_app.controllers import usuario


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )