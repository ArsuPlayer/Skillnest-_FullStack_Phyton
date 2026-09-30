class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        if tipo_suscripcion in self.costos_suscripcion:
            self.tipo_suscripcion = tipo_suscripcion
        else:
            self.tipo_suscripcion = "Gratis"
        
        self.costo_mensual = self.costos_suscripcion[self.tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        """Reduce el saldo pendiente según el monto pagado."""
        if monto <= 0:
            print(f"[{self.usuario}] El monto del pago debe ser mayor a 0.")
            return
        
        if monto >= self.saldo_pendiente:
            vuelto = monto - self.saldo_pendiente
            self.saldo_pendiente = 0.0
            print(f"[{self.usuario}] Pago exitoso de ${monto:.2f}. Saldo pendiente saldado. Vuelto: ${vuelto:.2f}")
        else:
            self.saldo_pendiente -= monto
            print(f"[{self.usuario}] Pago parcial de ${monto:.2f} realizado. Saldo pendiente restante: ${self.saldo_pendiente:.2f}")

    def cambiar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción y actualiza el costo mensual."""
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
            self.saldo_pendiente += self.costo_mensual
            print(f"[{self.usuario}] Cambio de suscripción exitoso a '{nuevo_tipo}'. Nuevo costo mensual añadido al saldo: ${self.costo_mensual:.2f}")
        else:
            print(f"[{self.usuario}] Tipo de suscripción '{nuevo_tipo}' no válido.")

    def ver_contenido_exclusivo(self):
        """Permite ver contenido exclusivo según el tipo de suscripción."""
        if self.tipo_suscripcion == "Gratis":
            print(f"[{self.usuario}] Acceso denegado. La suscripción 'Gratis' no incluye contenido exclusivo.")
            return False
        else:
            print(f"[{self.usuario}] Reproduciendo contenido exclusivo con suscripción '{self.tipo_suscripcion}'...")
            return True

    def mostrar_info_suscripcion(self):
        """Muestra la información de la suscripción del usuario."""
        print(f"\n--- Información de Suscripción ---")
        print(f"Usuario: {self.usuario}")
        print(f"Tipo de suscripción: {self.tipo_suscripcion}")
        print(f"Costo mensual: ${self.costo_mensual:.2f}")
        print(f"Saldo pendiente: ${self.saldo_pendiente:.2f}")
        print(f"----------------------------------\n")


# Bloque de pruebas detalladas
if __name__ == "__main__":
    print("=== INICIO DE PRUEBAS DE SUSCRIPCIÓN ===\n")
    
    # 1. Crea 3 usuarios con diferentes tipos de suscripción.
    usuario1 = SuscripcionStreaming("Ana", "Gratis")
    usuario2 = SuscripcionStreaming("Carlos", "Estándar")
    usuario3 = SuscripcionStreaming("Sofía", "Premium")

    # 2. Haz que el primer usuario intente ver contenido exclusivo, mejore su suscripción y pague su saldo.
    print("--- PRUEBA 1: Ana (Gratis -> Estándar) ---")
    usuario1.ver_contenido_exclusivo()
    usuario1.cambiar_suscripcion("Estándar")
    usuario1.mostrar_info_suscripcion()
    usuario1.realizar_pago(5.99)
    usuario1.mostrar_info_suscripcion()

    # 3. Haz que el segundo usuario vea contenido exclusivo, cambie su suscripción a Premium y pague dos veces.
    print("--- PRUEBA 2: Carlos (Estándar -> Premium y pagos dobles) ---")
    usuario2.ver_contenido_exclusivo()
    usuario2.cambiar_suscripcion("Premium")
    usuario2.mostrar_info_suscripcion()
    usuario2.realizar_pago(5.99)
    usuario2.realizar_pago(10.99)
    usuario2.mostrar_info_suscripcion()

    # 4. Haz que el tercer usuario intente pagar una cantidad menor a su saldo pendiente y vea contenido exclusivo.
    print("--- PRUEBA 3: Sofía (Pago parcial y contenido exclusivo) ---")
    usuario3.mostrar_info_suscripcion()
    usuario3.realizar_pago(5.00)  # Pago menor al saldo pendiente (10.99)
    usuario3.mostrar_info_suscripcion()
    usuario3.ver_contenido_exclusivo()  # Puede ver contenido a pesar de tener saldo pendiente