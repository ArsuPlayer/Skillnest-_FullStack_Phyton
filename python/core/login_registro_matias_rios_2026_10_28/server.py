from flask import Flask

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

from controllers.usuarios import *

if __name__ == "__main__":
    app.run(debug=True)