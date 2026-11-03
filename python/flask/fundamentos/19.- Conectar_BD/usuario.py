from mysqlconnection import connectToMySQL

class Usuario:
    """
    Modelo de Objeto (POO) que representa la tabla 'usuarios'.
    """
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """Obtiene todos los usuarios registrados."""
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL("primera_flask").query_db(query)
        
        usuarios = []
        if resultados:
            for registro in resultados:
                usuarios.append(cls(registro))
        return usuarios

    @classmethod
    def get_by_id(cls, usuario_id):
        """Consulta un usuario por su ID."""
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        data = {"id": usuario_id}
        
        resultados = connectToMySQL("primera_flask").query_db(query, data)
        
        if resultados:
            return cls(resultados[0])
        return None