import pymysql.cursors

class MySQLConnection:
    """
    Administra la conexión con MySQL centralizando las ejecuciones de SQL.
    """
    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",  # Reemplazar con tu contraseña local de MySQL
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """
        Ejecuta consultas parametrizadas.
        - SELECT: Devuelve lista de diccionarios.
        - INSERT: Devuelve el ID numérico insertado.
        - UPDATE/DELETE: Devuelve None.
        - Error: Devuelve False.
        """
        with self.connection.cursor() as cursor:
            try:
                print("\n[Executing Query]:", query)
                if data:
                    print("[Data Passed]:", data)

                cursor.execute(query, data)

                query_type = query.strip().lower()

                if query_type.startswith("select"):
                    return cursor.fetchall()
                elif query_type.startswith("insert"):
                    return cursor.lastrowid
                else:
                    return None
            except Exception as e:
                print("[MySQL Error]:", e)
                return False
            finally:
                self.connection.close()


def connectToMySQL(db):
    """Retorna una instancia activa de la conexión a la base de datos especificada."""
    return MySQLConnection(db)