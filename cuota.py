from persona import Persona
from datetime import datetime

class Socio(Persona):
    def __init__(self, nombre_completo, fecha_nacimiento, tipo_identificacion, identificacion, nacionalidad,
                 fecha_inscripcion, estado="Activo", usuario="", contrasenia=""):
        super().__init__(nombre_completo, fecha_nacimiento, tipo_identificacion, identificacion, nacionalidad)
        self.clubes = []
        self.cuotas = []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado  # Ejemplos: "Activo", "Suspendido"
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

    # --- Métodos de Gestión de Clubes ---

    def asociarse_a_club(self, club):
        if club not in self.clubes:
            self.clubes.append(club)
            return True
        return False

    def dejar_club(self, club):
        if club in self.clubes:
            self.clubes.remove(club)
            return True
        return False

    # --- Métodos de Gestión de Cuotas ---

    def generar_cuota(self, cuota):
        self.cuotas.append(cuota)

    def registrar_pago_cuota(self, periodo):
        for cuota in self.cuotas:
            if cuota.periodo == periodo and cuota.get_estado() != "pagada":
                cuota.registrar_pago()
                return True
        return False

    def tiene_deudas(self):
        for cuota in self.cuotas:
            if cuota.get_estado() != "pagada":
                return True
        return False

    def cantidad_cuotas_pendientes(self):
        return sum(1 for cuota in self.cuotas if cuota.get_estado() != "pagada")

    # --- Métodos de Estado del Socio ---

    def suspender(self):
        self.estado = "Suspendido"

    def reactivar(self):
        self.estado = "Activo"

    # --- Métodos de Seguridad / Autenticación ---

    def actualizar_contrasenia(self, contrasenia_actual, nueva_contrasenia):
        if self.__contrasenia == contrasenia_actual:
            self.__contrasenia = nueva_contrasenia
            return True
        return False

    def iniciar_sesion(self, usuario, contrasenia):
        return self.__usuario == usuario and self.__contrasenia == contrasenia


# --- Pruebas ---
from cuota import Cuota

cliente1 = Socio("Juan Pérez", datetime(1994, 5, 20), "DNI", "12345678", "Argentina",
                  "01/01/2020", "Activo", "juanperez", "pass123")

cliente1.asociarse_a_club("Club Atlético")

cuota_julio = Cuota("pendiente", datetime(2024, 7, 31), "Cuota Julio 2024")
cliente1.generar_cuota(cuota_julio)

print(cliente1.cantidad_cuotas_pendientes())     # 1
print(cliente1.registrar_pago_cuota("Cuota Julio 2024"))  # True
print(cliente1.tiene_deudas())                    # False
cliente1.suspender()
cliente1.reactivar()
print(cliente1.actualizar_contrasenia("pass123", "newpass456"))  # True