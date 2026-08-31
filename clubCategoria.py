from club import Club
from datetime import datetime

class ClubCategoria(Club):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []
        self.actividades = []

    def get_socios(self):
        return self.__socios

    def set_socios(self, socios):
        self.__socios = socios

    def mostrar_socios(self):
        if not self.__socios:
            print("No hay socios registrados.")
            return
        print("· Lista de Socios:")
        for socio in self.__socios:
            print(f"Socio: {socio}")

    def mostrar(self):
        print("Nombre:  ", self.nombre)
        print("Descripcion: ", self.descripcion)
        print("Ubicacion:   ", self.ubicacion)
        print("Presidente:  ", self.get_presidente())
        print("Fecha De Fundacion:  ", self.get_fecha_fundacion())

    # 1. Registrar nuevos socios en la categoría
    def registrar_socios(self, socio):
        #Agrega un socio si aún no está registrado
        if socio not in self.__socios:
            self.__socios.append(socio)
            return True
        return False

    # 2. Eliminar socios de la categoría
    def eliminar_socio(self, socio):
        if socio in self.__socios:
            self.__socios.remove(socio)
            print(f"Socio '{socio}' eliminado con éxito.")
            return True
        print(f"El socio '{socio}' no se encontró.")
        return False

    # 3. Buscar un socio por dato identificatorio
    def buscar_socio(self, dato_identificatorio):
        #Busca un socio; funciona tanto si guardás strings como objetos Socio con get_identificacion()
        for socio in self.__socios:
            identificador = socio.get_identificacion() if hasattr(socio, "get_identificacion") else socio # hasattr(objeto, "nombre") te dice True o False según si ese objeto tiene ese atributo o método, para que puedas preguntarlo antes de usarlo y evitar que el programa explote si no lo tiene
            if identificador == dato_identificatorio:
                print(f"Se encontró al socio: {socio}")
                return socio
        print("Socio no encontrado.")
        return None

    # 4. Cantidad total de socios
    def cantidad_socio(self):
        return len(self.__socio) #que devuelva como mensaje si no hay socios

    # 5. Agregar nueva actividad
    def actividad_nueva(self, actividad):
        self.actividades.append(actividad)
        print(f"Actividad '{actividad}' agregada.")
        #hacer una condicion para verifica si ya esta la actividad y para eliminar

    # 6. Eliminar actividad
    def eliminar_actividad(self, actividad):
        if actividad in self.actividades:
            self.actividades.remove(actividad)
            print(f"Actividad '{actividad}' eliminada por completo.")

    # 7. Mostrar listado de actividades
    def mostrar_actividades(self):
        for i in self.actividades:
            print(i)

    # 8. Porcentaje de socios activos
    def porcentaje_socios_activos(self):
        """Requiere que self.__socios contenga objetos Socio (con atributo .estado), no strings."""
        if not self.__socios:
            return 0
        activos = sum(1 for s in self.__socios if getattr(s, "estado", None) == "Activo")
        return (activos / len(self.__socios)) * 100

    #modificar este metodo como nosotros estuvimos trabajando

club_deportivo = ClubCategoria("VoleyBall", "cancha Voley 18x9 metros","Polideportivo Benito Quinquela Martín", "Gaston", datetime(2000, 12, 9))

club_deportivo.actividad_nueva("Torneo 2vs2")
club_deportivo.actividad_nueva("Rugby")
club_deportivo.mostrar_actividades()

club_deportivo.registrar_socios("Changuito")
club_deportivo.registrar_socios("Benja")
club_deportivo.mostrar_socios()

club_deportivo.eliminar_socio("Changuito")
club_deportivo.buscar_socio("Benja")