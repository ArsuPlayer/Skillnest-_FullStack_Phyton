class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

    def aumentarCredito(self, aumento):
        self.limite_credito += aumento

#Instancias de la clase
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

print("----------------------Compras Miyagi------------------------------")
miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
segundacompra = 300
miyagi.hacer_compra(segundacompra)
print(f"Segunda compra: ${segundacompra}")
#Imprimir cuanto crédito le queda a Miyagi
print(f"Crédito disponible ${miyagi.limite_credito - miyagi.saldo_pagar}")
daniel.hacer_compra(45)
print(daniel.saldo_pagar) #Imprime: 45

print("----------------------Compras Daniel------------------------------")


# Tarea
'''
1.-Crear un nuevo método que permita aumentar el límite de crédito.
Imprimir el nuevo límite de crédito.

2.- Crear un método que permita cambiar el correo de la instancia.
'''

miyagi.aumentarCredito(2000)
print(f"El nuevo crédito de {miyagi.nombre} es: {miyagi.limite_credito}")