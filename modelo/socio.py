#e) Crear el archivo admin.py con la clase Administrador:

#Atributos:

#● nombre
#■ __usuario
#● __contraseña

#Métodos:

#● getters y setters
from modelo.persona import Persona


class Socio(Persona):
    # Tarea C: Socio hereda de Persona y usa super().__init__() para inicializar lo heredado.
    # Tarea D: se agrega el atributo "rol" (reemplaza a la clase Administrador suelta).
    def __init__(self, nombre_completo, fecha_nacimiento, tipo_identificacion, identificacion, nacionalidad,
                 fecha_inscripcion, estado="Activo", usuario="", contrasenia="", rol="socio"):
        super().__init__(nombre_completo, fecha_nacimiento, tipo_identificacion, identificacion, nacionalidad)
        self.clubes = []
        self.cuotas = []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado  # "Activo" o "Suspendido"
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        self.__rol = rol  # "socio" o "admin"

    # Getter/setter de usuario
    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    # Getter/setter de contraseña
    def get_contrasenia(self):
        return self.__contrasenia

    def set_contrasenia(self, contrasenia):
        self.__contrasenia = contrasenia

    # Getter/setter de rol
    def get_rol(self):
        return self.__rol

    def set_rol(self, rol):
        self.__rol = rol

    # Tarea D: método que consulta el rol. Reemplaza la necesidad de una clase Administrador aparte.
    def es_admin(self):
        return self.__rol == "admin"

    # Clase Socio - Punto 1: Permitir que un socio pueda asociarse a uno o más clubes.
    def asociarse_a_club(self, club):
        if club not in self.clubes:
            self.clubes.append(club)
            return True
        return False

    # Clase Socio - Punto 2: Permitir que un socio deje de pertenecer a un club determinado.
    def dejar_club(self, club):
        if club in self.clubes:
            self.clubes.remove(club)
            return True
        return False

    # Clase Socio - Punto 3: Generar nuevas cuotas correspondientes a distintos períodos.
    def generar_cuota(self, cuota):
        self.cuotas.append(cuota)

    # Clase Socio - Punto 4: Registrar el pago de una cuota pendiente.
    def registrar_pago_cuota(self, periodo):
        for cuota in self.cuotas:
            if cuota.periodo == periodo and cuota.get_estado() != "pagada":
                cuota.registrar_pago()
                return True
        return False

    # Clase Socio - Punto 5: Informar si el socio posee deudas o cuotas sin abonar.
    def tiene_deudas(self):
        for cuota in self.cuotas:
            if cuota.get_estado() != "pagada":
                return True
        return False

    # Clase Socio - Punto 6: Mostrar la cantidad de cuotas pendientes de pago.
    def cantidad_cuotas_pendientes(self):
        return sum(1 for cuota in self.cuotas if cuota.get_estado() != "pagada")

    # Clase Socio - Punto 7: Cambiar el estado de un socio activo a suspendido cuando corresponda.
    def suspender(self):
        self.estado = "Suspendido"

    # Clase Socio - Punto 8: Reactivar un socio suspendido.
    def reactivar(self):
        self.estado = "Activo"

    # Clase Socio - Punto 9: Permitir la actualización de la contraseña de acceso al sistema.
    def actualizar_contrasenia(self, contrasenia_actual, nueva_contrasenia):
        if self.__contrasenia == contrasenia_actual:
            self.__contrasenia = nueva_contrasenia
            return True
        return False

    # Clase Socio - Punto 10: Verificar los datos de acceso al iniciar sesión.
    def iniciar_sesion(self, usuario, contrasenia):
        return self.__usuario == usuario and self.__contrasenia == contrasenia

    # Representación legible del objeto (para que print(socio) no muestre una dirección de memoria)
    def __str__(self):
        return f"{self.nombre_completo} ({self.estado}, rol: {self.__rol})"