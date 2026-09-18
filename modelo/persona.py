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

    # Getter/setter de tipo_identificacion
    def get_tipo_identificacion(self):
        return self.__tipo_identificacion

    def set_tipo_identificacion(self, tipo_identificacion):
        self.__tipo_identificacion = tipo_identificacion

    # Getter/setter de identificacion
    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    # Getter/setter de nacionalidad
    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # Clase Persona - Punto 1: Determinar automáticamente si una persona es mayor o menor de edad.
    # Calcula la edad comparando la fecha de nacimiento con la fecha actual (no depende de un número pasado a mano).
    def calcular_edad(self):
        fecha_actual = datetime.now()
        edad = fecha_actual.year - self.__fecha_nacimiento.year
        cumple_paso = (fecha_actual.month, fecha_actual.day) >= (self.__fecha_nacimiento.month, self.__fecha_nacimiento.day)
        if not cumple_paso:
            edad -= 1
        return edad

    # Clase Persona - Punto 1 (continuación): usa calcular_edad() para responder mayor/menor de edad.
    def es_mayor_de_edad(self):
        return self.calcular_edad() >= 18

    # Clase Persona - Punto 2: Verificar que la identificación ingresada sea válida y no se encuentre vacía.
    # Devuelve el resultado en vez de imprimirlo (Tarea A: sin print() dentro de los métodos).
    def validar_identificacion(self):
        if self.__identificacion is None or str(self.__identificacion).strip() == "": # <--- se asegura de que no sea None ni una cadena vacía
            return False
        return True