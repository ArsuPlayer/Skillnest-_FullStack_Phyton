import os
def positivos_negativos(numeros):
    for num in numeros:
        if num < 0:
            print("Ingresaste un número negativo:", num)
            return False
    
    print(f"Ingresaste los siguientes numeros: {numeros}")
    
    
def ingreso_numeros():
    numeros = []
    cantidad  = int(input("Ingresar cuantos numeros agregara : "))
    for i in range(cantidad):
        num = int(input("Ingresa un número :  "))
        numeros.append(num)
    return numeros

# ----------- EJERCICIO EDADES ------------

def clasificacionEdades(lista):
    menores = 0
    adultos = 0
    mayores = 0

    for i in range(len(lista)):
        if lista[i] < 18:
            menores += 1
        elif lista[i] >= 18 and lista[i] < 60:
            adultos += 1
        elif lista[i] >= 60:
            mayores += 1

    print(f"Edades: {lista}")
    print(f"Hay {menores} menores, {adultos} adultos y {mayores} adultos mayores.")


def ingresoEdad():
    cantidad = int(input("Ingresa cantidad de personas: "))
    edades = []

    for i in range(cantidad): 
        edad = int(input("Ingrese la edad: "))
        edades.append(edad)

    clasificacionEdades(edades)


def limpiar_consola():
    os.system('cls')


# ----------- MENÚ ------------

numeros = []

while True:
    print("\n1. ejercicio 1")
    print("2. ejercicio 2")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        numeros = ingreso_numeros()
        positivos_negativos(numeros)
    elif opcion == "2":
        ingresoEdad()

    elif opcion == "0":
        break

    else:
        print("Opción inválida")