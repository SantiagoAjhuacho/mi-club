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
        self.__fecha_fundacion = fecha_fundacion  # debe ser un objeto datetime

    # Clase Club - Punto 1: Permitir modificar el presidente del club cuando se produzca un cambio de autoridades.
    def get_presidente(self):
        return self.__presidente

    def set_presidente(self, nuevo_presidente):
        self.__presidente = nuevo_presidente

    def get_fecha_fundacion(self):
        return self.__fecha_fundacion

    # Clase Club - Punto 2: Mostrar la antigüedad del club (años desde la fundación hasta hoy).
    def calcular_antiguedad(self):
        fecha_actual = datetime.now()
        antiguedad = fecha_actual.year - self.__fecha_fundacion.year
        cumpleanios_paso = (fecha_actual.month, fecha_actual.day) >= (self.__fecha_fundacion.month, self.__fecha_fundacion.day)
        if not cumpleanios_paso:
            antiguedad -= 1
        return antiguedad

    # Clase Club - Punto 3: Determinar si el club es institución histórica (más de 50 años).
    def es_institucion_historica(self):
        return self.calcular_antiguedad() > 50

    # Devuelve la info del club como diccionario (reemplaza al viejo mostrar() con print, según Tarea A).
    def obtener_info(self):
        return {
            "nombre": self.nombre, #<--- lo que hace las comas son separar los elementos del diccionario, no es un error de sintaxis.
            "descripcion": self.descripcion,
            "ubicacion": self.ubicacion,
            "presidente": self.__presidente,
            "fecha_fundacion": self.__fecha_fundacion,
        }