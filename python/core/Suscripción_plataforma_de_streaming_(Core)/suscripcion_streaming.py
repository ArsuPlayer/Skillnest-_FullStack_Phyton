class SuscripcionStreaming:
    costos_suscripcion = {
        "Gratis": 0,
        "Estándar": 5.99,
        "Premium": 10.99
    }

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        self.saldo_pendiente -= monto

        if self.saldo_pendiente < 0:
            self.saldo_pendiente = 0

        print(f"Pago realizado. Saldo pendiente: ${self.saldo_pendiente}")

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
            self.saldo_pendiente = self.costo_mensual

            print(f"Suscripción cambiada a {nuevo_tipo}")
        else:
            print("Tipo de suscripción no válido.")

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Premium":
            print("Puedes ver todo el contenido exclusivo Premium.")
        elif self.tipo_suscripcion == "Estándar":
            print("Puedes ver contenido exclusivo Estándar.")
        else:
            print("La suscripción Gratis no tiene contenido exclusivo.")

    def mostrar_info_suscripcion(self):
        print("Usuario:", self.usuario)
        print("Tipo de suscripción:", self.tipo_suscripcion)
        print("Costo mensual:", self.costo_mensual)
        print("Saldo pendiente:", self.saldo_pendiente)


