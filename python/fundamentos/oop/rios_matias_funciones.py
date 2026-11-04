# ==========================================================
# ACTIVIDAD: DESARROLLO DE FUNCIONES EN PYTHON
# ALUMNO: Matias
# ==========================================================

# 1. Función para mostrar el número mayor y menor de una lista
def ejercicio_mayor_menor():
    print("\n--- 1. Número Mayor y Menor ---")
    entrada = input("Ingresa números enteros separados por espacio: ")
    try:
        numeros = [int(x) for x in entrada.split()]
        if not numeros:
            print("La lista está vacía.")
            return
        mayor = max(numeros)
        menor = min(numeros)
        print(f"Lista ingresada: {numeros}")
        print(f"El número mayor es: {mayor}")
        print(f"El número menor es: {menor}")
    except ValueError:
        print("Error: Asegúrate de ingresar solo números enteros.")


# 2. Función para contar vocales en una cadena de texto
def ejercicio_contar_vocales():
    print("\n--- 2. Contador de Vocales ---")
    texto = input("Ingresa una cadena de texto: ")
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    print(f"El texto contiene {contador} vocales.")


# 3. Función para mostrar nombres con más de 5 letras
def ejercicio_filtrar_nombres():
    print("\n--- 3. Nombres con más de 5 letras ---")
    entrada = input("Ingresa nombres separados por comas o espacios: ")
    # Limpiamos los espacios y separamos por comas si las hay, o por espacios
    if "," in entrada:
        nombres = [n.strip() for n in entrada.split(",")]
    else:
        nombres = [n.strip() for n in entrada.split()]
    
    print("Nombres con más de 5 letras:")
    encontrado = False
    for nombre in nombres:
        if len(nombre) > 5:
            print(f"- {nombre} ({len(nombre)} letras)")
            encontrado = True
    if not encontrado:
        print("Ningún nombre supera las 5 letras.")


# 4. Función para calcular promedio de notas y verificar aprobación
def ejercicio_calcular_promedio():
    print("\n--- 4. Promedio de Notas ---")
    entrada = input("Ingresa las notas decimales separadas por espacio (ej: 3.5 5.0 4.2): ")
    try:
        notas = [float(x) for x in entrada.split()]
        if not notas:
            print("No se ingresaron notas.")
            return
        promedio = sum(notas) / len(notas)
        print(f"Notas: {notas}")
        print(f"Promedio final: {promedio:.2f}")
        if promedio >= 4.0:
            print("Estado: ¡APROBADO! (Promedio mayor o igual a 4.0)")
        else:
            print("Estado: REPROBADO (Promedio menor a 4.0)")
    except ValueError:
        print("Error: Ingresa números decimales válidos (usa punto para los decimales).")


# 5. Función para aplicar descuento del 10% a precios de productos
def ejercicio_aplicar_descuento():
    print("\n--- 5. Descuento de Productos (10%) ---")
    entrada = input("Ingresa los precios de los productos separados por espacio: ")
    try:
        precios = [float(x) for x in entrada.split()]
        if not precios:
            print("No se ingresaron precios.")
            return
        print("\nDetalle de precios con 10% de descuento:")
        for i, precio in enumerate(precios, start=1):
            descuento = precio * 0.10
            nuevo_valor = precio - descuento
            print(f"Producto {i} -> Valor Original: ${precio:.2f} | Nuevo Valor: ${nuevo_valor:.2f}")
    except ValueError:
        print("Error: Ingresa precios numéricos válidos.")


# 6. Función para determinar si un número es par o impar
def ejercicio_par_impar():
    print("\n--- 6. Número Par o Impar ---")
    entrada = input("Ingresa un número entero: ")
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"El número {numero} es PAR.")
        else:
            print(f"El número {numero} es IMPAR.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")


# 7. Función para contar cuántas personas son mayores de edad (>= 18)
def ejercicio_mayores_edad():
    print("\n--- 7. Conteo de Mayores de Edad ---")
    entrada = input("Ingresa las edades separadas por espacio: ")
    try:
        edades = [int(x) for x in entrada.split()]
        if not edades:
            print("No se ingresaron edades.")
            return
        mayores = 0
        for edad in edades:
            if edad >= 18:
                mayores += 1
        print(f"Edades ingresadas: {edades}")
        print(f"Cantidad de personas mayores de edad (18 años o más): {mayores}")
    except ValueError:
        print("Error: Ingresa solo números enteros para las edades.")


