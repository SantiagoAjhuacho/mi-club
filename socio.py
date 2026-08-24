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

from datetime import datetime
from persona import Persona
from cuota import Cuota

class Socio(Persona):
    def __init__(self, nombre_completo, fecha_nacimiento, tipo_identificacion, identificacion, nacionalidad,
                 fecha_inscripcion, estado="Activo", usuario="", contrasenia=""):
        super().__init__(nombre_completo, fecha_nacimiento, tipo_identificacion, identificacion, nacionalidad)
        self.clubes = []
        self.cuotas = []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado
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

    def asociarse_a_club(self, club):
        """Asocia al socio a un club si no pertenece a él aún."""
        if club not in self.clubes:
            self.clubes.append(club)
            return True
        return False

    def dejar_club(self, club):
        """Desvincula al socio de un club determinado."""
        if club in self.clubes:
            self.clubes.remove(club)
            return True
        return False

    def generar_cuota(self, cuota):
        """Agrega una nueva cuota al historial del socio."""
        self.cuotas.append(cuota)

    def registrar_pago_cuota(self, periodo):
        """Busca una cuota por su período y registra el pago."""
        for cuota in self.cuotas:
            if cuota.periodo == periodo and cuota.get_estado() != "pagada": #<---- lo que estaria diciendo aca es que si la cuota de periodo es igual a la del periodo y la cuota de estado es diferente a pagada entonces se registra el pago de la cuota
                cuota.registrar_pago()
                return True
        return False

    def tiene_deudas(self):
        """Informa True si el socio posee al menos una cuota sin abonar."""
        for cuota in self.cuotas:
            if cuota.get_estado() != "pagada":
                return True
        return False

    def cantidad_cuotas_pendientes(self):
        """Devuelve el total de cuotas impagas."""
        return sum(1 for cuota in self.cuotas if cuota.get_estado() != "pagada")

    def suspender(self):
        """Cambia el estado del socio a Suspendido."""
        self.estado = "Suspendido"

    def reactivar(self):
        """Reactiva al socio para que pueda volver a utilizar los servicios."""
        self.estado = "Activo"

    def actualizar_contrasenia(self, contrasenia_actual, nueva_contrasenia):
        """Permite actualizar la contraseña previa verificación de la actual."""
        if self.__contrasenia == contrasenia_actual:
            self.__contrasenia = nueva_contrasenia
            return True
        return False

    def iniciar_sesion(self, usuario, contrasenia):
        """Verifica los datos de acceso para iniciar sesión."""
        return self.__usuario == usuario and self.__contrasenia == contrasenia


cliente1 = Socio("Juan Pérez", datetime(2009, 9, 20), "DNI", "12345678", "Argentina","01/01/2020", usuario="juanperez", contrasenia="pass123")

cliente1.asociarse_a_club("Club Atlético")

cuota_julio = Cuota("pendiente", datetime(2024, 7, 31), "Cuota Julio 2024")
cliente1.generar_cuota(cuota_julio)

print(cliente1.cantidad_cuotas_pendientes())               # 1
print(cliente1.registrar_pago_cuota("Cuota Julio 2024"))   # True
print(cliente1.tiene_deudas())                              # False
cliente1.suspender()
cliente1.reactivar()
print(cliente1.actualizar_contrasenia("pass123", "newpass456"))  # True