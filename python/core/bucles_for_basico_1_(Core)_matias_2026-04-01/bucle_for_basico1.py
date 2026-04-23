"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
def niveles():
    for i in range(0, 101):
        print(i)


# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
def energia():
    for i in range(2, 502, 2):
        print(i)

# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
def trampaEmoji():
    for i in range(1, 101):
        if i % 5 == 0:
            print("😒")
        elif i % 10 == 0:
            print("😎")
        else:
            print(i) 

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
def sumaColosal():
    total = 0
    for i in range(0, 500001, 2):
        total += i
    print(f"El resultado es: {total}")

# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
def retroceso():
    for i in range(2024, -3, -2):
        print(i)



# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.

inicio = 3
fin = 10
salto = 2

def contador():
    print(f"Multiplos de salto ente {salto} entre {inicio} y {fin}")
    for i in range(inicio, fin + 1):
        if i % salto == 0:
            print(i)

# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10



# Menú de navegación 
continuar = True
while continuar:
    print("")
    print("--- 1.- Ejercicio 1---")
    print("--- 2.- Ejercicio 2---")
    print("--- 3.- Ejercicio 3---")
    print("--- 4.- Ejercicio 4---")
    print("--- 5.- Ejercicio 5---")
    print("--- 6.- Ejercicio 6---")


    opcion = input("\n----Elige una opcion: (1-15) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        print(niveles())
    elif opcion == "2":
        print("\Ejecutando ejercicio 2:")
        print(energia())
    elif opcion == "3":
        print("\Ejecutando ejercicio 3:")
        print(trampaEmoji())
    elif opcion == "4":
        print("\Ejecutando ejercicio 4:")
        print(sumaColosal())
    elif opcion == "5":
        print("\Ejecutando ejercicio 5:")
        print(retroceso())
    elif opcion == "6":
        print("\Ejecutando ejercicio 6:")
        print(contador())
