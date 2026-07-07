from conexion import Conexión

class Usuario:
    def __init__(self, id_usuario=None, nombre_usuario=None, contrasena=None, tipo_usuario=None):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.tipo_usuario = tipo_usuario  # Almacenará el ID numérico (1 para ADMIN, 2 para USER)

    @staticmethod
    def iniciar_sesion(username, password):
        """Verifica las credenciales y devuelve un diccionario con los datos o None."""
        db = Conexión()
        conn = db.conectar()
        if not conn:
            return None
        
        try:
            with conn.cursor() as cursor:
                sql = """
                    SELECT u.id_usuario, u.nombre_usuario, u.contrasena, t.nombre_tipo 
                    FROM usuarios u
                    INNER JOIN tipo_usuarios t ON u.tipo_usuario = t.id_tipo_usuario
                    WHERE u.nombre_usuario = %s AND u.contrasena = %s AND u.deleted = 0
                """
                cursor.execute(sql, (username, password))
                resultado = cursor.fetchone()
                return resultado
        except Exception as e:
            print(f"Error en inicio de sesión: {e}")
            return None
        finally:
            db.cerrar()

    def registrar_usuario(self):
        db = Conexión()
        conn = db.conectar()
        if not conn: return False
        
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO usuarios (nombre_usuario, contrasena, tipo_usuario) VALUES (%s, %s, %s)"
                cursor.execute(sql, (self.nombre_usuario, self.contrasena, self.tipo_usuario))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return False
        finally:
            db.cerrar()

    @staticmethod
    def listar_usuarios():
        db = Conexión()
        conn = db.conectar()
        if not conn: return []
        
        try:
            with conn.cursor() as cursor:
                sql = """
                    SELECT u.id_usuario, u.nombre_usuario, t.nombre_tipo 
                    FROM usuarios u
                    INNER JOIN tipo_usuarios t ON u.tipo_usuario = t.id_tipo_usuario
                    WHERE u.deleted = 0
                """
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar usuarios: {e}")
            return []
        finally:
            db.cerrar()

    @staticmethod
    def buscar_usuario_por_id(id_buscar):
        db = Conexión()
        conn = db.conectar()
        if not conn: return None
        
        try:
            with conn.cursor() as cursor:
                sql = """
                    SELECT u.id_usuario, u.nombre_usuario, u.contrasena, t.nombre_tipo 
                    FROM usuarios u
                    INNER JOIN tipo_usuarios t ON u.tipo_usuario = t.id_tipo_usuario
                    WHERE u.id_usuario = %s AND u.deleted = 0
                """
                cursor.execute(sql, (id_buscar,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Error al buscar usuario: {e}")
            return None
        finally:
            db.cerrar()

    def modificar_usuario(self):
        db = Conexión()
        conn = db.conectar()
        if not conn: return False
        
        try:
            with conn.cursor() as cursor:
                sql = """
                    UPDATE usuarios 
                    SET nombre_usuario = %s, contrasena = %s, tipo_usuario = %s 
                    WHERE id_usuario = %s AND deleted = 0
                """
                cursor.execute(sql, (self.nombre_usuario, self.contrasena, self.tipo_usuario, self.id_usuario))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al modificar usuario: {e}")
            return False
        finally:
            db.cerrar()

    @staticmethod
    def eliminar_usuario(id_eliminar):
        db = Conexión()
        conn = db.conectar()
        if not conn: return False
        
        try:
            with conn.cursor() as cursor:
                # Se realiza un borrado lógico (Soft Delete) respetando tu columna 'deleted'
                sql = "UPDATE usuarios SET deleted = 1 WHERE id_usuario = %s"
                cursor.execute(sql, (id_eliminar,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False
        finally:
            db.cerrar()