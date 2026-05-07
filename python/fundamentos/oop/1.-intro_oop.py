# Creación de la clase usuario - Entidad
class Usuario:
    def __init__(self): #constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0

#Instancias de una clase
miyagi = Usuario()
matias = Usuario()
daniel = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.apellido) #Imprime: Miyagi
print(daniel.email) #Imprime: miyagi@codingdojo.la
print(daniel.limite_credito) #Imprime: 30000
print(daniel.saldo_pagar) #Imprime: 0

#Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000
print(daniel.nombre) #Imprime: Daniel

#Valores a nueva instancia
matias.nombre = "Matias"
matias.apellido = "Rios"
matias.email = "matias@gmail.com"
matias.limite_credito = 20
matias.saldo_pagar = 1000

#Imprimir nombre de cada instancia
print(miyagi.nombre)
print(daniel.nombre)
print(matias.nombre)
