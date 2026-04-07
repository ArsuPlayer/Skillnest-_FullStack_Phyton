# hola_mundo.py (Versión SIN respuestas)

# 1. Imprime "Hola, mundo"
#    Reemplaza el comentario con el código necesario para que, al ejecutar,
#    aparezca en pantalla la frase "Hola, mundo".
#    Ejemplo de uso: print("Mensaje")
# ---------------------------------------------------------------
print("Hola, mundo")


# 2. Imprime "Hola, Valeria" con el nombre en una variable
#    a) Concatenación usando comas
#    b) Concatenación usando +
# ---------------------------------------------------------------
nombre = "Valeria"
print(f"Hola,", (nombre))



# 3. Imprime "Hola 156!" con el número en una variable
#    a) Usando comas
#    b) Usando + (esto podría dar error si no conviertes el número a str)
# ---------------------------------------------------------------
numero = 156
print("Hola,", numero)
print("Hola, " + str(numero) + "!")



# 4. Imprime "Me encanta comer X e Y" con dos de tus comidas favoritas
#    a) Usando .format()
#    b) Usando f-strings
# ---------------------------------------------------------------
comida1 = "Lazaña"
comida2 = "Pastel de papa"
print("Me encanta comer {} y {}.".format(comida1,comida2))
print(f"Me encanta comer {comida1} y {comida2}.")



# Desafío bonus: Usa al menos un método de cadena adicional.
# Ejemplo: .upper(), .lower(), .replace(), etc.
# ---------------------------------------------------------------
nombre = input("Ingresa tu nombre: ")
nombre_mayuscula = nombre.upper()
print(nombre)
