#f) Crear el archivo cuota.py con la clase Cuota:
#Atributos:

#● __estado (pagada, pendiente, vencida)
#● fecha_de_vencimiento
#● periodo (mes/año)

#Métodos:

#● getters y setters


from datetime import datetime #<---- Crear una fecha fija (de nacimiento, fundación, vencimiento).

class Club:
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.__presidente = presidente
        # fecha_fundacion debe ser un objeto de tipo datetime 
        self.__fecha_fundacion = fecha_fundacion

  # Metodo 1: Calcular Antigüedad
    def calcular_antiguedad(self):
        # estoy guardando en una variable la fecha actual
        fecha_actual = datetime.now() 
        
        # se hace el calculo para ver cuantos años tiene de antiguedad
        antiguedad = fecha_actual.year - self.__fecha_fundacion.year
        
        # aca ajusto por si no paso la fecha de aniversario
        cumpleanios_paso = (fecha_actual.month, fecha_actual.day) >= (self.__fecha_fundacion.month, self.__fecha_fundacion.day)
        if not cumpleanios_paso:
            antiguedad -= 1
            
        # Devolver el valor calculado
        return antiguedad


    # Método 2: Determinar si es Institución Histórica (> 50 años)
    def es_institucion_historica(self):
        return self.calcular_antiguedad() > 50

club = Club("Instituto Deportivo de la gloria", "Establecimiento de deportes de gran altura", "Parque de los Patricios", "Talislao Zen", datetime(2000,8,3))
print("Antigüedad del club:", club.calcular_antiguedad())
print("Es institución histórica:", club.es_institucion_historica())