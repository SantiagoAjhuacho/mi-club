#e) Crear el archivo admin.py con la clase Administrador:

#Atributos:

#● nombre
#■ __usuario
#● __contraseña

#Métodos:

#● getters y setters

from clubCategoria import ClubCategoria
from datetime import datetime

class Administrador:
    def __init__(self, nombre, usuario, contrasenia):
        self.nombre = nombre
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_contrasenia(self):
        return self.__contrasenia

    def set_contrasenia(self, contrasenia):
        self.__contrasenia = contrasenia

    #Registrar nuevos socios en un club
    def registrar_socio(self, club, socio):
        """El admin le pide al club que registre al socio."""
        return club.registrar_socios(socio)

    #Eliminar socios de un club
    def suspender_socio(self, socio):
        """El admin le pide al socio que se suspenda a sí mismo."""
        socio.suspender()

    #Reactivar socios de un club
    def reactivar_socio(self, socio):
        """El admin le pide al socio que se reactive.""" #<--- El admin no puede cambiar el estado del socio directamente, sino que le pide al socio que se reactive a sí mismo
        socio.reactivar()

    # Listar socios de un club
    def listar_socios(self, club):
        """Devuelve la lista de socios que ya tiene ClubCategoria.""" # <--- El admin no tiene acceso directo a la lista de socios, sino que le pide al club que se la devuelva
        return club.socios()

    # Verificar credenciales de administrador
    def verificar_credenciales(self, usuario, contrasenia):
        return self.__usuario == usuario and self.__contrasenia == contrasenia


admin = Administrador("Ana Gómez", "admin", "admin123")

print(admin.verificar_credenciales("admin", "admin123"))    # True
print(admin.verificar_credenciales("admin", "wrongpass"))   # False
print(admin.verificar_credenciales("wronguser", "admin123"))# False
print(admin.verificar_credenciales("wronguser", "wrongpass"))# False

club = ClubCategoria("Club Deportivo", "Cancha de fútbol", "Buenos Aires", "Gaston", datetime(2000, 12, 9))