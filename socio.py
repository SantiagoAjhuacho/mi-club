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
    def __init__(self,nombre_completo,edad,tipo_identificacion,identificacion,nacionalidad,fecha_inscripcion,estado="Activo",usuario="",contrasenia=""):
        super().__init__(nombre_completo, edad, tipo_identificacion, identificacion)
        self.clubes = []
        self.cuotas = []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado  # Ejemplos: "Activo", "Suspendido"
        self.__nacionalidad = nacionalidad
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    # --- Getters y Setters ---
    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_contrasenia(self):
        return self.__contrasenia

    def set_contrasenia(self, contrasenia):
        self.__contrasenia = contrasenia

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # --- Métodos de Gestión de Clubes ---

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

    # --- Métodos de Gestión de Cuotas ---

    def generar_cuota(self, cuota):
        """Agrega una nueva cuota al historial del socio."""
        self.cuotas.append(cuota)

    def registrar_pago_cuota(self, periodo):
        """Busca una cuota por su período y registra el pago."""
        for cuota in self.cuotas:
            # Asumiendo que la clase Cuota tiene atributo 'periodo' y método 'pagar' o atributo 'pagada'
            if cuota.periodo == periodo and not cuota.pagada:
                cuota.pagada = True
                return True
        return False  # No se encontró la cuota o ya estaba pagada

    def tiene_deudas(self):
        """Informa True si el socio posee al menos una cuota sin abonar."""
        for cuota in self.cuotas:
            if not cuota.pagada:
                return True
        return False

    def cantidad_cuotas_pendientes(self):
        """Devuelve el total de cuotas impagas."""
        return sum(1 for cuota in self.cuotas if not cuota.pagada)

    # --- Métodos de Estado del Socio ---

    def suspender(self):
        """Cambia el estado del socio a Suspendido."""
        self.estado = "Suspendido"

    def reactivar(self):
        """Reactiva al socio para que pueda volver a utilizar los servicios."""
        self.estado = "Activo"

    # --- Métodos de Seguridad / Autenticación ---

    def actualizar_contrasenia(self, contrasenia_actual, nueva_contrasenia):
        """Permite actualizar la contraseña previa verificación de la actual."""
        if self.__contrasenia == contrasenia_actual:
            self.__contrasenia = nueva_contrasenia
            return True
        return False

    def iniciar_sesion(self, usuario, contrasenia):
        """Verifica los datos de acceso para iniciar sesión."""
        return self.__usuario == usuario and self.__contrasenia == contrasenia

cliente1 = Socio("Juan Pérez", 30, "DNI", "12345678", "Argentina", "01/01/2020", "Activo", "juanperez", "pass123")

cliente1.asociarse_a_club("Club Atlético")
cliente1.generar_cuota("Cuota Julio 2024")
cliente1.cantidad_cuotas_pendientes()  # Devuelve 1, ya que se generó una cuota pendiente
cliente1.registrar_pago_cuota("Cuota Julio 2024")  # Marca la cuota como pagada
cliente1.tiene_deudas()  # Devuelve False, ya que la cuota fue pagada
cliente1.suspender()  # Cambia el estado del socio a "Suspendido"
cliente1.reactivar()  # Cambia el estado del socio a "Activo"
cliente1.actualizar_contrasenia("pass123", "newpass456")  # Actualiza la contraseña