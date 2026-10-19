#from datetime import datetime
#from modelo.persona import Persona
#from modelo.socio import Socio
#from modelo.cuota import Cuota
#from modelo.club import Club
#from modelo.actividad import Actividad

## --- Pruebas Clase Persona ---
#persona1 = Persona("Santiago Ariel", datetime(2000, 3, 15), "DNI", "34567890", "Argentina")
#print("¿Es mayor de edad?:", persona1.es_mayor_de_edad())
#print("¿Identificación válida?:", persona1.validar_identificacion())

## --- Pruebas Clase Socio (hereda de Persona + rol) ---
#socio1 = Socio("Juan Pérez", datetime(1994, 5, 20), "DNI", "12345678", "Argentina","01/01/2020", usuario="juanperez", contrasenia="pass123", rol="socio")
#print("¿Socio1 es admin?:", socio1.es_admin())

#admin1 = Socio("Ana Gómez", datetime(1985, 2, 10), "DNI", "11223344", "Argentina","01/01/2018", usuario="admin", contrasenia="admin123", rol="admin")
#print("¿Admin1 es admin?:", admin1.es_admin())

## --- Pruebas Clase Cuota ---
#cuota_julio = Cuota("pendiente", datetime(2024, 7, 31), "Cuota Julio 2024")
#socio1.generar_cuota(cuota_julio)
#print("Cuotas pendientes:", socio1.cantidad_cuotas_pendientes())
#print("¿Pago registrado?:", socio1.registrar_pago_cuota("Cuota Julio 2024"))
#print("¿Tiene deudas?:", socio1.tiene_deudas())

from datetime import date
from base_datos.base_datoss import (
    conectar, crear_tablas, guardar_socio, buscar_socio_por_usuario,
    guardar_cuota, listar_cuotas_de_socio, guardar_club, obtener_club,
    guardar_actividad, anotar_socio_actividad, desanotar_socio_actividad,
    listar_actividades_de_socio,
)
from modelo.socio import Socio
from modelo.cuota import Cuota
from modelo.club import Club
from modelo.actividad import Actividad

RUTA = "club.db"

conexion = conectar(RUTA)
crear_tablas(conexion)

# Consigna I: guardar un socio
# (con el if, no se rompe el codigo ya que si ya existe el socio no se vuelve a guardar)
if buscar_socio_por_usuario(conexion, "carlosramirez") is None:
    carlos = Socio(
        "Carlitos Ramirez", date(1993, 5, 10), "DNI", "40322775", "Argentina",
        date(2026, 1, 1), "socio", "Activo", "carlosramirez", "clave111"
    )
    guardar_socio(conexion, carlos)
    print("Socio guardado.")

#  Consigna II, Paso 1: buscar socio por usuario 
print("Socio encontrado:", buscar_socio_por_usuario(conexion, "carlosramirez"))
print("Usuario inexistente:", buscar_socio_por_usuario(conexion, "nadie"))

# Cuotas (consigna anterior) 
guardar_cuota(conexion, "carlosramirez", Cuota("Pendiente", date(2026, 11, 30), "Noviembre 2026"))
for c in listar_cuotas_de_socio(conexion, "carlosramirez"):
    print("Cuota:", c.periodo, c.get_estado())

#Consigna II, Pasos 5 y 8: club
guardar_club(conexion, Club("Instituto Deportivo de la Gloria", "Club de deportes","Parque de los Patricios", "Talislao Zen", date(1960, 8, 3)))
club = obtener_club(conexion)
print("Club:", club.nombre, "-", club.calcular_antiguedad(), "años")

#Consigna II, Pasos 5, 6 y 7: actividades
guardar_actividad(conexion, Actividad("Futbol", "Lunes", "18:00"))
guardar_actividad(conexion, Actividad("Handball", "Martes", "19:00"))
print(anotar_socio_actividad(conexion, "carlosramirez", "Futbol"))
print(anotar_socio_actividad(conexion, "nadie", "Futbol"))
print(anotar_socio_actividad(conexion, "carlosramirez", "Ajedrez"))
for a in listar_actividades_de_socio(conexion, "carlosramirez"):
    print("Actividad:", a.obtener_informacion())
print(desanotar_socio_actividad(conexion, "carlosramirez", "Futbol"))
print("Actividades tras desanotar:", len(listar_actividades_de_socio(conexion, "carlosramirez")))

conexion.close()