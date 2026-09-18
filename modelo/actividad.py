class Actividad:
    # Tarea E: nueva clase Actividad, con nombre, día y horario como atributos mínimos.
    def __init__(self, nombre, dia, horario):
        self.nombre = nombre
        self.dia = dia
        self.horario = horario

    # Getter/setter de nombre
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    # Getter/setter de día
    def get_dia(self):
        return self.dia

    def set_dia(self, dia):
        self.dia = dia

    # Getter/setter de horario
    def get_horario(self):
        return self.horario

    def set_horario(self, horario):
        self.horario = horario

    # Tarea E: método que retorna la información de la actividad (sin usar print, según Tarea A).
    def obtener_informacion(self):
        return f"{self.nombre} - {self.dia} - {self.horario}"