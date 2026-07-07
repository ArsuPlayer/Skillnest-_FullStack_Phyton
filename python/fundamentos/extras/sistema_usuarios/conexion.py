import pymysql

class Conexión:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "1234"
        self.db = "usuarios_db"
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db,
                cursorclass=pymysql.cursors.DictCursor
            )
            return self.conexion
        except pymysql.MySQLError as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def cerrar(self):
        if self.conexion:
            self.conexion.close()