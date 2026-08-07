#e) Crear el archivo admin.py con la clase Administrador:

#Atributos:

#● nombre
#■ __usuario
#● __contraseña

#Métodos:

#● getters y setters


class Administrador:
   def __init__(self, nombre, usuario, contrasenia):
       self.nombre = nombre
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