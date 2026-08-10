#c) Crear el archivo persona.py con la clase Persona:
#Atributos:
#● nombre_completo
#● edad
#● __tipo_identificacion (DNI, Pasaporte, Cédula de identidad)
#● __identificacion
#● __nacionalidad
#Métodos:
#● mostrar_datos()
#● getters y setters

from datetime import datetime

class Persona:
    def __init__(self, nombre_completo, fecha_nacimiento, tipo_identificacion, identificacion, nacionalidad):
        self.nombre_completo = nombre_completo
        self.__fecha_nacimiento = fecha_nacimiento
        self.__tipo_identificacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad


    def get_tipo_identificacion (self):
        return self.__tipo_identificacion

    def set_tipo_identificacion (self, tipo_identificacion):
        self.__tipo_identificacion = tipo_identificacion

    
    def get_identificacion (self):
        return self.__identificacion

    def set_identificacion (self, identificacion):
        self.__identificacion = identificacion

    def get_nacionalidad (self):
        return self.__nacionalidad

    def set_nacionalidad (self, nacionalidad):
        self.__nacionalidad = nacionalidad


    def calcular_edad(self):
        fecha_actual = datetime.now()
        edad = fecha_actual.year - self.__fecha_nacimiento.year
        cumple_paso = (fecha_actual.month, fecha_actual.day) >= (self.__fecha_nacimiento.month, self.__fecha_nacimiento.day)
        if not cumple_paso:
            edad -= 1
        return edad

    def es_mayor_de_edad(self):
        return self.calcular_edad() >= 18


persona1 = Persona("Santiago Ariel", datetime(2000, 3, 15), "DNI", "34567890", "Argentina")
print("¿Es mayor de edad?:  ", persona1.es_mayor_de_edad())  # con el data time lo que hace es calcular realmente la edad de la persona y no solo se guia por un numero que le pasamos como parametro.

persona2 = Persona("Arian Palacios", datetime(2015, 6, 1), "DNI", "40111222", "Argentina")
print("¿Es mayor de edad?:  ", persona2.es_mayor_de_edad())