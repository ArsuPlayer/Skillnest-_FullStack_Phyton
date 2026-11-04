import pymysql.cursors

class Conexion:
    """
    Clase responsable de gestionar la conexión con la base de datos MySQL.
    """
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "1234"  # Actualiza con tu contraseña de MySQL
        self.database = "usuarios_db"
        self.connection = None

    def abrir_conexion(self):
        """Abre y retorna la conexión a MySQL."""
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True
            )
            return self.connection
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None

    def cerrar_conexion(self):
        """Cierra la conexión si está abierta."""
        if self.connection:
            try:
                self.connection.close()
            except Exception as e:
                print(f"Error al cerrar la conexión: {e}")