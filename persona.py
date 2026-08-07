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


class Persona:
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.__tipo_identiicacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad


    def get_tipo_identificacion (self):
        return self.__tipo_identiicacion

    def set_tipo_identificacion (self, tipo_identificacion):
        self.__tipo_identiicacion = tipo_identificacion

    
    def get_identificacion (self):
        return self.__identificacion

    def set_identificacion (self, identificacion):
        self.__identificacion = identificacion

    def get_nacionalidad (self):
        return self.__nacionalidad

    def set_nacionalidad (self, nacionalidad):
        self.__nacionalidad = nacionalidad


    def mostrar_datos(self):
        print(f'Nombre completo: {self.nombre_completo}')
        print(f'Edad: {self.edad}')
        print(f'Tipo de Identificacion: {self.__tipo_identiicacion}')
        print(f'Identificacion: {self.identificacion}')
        print(f'Nacionalidad: {self.nacionalidad}')

   # --- Métodos de las consignas ---

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def validar_identificacion(self, identificacion):
        if identificacion == "" or identificacion == " ":
            print("Error: La identificación no puede estar vacía.")
            return False
        else:
            return True



persona1 = Persona("Carlos Gómez", 25, "DNI", "34567890", "Argentina")
persona1.mostrar_datos()


persona2 = Persona("Santi Pérez", 15, "DNI", "", "Uruguay")
persona2.mostrar_datos()

