import os
# Funciones básicas práctica 2

#Ejercicio 1°
# Calcula experiencia
def multiplica_por_2(num):
    result = []
    for i in range (num + 1):
        result.append(i * 2)
    return result

def ejercicio1():
    result1 = multiplica_por_2(5)
    print(result1)
# Debe retornar: [0, 2, 4, 6, 8, 10]


#Ejercicio 2°
# Analiza publicaciones
def suma_y_resta(a):
    print(a[0] + a[1])
    return a[0] - a[1]
# Imprime: 235 y retorna:  5


#Ejercicio 3°
# Puntaje ajustado
def sumatoria_menos_longitud(b):
    total = 0
    largo = len(b)
    for i in range(largo):
        total += b[i]
    print(f"Suma total = {total}, longitud = {largo}")
    return total - largo
# Suma total = 25, longitud = 4, debe retornar: 21


#Ejercicio 4°
# Ajusta visualizaciones
def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))
        return []
    else: 
        segEle = lista[1]
        nuevaLista = []
        for i in lista:
            nuevaLista.append(i * segEle)
            long = len(nuevaLista)
            print(long)
            return nuevaLista
def ejercicio4():
    valores_multiplicados_segundo([100, 3, 50, 20])
# Imprime: 4 y retorna: [300, 9, 150, 60]

    valores_multiplicados_segundo([100])
# Imprime: 1 y retorna: []


#Ejercicio 5°
# Genera precio fijo
def valor_multiplicado_longitud(a, b):
    multList = []
    for i in range(0, b):
        multList.append(a * b)
    return multList

def ejercicio5():
    result1 = valor_multiplicado_longitud(5, 2)
    print(f"Resultado 1: {result1}")
# Debe retornar: [10, 10]
    result2 = valor_multiplicado_longitud(7, 5)
    print(f"Resultado 2: {result2}")
# Debe retornar: [35, 35, 35, 35, 35]


def limpiar_consola():
    os.system('cls')

# Menú de navegación 
continuar = True
while continuar:
    print("")
    print("--- 1.- Ejercicio 1---")
    print("--- 2.- Ejercicio 2---")
    print("--- 3.- Ejercicio 3---")
    print("--- 4.- Ejercicio 4---")
    print("--- 5.- Ejercicio 5---")

    opcion = input("\n----Elige una opcion: (1-15) (0 para salir) =")
    if opcion == "1":
        limpiar_consola()
        print("\nEjecutando ejercicio 1: ")
        print(multiplica_por_2())
    elif opcion == "2":
        limpiar_consola()
        print("\Ejecutando ejercicio 2:")
        print(suma_y_resta())
    elif opcion == "3":
        limpiar_consola()
        print("\Ejecutando ejercicio 3:")
        print(sumatoria_menos_longitud())
    elif opcion == "4":
        limpiar_consola()
        print("\Ejecutando ejercicio 4:")
        print(valores_multiplicados_segundo())
    elif opcion == "5":
        limpiar_consola()
        print("\Ejecutando ejercicio 5:")
        print(valor_multiplicado_longitud())
    else:
        print("Opción no válida, intenta otra vez")
