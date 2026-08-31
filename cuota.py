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
        """Marca la cuota como pagada."""
        self.__estado = "pagada"

    # 2. Determinar si está vencida
    def esta_vencida(self):
        """Compara la fecha de vencimiento con la fecha actual."""
        if self.__estado == "pagada":
            return False
        fecha_actual = datetime.now()
        return fecha_actual > self.fecha_de_vencimiento

    # 3. Actualizar automáticamente el estado
    def actualizar_estado(self):
        """Recalcula el estado según fecha y pago."""
        if self.__estado == "pagada":
            return self.__estado
        if self.esta_vencida():
            self.__estado = "vencida"
        else:
            self.__estado = "pendiente"
        return self.__estado

    # 4. Días que faltan para el vencimiento
    def dias_para_vencimiento(self):
        """Devuelve días para vencer (negativo si ya venció)."""
        fecha_actual = datetime.now()
        diferencia = self.fecha_de_vencimiento - fecha_actual
        return diferencia.days

    # 5. Renovar para un nuevo período
    def renovar(self, nuevo_periodo, nueva_fecha_vencimiento):
        """Actualiza período y vencimiento, reinicia estado a pendiente."""
        self.periodo = nuevo_periodo
        self.fecha_de_vencimiento = nueva_fecha_vencimiento
        self.__estado = "pendiente"


cuota1= Cuota("pendiente", datetime(2026, 12, 1), "Diciembre 2026")
print("Estado inicial:", cuota1.get_estado())
print("¿Vencida?:", cuota1.esta_vencida())
print("Días para vencer:", cuota1.dias_para_vencimiento())
cuota1.registrar_pago()
print("Estado después de registrar pago:", cuota1.get_estado())
cuota1.actualizar_estado()
print("Estado después de actualizar:", cuota1.get_estado())
cuota1.renovar("Enero 2027", datetime(2027, 1, 1))
print("Estado después de renovar:", cuota1.get_estado())