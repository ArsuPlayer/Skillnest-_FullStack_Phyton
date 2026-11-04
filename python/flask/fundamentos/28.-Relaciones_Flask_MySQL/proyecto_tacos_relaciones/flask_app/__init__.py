from flask import Flask

app = Flask(__name__)
app.secret_key = "secreto_tacos_app"