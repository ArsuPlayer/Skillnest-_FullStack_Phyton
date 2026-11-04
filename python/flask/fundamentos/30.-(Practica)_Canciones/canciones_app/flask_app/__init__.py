from flask import Flask

app = Flask(__name__)

# Clave secreta necesaria para utilizar mensajes flash.
app.secret_key = "clave-secreta-desarrollo"