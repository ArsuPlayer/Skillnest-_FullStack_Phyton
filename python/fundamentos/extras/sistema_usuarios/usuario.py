from conexion import Conexion

class Usuario:
    """
    Clase que representa a un Usuario y encapsula las operaciones CRUD y autenticación.
    """
    def __init__(self, id_usuario=None, usuario=None, password=None, tipo=None):
        self.id = id_usuario
        self.usuario = usuario
        self.password = password
        self.tipo = tipo

    def validar_inicio_sesion(self, nombre_usuario, password):
        """Valida las credenciales del usuario en la base de datos."""
        db = Conexion()
        conexion = db.abrir_conexion()
        if not conexion:
            return None

        try:
            with conexion.cursor() as cursor:
                query = """
                    SELECT u.id, u.usuario, u.password, t.nombre_tipo AS tipo
                    FROM usuarios u
                    JOIN tipos_usuario t ON u.tipo_usuario = t.id
                    WHERE u.usuario = %s AND u.password = %s;
                """
                cursor.execute(query, (nombre_usuario, password))
                resultado = cursor.fetchone()
                if resultado:
                    self.id = resultado['id']
                    self.usuario = resultado['usuario']
                    self.password = resultado['password']
                    self.tipo = resultado['tipo']
                    return self
                return None
        except Exception as e:
            print(f"Error en la validación: {e}")
            return None
        finally:
            db.cerrar_conexion()

    def crear_usuario(self, usuario, password, tipo_str):
        """Crea un nuevo usuario en la base de datos."""
        db = Conexion()
        conexion = db.abrir_conexion()
        if not conexion:
            return False

        try:
            tipo_id = 1 if tipo_str.upper() == 'ADMIN' else 2

            with conexion.cursor() as cursor:
                cursor.execute("SELECT id FROM usuarios WHERE usuario = %s", (usuario,))
                if cursor.fetchone():
                    print("Error: El nombre de usuario ya existe.")
                    return False

                query = """
                    INSERT INTO usuarios (usuario, password, tipo_usuario)
                    VALUES (%s, %s, %s);
                """
                cursor.execute(query, (usuario, password, tipo_id))
                return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False
        finally:
            db.cerrar_conexion()

    @staticmethod
    def obtener_listado():
        """Obtiene todos los registros de la tabla usuarios."""
        db = Conexion()
        conexion = db.abrir_conexion()
        if not conexion:
            return []

        try:
            with conexion.cursor() as cursor:
                query = """
                    SELECT u.id, u.usuario, t.nombre_tipo AS tipo
                    FROM usuarios u
                    JOIN tipos_usuario t ON u.tipo_usuario = t.id
                    ORDER BY u.id;
                """
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar usuarios: {e}")
            return []
        finally:
            db.cerrar_conexion()

    @staticmethod
    def buscar_por_id(id_usuario):
        """Busca un usuario por su ID."""
        db = Conexion()
        conexion = db.abrir_conexion()
        if not conexion:
            return None

        try:
            with conexion.cursor() as cursor:
                query = """
                    SELECT u.id, u.usuario, u.password, t.nombre_tipo AS tipo, u.created_at
                    FROM usuarios u
                    JOIN tipos_usuario t ON u.tipo_usuario = t.id
                    WHERE u.id = %s;
                """
                cursor.execute(query, (id_usuario,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Error al buscar usuario: {e}")
            return None
        finally:
            db.cerrar_conexion()

    def modificar_usuario(self, id_usuario, nuevo_usuario, nueva_password, nuevo_tipo_str):
        """Modifica los datos de un usuario existente."""
        db = Conexion()
        conexion = db.abrir_conexion()
        if not conexion:
            return False

        try:
            tipo_id = 1 if nuevo_tipo_str.upper() == 'ADMIN' else 2
            with conexion.cursor() as cursor:
                query = """
                    UPDATE usuarios
                    SET usuario = %s, password = %s, tipo_usuario = %s
                    WHERE id = %s;
                """
                cursor.execute(query, (nuevo_usuario, nueva_password, tipo_id, id_usuario))
                return True
        except Exception as e:
            print(f"Error al modificar usuario: {e}")
            return False
        finally:
            db.cerrar_conexion()

    @staticmethod
    def eliminar_usuario(id_usuario):
        """Elimina un usuario de la base de datos."""
        db = Conexion()
        conexion = db.abrir_conexion()
        if not conexion:
            return False

        try:
            with conexion.cursor() as cursor:
                query = "DELETE FROM usuarios WHERE id = %s;"
                cursor.execute(query, (id_usuario,))
                return True
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False
        finally:
            db.cerrar_conexion()