#➡️ Pasar argumentos 
#Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__
# y que de esta manera podamos asignarle a los atributos los valores correspondientes.
class Usuario:
    def __init__(self, nombre, apellido, email,limite_credito,saldo_pagar):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar

#Creación de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 1000, 20)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 2000, 2000)
matias = Usuario("Matias", "Rios", "matias@gmail.com", 1, 2)

#Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

#----------------------------------------------------
#------------------Tarea rápida----------------------
'''
Crear una clase Estudiante y asignarle los siguientes atributos:
(rut,nombre,apellido,especialidad,fecha_nacimiento)
Crear 3 instancias para la clase con distintos estudiantes.
Imprimir: nombre y apellido concatenado + especialidad
'''
class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nacimiento):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nacimiento = fecha_nacimiento

miyagi = Estudiante(22875342-1, "Nariyoshi", "Miyagi", "Contabilidad", 10/10/1979)
daniel = Estudiante(22875342-3, "Daniel", "Larusso", "Programación", 20/12/2000)
matias = Estudiante(22875342-6, "Matias", "Rios", "Programación", 10/11/2008)

print(matias.nombre + " " + matias.apellido + " " + matias.especialidad)
print(daniel.nombre + " " + daniel.apellido + " " + daniel.especialidad)
print(miyagi.nombre + " " + miyagi.apellido + " " + miyagi.especialidad)
