#d) Crear el archivo socio.py con la clase Socio:

#Atributos:

#● clubes (lista)
#● cuotas (lista)
#● fecha_inscripcion (DD/MM/AAAA)
#● estado (activo, suspendido, inactivo)
#● __usuario
#● __contraseña

#Métodos:
#● getters y setters

from persona import Persona


class Socio(Persona):
   def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, fecha_inscripcion, estado, usuario, contrasenia):
       super().__init__(nombre_completo, edad, tipo_identificacion, identificacion)   
       self.clubes = []
       self.cuotas = []
       self.fecha_inscripcion = fecha_inscripcion
       self.estado = estado
       self.__nacionalidad = nacionalidad
       self.__usuario = usuario
       self.__contrasenia = contrasenia
  


   def get_usuario (self):
       return self.__usuario


   def set_usuario (self, usuario):
       self.__usuario = usuario


   def get_contrasenia (self):
       return self.__contrasenia
  
   def set_contrasenia (self, contrasenia):
       self.__contrasenia = contrasenia




   def get_nacionalidad (self):
       return self.__nacionalidad
  
   def set_nacionalidad (self, nacionalidad):
       self.__nacionalidad = nacionalidad
