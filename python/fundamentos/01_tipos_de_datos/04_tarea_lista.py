"""
Actividad: Gestor de inventario
"""

"""1.- Creación: Crear una lista llamada inventario que contenga los siguientes
articulos: "laptop", "ratón", "monitor", "cable hdmi"
"""
inventario = ["laptop", "ratón", "monitor", "cable hdmi"]
print(inventario)

"""
2.- Expansión: Utiliza el método correspondiente para agregar "impresora"
al final de la lista
"""
inventario.append("impresora")
inventario.append("teclado")

"""
3.-Conteo: Utiliza la funcion integrada para mostrar cuántos elementos totales hay en la lista
"""
print(len(inventario))
print(inventario)

"""
4.-Acceso y modificaciones: Modifica "teclado" por "teclado mecánico"
"""
inventario[5] = "teclado mecánico"
print(inventario[5])

"""
5.-Slicing: Crea una nueva lista llamada "promoción",
debe contener sólo los 3 primeros elementos de la lista "articulos".
"""
promoción = inventario[:3]
print(promoción)

"""
6.-Mostrar la lista de inventario ordenado alfabeticamente
"""
inventario.sort()
print(inventario)
"""
7.-Elimina el último elemento de la lista inventario mostrando el elemento
eliminado y la lista final
"""
eliminado = inventario.pop()

print(eliminado)
print(inventario)