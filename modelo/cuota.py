from datetime import datetime


class Cuota:
    def __init__(self, estado, fecha_de_vencimiento, periodo):
        self.__estado = estado  # "pagada", "pendiente" o "vencida"
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.periodo = periodo

    # Getter/setter de estado
    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    # Clase Cuota - Punto 1: Registrar una cuota como pagada.
    def registrar_pago(self):
        self.__estado = "pagada"

    # Clase Cuota - Punto 2: Determinar si una cuota está vencida comparando fecha de vencimiento vs fecha actual.
    def esta_vencida(self):
        if self.__estado == "pagada":
            return False
        fecha_actual = datetime.now()
        return fecha_actual > self.fecha_de_vencimiento

    # Clase Cuota - Punto 3: Actualizar automáticamente el estado de la cuota cuando corresponda.
    def actualizar_estado(self):
        if self.__estado == "pagada":
            return self.__estado
        if self.esta_vencida():
            self.__estado = "vencida"
        else:
            self.__estado = "pendiente"
        return self.__estado

    # Clase Cuota - Punto 4: Informar cuántos días faltan para el vencimiento de una cuota.
    # Si ya venció, devuelve un número negativo (días de atraso).
    def dias_para_vencimiento(self):
        fecha_actual = datetime.now()
        diferencia = self.fecha_de_vencimiento - fecha_actual
        return diferencia.days

    # Clase Cuota - Punto 5: Permitir la renovación de una cuota para un nuevo período.
    def renovar(self, nuevo_periodo, nueva_fecha_vencimiento):
        self.periodo = nuevo_periodo
        self.fecha_de_vencimiento = nueva_fecha_vencimiento
        self.__estado = "pendiente"