# 8. Función para buscar cuántas veces aparece una palabra específica
def ejercicio_buscar_palabra():
    print("\n--- 8. Frecuencia de una Palabra ---")
    entrada = input("Ingresa una lista de palabras separadas por espacio: ")
    palabras = entrada.split()
    if not palabras:
        print("La lista está vacía.")
        return
    
    buscada = input("Ingresa la palabra específica que deseas buscar: ").strip()
    contador = 0
    for palabra in palabras:
        # Comparamos ignorando mayúsculas/minúsculas para mayor precisión
        if palabra.lower() == buscada.lower():
            contador += 1
            
    print(f"La palabra '{buscada}' aparece {contador} vez/veces en la lista.")


# 9. Función para generar una nueva lista únicamente con números positivos
def ejercicio_filtrar_positivos():
    print("\n--- 9. Filtrar Números Positivos ---")
    entrada = input("Ingresa números (positivos y negativos) separados por espacio: ")
    try:
        numeros = [float(x) for x in entrada.split()]
        if not numeros:
            print("No se ingresaron números.")
            return
        
        positivos = []
        for num in numeros:
            if num > 0:
                positivos.append(num)
                
        print(f"Lista original: {numeros}")
        print(f"Lista solo con números positivos: {positivos}")
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")


# 10. Función con diccionarios para productos con stock menor a 5
def ejercicio_stock_productos():
    print("\n--- 10. Control de Stock de Productos ---")
    print("Ingrese los datos de los productos.")
    productos = []
    
    while True:
        nombre = input("Nombre del producto (o escribe 'salir' para terminar): ").strip()
        if nombre.lower() == 'salir':
            break
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
            
        try:
            stock = int(input(f"Stock disponible para {nombre}: "))
            # Usando diccionario tal como lo solicita la pauta
            producto = {"nombre": nombre, "stock": stock}
            productos.append(producto)
        except ValueError:
            print("Error: El stock debe ser un número entero.")

    if not productos:
        print("No se registraron productos.")
        return

    print("\nProductos con stock crítico (menor a 5 unidades):")
    encontrado_critico = False
    for prod in productos:
        if prod["stock"] < 5:
            print(f"- Producto: {prod['nombre']} | Stock: {prod['stock']}")
            encontrado_critico = True
            
    if not encontrado_critico:
        print("¡Excelente! Ningún producto tiene stock menor a 5.")


# ==========================================================
# MENÚ PRINCIPAL INTERACTIVO
# ==========================================================
def main():
    while True:
        print("\n==============================================")
        print("          MENÚ PRINCIPAL DE FUNCIONES         ")
        print("==============================================")
        print("1. Mostrar número mayor y menor de una lista")
        print("2. Contar vocales en un texto")
        print("3. Filtrar nombres con más de 5 letras")
        print("4. Calcular promedio de notas y estado de aprobación")
        print("5. Aplicar descuento del 10% a precios")
        print("6. Determinar si un número es par o impar")
        print("7. Contar personas mayores de edad (>= 18)")
        print("8. Buscar cuántas veces se repite una palabra")
        print("9. Filtrar y generar nueva lista con números positivos")
        print("10. Gestionar productos y detectar stock menor a 5 (Diccionarios)")
        print("0. Salir")
        print("==============================================")
        
        opcion = input("Selecciona una opción (0-10): ").strip()
        
        if opcion == "1":
            ejercicio_mayor_menor()
        elif opcion == "2":
            ejercicio_contar_vocales()
        elif opcion == "3":
            ejercicio_filtrar_nombres()
        elif opcion == "4":
            ejercicio_calcular_promedio()
        elif opcion == "5":
            ejercicio_aplicar_descuento()
        elif opcion == "6":
            ejercicio_par_impar()
        elif opcion == "7":
            ejercicio_mayores_edad()
        elif opcion == "8":
            ejercicio_buscar_palabra()
        elif opcion == "9":
            ejercicio_filtrar_positivos()
        elif opcion == "10":
            ejercicio_stock_productos()
        elif opcion == "0":
            print("\nSaliendo del sistema. ¡Hasta luego, Matias!")
            break
        else:
            print("\n[!] Opción inválida. Por favor, selecciona un número entre 0 y 10.")


# Ejecución principal del programa
if __name__ == "__main__":
    main()