from datetime import datetime

class Cuota:
    def __init__(self, estado, fecha_de_vencimiento, periodo):
        self.__estado = estado
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.periodo = periodo

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    # 1. Registrar una cuota como pagada
    def registrar_pago(self):
        self.__estado = "pagada"

    # 2. lo que hace este metodo es que si esta vencida la cuota
    def esta_vencida(self):
        if self.__estado == "pagada":
            return False
        fecha_actual = datetime.now()
        return fecha_actual > self.fecha_de_vencimiento

    # 3. Actualizar automáticamente el estado
    def actualizar_estado(self):
        if self.__estado == "pagada":
            return self.__estado
        if self.esta_vencida():
            self.__estado = "vencida"
        else:
            self.__estado = "pendiente"
        return self.__estado

    # 4. Días para el vencimiento
    def dias_para_vencimiento(self):
        fecha_actual = datetime.now()
        diferencia = self.fecha_de_vencimiento - fecha_actual
        return diferencia.days

    # 5. Renovar para un nuevo período
    def renovar(self, nuevo_periodo, nueva_fecha_vencimiento):
        self.periodo = nuevo_periodo
        self.fecha_de_vencimiento = nueva_fecha_vencimiento
        self.__estado = "pendiente"

cuota_cliente = Cuota("pendiente", datetime(2024, 7, 15), "07/2024")
print("Estado inicial de la cuota:", cuota_cliente.get_estado())
cuota_cliente.actualizar_estado()
print("Estado actualizado de la cuota:", cuota_cliente.get_estado())
