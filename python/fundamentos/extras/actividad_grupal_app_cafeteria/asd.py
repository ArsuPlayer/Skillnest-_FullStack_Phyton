class CafeteriaCliente:
    membresia = {"Bronce": 0, "Plata": 0, "Oro": 0}
    total_clientes = 0
    def __init__(self, nombre, membresia="Bronce"):

        self.nombre = nombre
        self.puntos = 0
        self.saldoPendiente = 0.0
        self.membresia = membresia
        CafeteriaCliente.total_clientes += 1
        
    def realizar_compra(self, monto):
        # TODO:
        # Aumentar saldo pendiente
        self.saldoPendiente -= monto
        
        # TODO:
        # Aumentar puntos
        if self.membresia == "Bronce":
            self.puntos += (monto // 100) * 1
        elif self.membresia == "Plata":
            self.puntos += (monto // 100) * 2
        elif self.membresia == "Oro":
            self.puntos += (monto // 100) * 3
        else:
            print("Membresia no coincidente")
        print(f"{self.nombre} realizó una compra de ${monto}")
    
    def pagar_saldo(self, monto):

        if self.saldoPendiente >= 0:
            print("No tienes deudas pendientes")
        elif self.saldoPendiente < 0:
            self.saldoPendiente += monto
            if self.saldoPendiente > 0:
                print(f"Su deuda ha sido pagada\nEl sobrante sera guardado en su saldo. ({self.saldoPendiente})")
            else:
                print("Su deuda ha sido pagada")
    def mostrar_info(self):
        print(f"""
            Nombre: {self.nombre}
            Puntos: {self.puntos}
            Saldo: {self.saldoPendiente}
            Membresia: {self.membresia}
        """)
        pass
    @classmethod
    def mostrar_total_clientes(cls):
        print(f"La cantidad de clientes es {cls.total_clientes}")
        
    @staticmethod
    def validar_membresia(tipo):
        if tipo in CafeteriaCliente.membresia:
            print("Membresía válida")
            return True
        else:
            print("Membresía invalida")
            return False


akon = CafeteriaCliente("Akon", "Plata")
matias = CafeteriaCliente("Matias", "Oro")
benjamin = CafeteriaCliente("Benjamin", "Plata")
fabrizio = CafeteriaCliente("Fabrizio")
akon.realizar_compra(1000)
benjamin.realizar_compra(1000)
matias.realizar_compra(7777)
fabrizio.realizar_compra(1)
matias.pagar_saldo(10000)
akon.pagar_saldo(100)
matias.mostrar_info()
matias.realizar_compra(10000)
matias.mostrar_info()

CafeteriaCliente.mostrar_total_clientes()
print(akon.validar_membresia("Bronce"))
print(akon.validar_membresia("Diamante"))
