#f) Crear el archivo cuota.py con la clase Cuota:
#Atributos:

#● __estado (pagada, pendiente, vencida)
#● fecha_de_vencimiento
#● periodo (mes/año)

#Métodos:

#● getters y setters


from datetime import datetime

class Club:
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.__presidente = presidente
        # fecha_fundacion debe ser un objeto de tipo datetime
        self.__fecha_fundacion = fecha_fundacion

    # 1. Modificar el presidente (cambio de autoridades)
    def get_presidente(self):
        return self.__presidente

    def set_presidente(self, nuevo_presidente):
        """Actualiza el presidente del club."""
        self.__presidente = nuevo_presidente

    def get_fecha_fundacion(self):
        return self.__fecha_fundacion

    # 2. Calcular Antigüedad
    def calcular_antiguedad(self):
        fecha_actual = datetime.now()
        antiguedad = fecha_actual.year - self.__fecha_fundacion.year
        cumpleanios_paso = (fecha_actual.month, fecha_actual.day) >= (self.__fecha_fundacion.month, self.__fecha_fundacion.day)
        if not cumpleanios_paso:
            antiguedad -= 1
        return antiguedad

    # 3. Determinar si es Institución Histórica (> 50 años)
    def es_institucion_historica(self):
        return self.calcular_antiguedad() > 50


club = Club("Instituto Deportivo de la gloria", "Establecimiento de deportes",
            "Parque de los Patricios", "Talislao Zen", datetime(1876, 8, 3)) #la fecha debe de ser str
print("Antigüedad:", club.calcular_antiguedad())
print("Es institución histórica:", club.es_institucion_historica())

club.set_presidente("Nuevo Presidente")
print("Presidente actualizado:", club.get_presidente())