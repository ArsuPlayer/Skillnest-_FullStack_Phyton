"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
print("--- 1. Generador de niveles ---")
for nivel in range(101):
    print(nivel)


# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
print("\n--- 2. Potenciadores de energía ---")
for potenciador in range(2, 501, 2):
    print(potenciador)


# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime un emoji (ej. "⭐")
# - Si es divisible por 10, imprime otro emoji (ej. "🎮")
# ¡Cuidado con la prioridad en tus condicionales! (Los múltiplos de 10 también son de 5, por lo que van primero).
print("\n--- 3. Trampa de emojis ---")
for punto in range(1, 101):
    if punto % 10 == 0:
        print(f"Punto {punto}: 🎮 (Múltiplo de 10)")
    elif punto % 5 == 0:
        print(f"Punto {punto}: ⭐ (Múltiplo de 5)")
    else:
        print(f"Punto {punto}")


# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
print("\n--- 4. Suma colosal ---")
suma_total = 0
for numero in range(0, 500001, 2):
    suma_total += numero
print(f"La suma total de los números pares hasta 500,000 es: {suma_total}")


# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
print("\n--- 5. Retroceso temporal ---")
for anio in range(2024, -1, -3):
    print(anio)


# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
print("\n--- 6. Contador dinámico ---")
inicio = 3
fin = 10
salto = 2

for i in range(inicio, fin + 1):
    if i % salto == 0:
        print(i)