from club import Club

class ClubCategoria(Club):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []
        self.actividades = []

    def socios (self):
        return self.__socios


    def set_socios (self, socios):
        self.__socios = socios

    def agregar_socio(self, socio):
        self.__socios.append(socio)
    
    def mostrar_socios(self):
        if not self.__socios:
            print("No hay socios registrados.")
            return print("· Lista de Socios: ")
        for socio in self.__socios:
            print(f"Socio: {socio}")

    def agregar_actividad(self, actividad):
        self.__actividades.append(actividad)

    def mostrar_socio(self):
        for i in self.__socio:
            print(i)
    
    def mostrar(self):
        print("Nombre:  ", self.nombre)
        print("Descripcion: ", self.descripcion)
        print("Ubicacion:   ", self.ubicacion)
        print("Presidente:  ", self.__presidente)
        print("Fecha De Fundacion:  ", self.__fecha_fundacion)
        
#1)Incorporar la funcionalidad para registrar nuevos socios dentro de la categoría correspondiente.

    def registrar_socios(self,socio):
        self.__socios.append(socio)

#2)Permitir eliminar socios de la categoría cuando estos dejen de pertenecer a ella.

    def eliminar_socio(self, socio):
        if socio in self.__socios:
            self.__socios.remove(socio)
            print(f"Socio '{socio}' eliminado con éxito.")
        else:
            print(f"El socio '{socio}' no se encontró.")

#3)Implementar una búsqueda que permita localizar rápidamente un socio utilizando algún dato identificatorio.

    def buscar_socio(self, nombre_socio):
        for socio in self.__socios:
            if socio == nombre_socio:
                print(f"Se a encontrado al socio {socio} está registrado en la suigiente categoria.")

#4)Obtener la cantidad total de socios registrados en la categoría.

    def cantidad_socio(self):
        return len(self.__socios)

#5)Permitir agregar nuevas actividades deportivas, recreativas o culturales ofrecidas por el club. Permitir el

    def actividad_nueva(self,actividad):
        self.actividades.append(actividad)
        print("agregando actividades nuevas")

#6)Permitir eliminar actividades que ya no se encuentren disponibles.

    def eliminar_actividad(self, actividad):
        if actividad in self.actividades:
            self.actividades.remove(actividad)
            print(f"Actividad '{actividad}' se a eliminado por completo")

#7)Mostrar un listado completo de las actividades que se realizan en la categoría.
    def mostrar_actividades(self):
        for i in self.actividades:
            print(i)



club_deportivo = ClubCategoria("VoleyBall", "cancha Voley 18x9 metros", "Polideportivo Benito Quinquela Martín", "Gaston", "9/12/2000")


club_deportivo.actividad_nueva("actividad Torneo 2vs2")
club_deportivo.actividad_nueva("actividad de Rugby")

club_deportivo.mostrar_actividades()


club_deportivo.agregar_socio("Changuito")
club_deportivo.agregar_socio("Benja")
club_deportivo.agregar_socio("Wuelco")


club_deportivo.mostrar_socios()


club_deportivo.eliminar_socio("Changote")
club_deportivo.eliminar_socio("Changuito")


club_deportivo.buscar_socio("Facu")