# Diccionarios en python
estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
# Imprimir el nombre de estudiante
print(estudiante["nombre"]) #Imprime: Vicente

estudiante["nombre"] = "Matias" #Imprime: Matias
print(estudiante["nombre"])

# Diccionario de paises
paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Perú"
paises["ARG"] = "Argentina"

# Eliminar valores de diccionario
if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
    print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
    paises["CRI"] = "Costa Rica"

    #Eliminar valores de diccionario
valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}

# Diccionario pintor multilínea
pintor = {
    "nombre": "Frida Kahlo",
    "pais": "México",
    "fecha_nacimiento": "6 de julio de 1907"
}

# Diccionarios anidados
escuela = {
    "nombre": "Coding Dojo LATAM",
    "profesores": [
        {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
        {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
        {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
    ]
}
