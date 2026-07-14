from flask import Flask
app = Flask(__name__)

# Ruta raíz - Página de inicio
@app.route("/")
def hola_mundo()
    retur
# Ruta genérica para explorar enrutamiento

# Rutas dinámicas para personalización

# Ruta que repite un mensaje varias veces

# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente

# Ejecuta el servidor
if __name__ == "__main__":
    app.run(debug=True)