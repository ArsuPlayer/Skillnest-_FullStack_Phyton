"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random #Importación de libreria para procesos aleatorios


nombre = "Frida Kahlo" #Creación de variable tipo string y se asigna valor
print(type(nombre)) #type() = Método de python para mostrar tipo de una variable
print(len(nombre)) #len() = Devuelve el largo de una variable


edad = 25 #Creación de variable tipo númerico(int).


if edad < 18: #Se establece condición if y 
   print("Eres menor de edad.") #Imprime un mensaje 
elif edad == 18: #Se establece subcondición elif(else if)
   print("Tienes 18 años.") #Imprime un mensaje
else: #Cierre de condición (Si no se cumplen condiciones anteriores)
   print("Eres mayor de edad.") #Imprime un mensaje


frutas = ["manzana", "pera", "fresa"] #Crea un Array(Arreglo) con valores ya asignados
print(frutas[0]) #Mostramos la primera posición array
frutas[0] = "banana" #A la posición 0 del array se le asigna el valor de "banana"
frutas.append("uva") #Se le agrega "uva" al final del array
frutas.remove("pera") #Se remueve la palabra "pera" del array


dimensiones = (200, 50) #Crea variable tipo tupla (variable inmutable)
print(dimensiones[0]) #Imprime la posición 0 de la variable creada(tupla)


persona = { #Variable tipo object
   "nombre": "Carlos", #Se establece item y su respectivo valor
   "edad": 30 #Se establece item y su respectivo valor
}
print(persona["nombre"]) #Imprime el valor del del item(ej: "Carlos")
persona["edad"] = 31 #Se modifica el valor del item edad a 31
persona["ciudad"] = "Santiago" #Se agrega un nuevo item con un valor
del persona["ciudad"] #Se elimina el item completo


for i in range(5): #for range: Se crea bucle en rango desde 0 a 5
   if i == 2: # Se establece condición if == 2
       continue #continue ignora el proceso y continua.
   if i == 4: #Se establece condición if == 4
       break #Si i = 4 se rompe el bucle
   print(i) #Imprime valor de i en cada iteración. (hasta 4)


contador = 0 #Se crea una variable contador tipo numerica(int)
while contador < 3: #Se crea bucle while con una condición
   print(f"while contador es: {contador}") #Imprime el contador en un mensaje concatenado con f"" string
   contador += 1 #Incrementa el valor en 1 en cada iteración


def saludar_usuario(nombre): #def - Palabra reservada para crear una función
   return f"Hola, {nombre}" #Devuelve un valor de la función.


print(saludar_usuario("Francisca")) #Se imprimke "Hola Francisca" - return de la función 