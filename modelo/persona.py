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
    def __init__(self, nombre_completo, fecha_nacimiento, tipo_identificacion, identificacion, nacionalidad): #Me olvide de poner el atributo edad
        self.nombre_completo = nombre_completo
        self.__fecha_nacimiento = fecha_nacimiento
        self.__tipo_identificacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad

    def get_tipo_identificacion(self):
        return self.__tipo_identificacion

    def set_tipo_identificacion(self, tipo_identificacion):
        self.__tipo_identificacion = tipo_identificacion

    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # 1. Determinar si es mayor o menor de edad
    def calcular_edad(self):
        fecha_actual = datetime.now()
        edad = fecha_actual.year - self.__fecha_nacimiento.year
        cumple_paso = (fecha_actual.month, fecha_actual.day) >= (self.__fecha_nacimiento.month, self.__fecha_nacimiento.day)
        #cuando agregue el atributo edad tengo que modificar este metodo
        if not cumple_paso:
            edad -= 1
        return edad

    def es_mayor_de_edad(self):
        return self.calcular_edad() >= 18

    # 2. Verificar que la identificación sea válida y no esté vacía
    def validar_identificacion(self):
        """Valida que self.__identificacion no esté vacía ni compuesta solo de espacios."""
        if str(self.__identificacion).strip() == "":
            print("Error: La identificación no puede estar vacía.")
            return False
        return True



persona1 = Persona("Santiago Ariel", datetime(2000, 3, 15), "DNI", "34567890", "Argentina")
print("¿Es mayor de edad?:", persona1.es_mayor_de_edad())
print("¿Identificación válida?:", persona1.validar_identificacion())

persona2 = Persona("Arian Palacios", datetime(2015, 6, 1), "DNI", "", "Uruguay")
print("¿Es mayor de edad?:", persona2.es_mayor_de_edad())
print("¿Identificación válida?:", persona2.validar_identificacion())