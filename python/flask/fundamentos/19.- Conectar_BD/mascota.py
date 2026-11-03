from mysqlconnection import connectToMySQL

class Mascota:
    """
    Modelo de Objeto (POO) que representa la tabla 'mascotas'.
    """
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """Obtiene todas las mascotas registradas."""
        query = "SELECT * FROM mascotas;"
        resultados = connectToMySQL("primera_flask").query_db(query)
        
        mascotas = []
        if resultados:
            for registro in resultados:
                mascotas.append(cls(registro))
        return mascotas

    @classmethod
    def get_by_id(cls, mascota_id):
        """
        Desafío: Consulta una mascota por ID utilizando binding parametrizado safe.
        Devuelve una instancia de Mascota o None si no existe.
        """
        query = "SELECT * FROM mascotas WHERE id = %(id)s;"
        data = {"id": mascota_id}
        
        resultados = connectToMySQL("primera_flask").query_db(query, data)
        
        if resultados:
            return cls(resultados[0])
        return None