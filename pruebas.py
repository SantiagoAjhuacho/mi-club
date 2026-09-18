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

## --- Pruebas Clase Club ---
#club = Club("Instituto Deportivo de la gloria", "Establecimiento de deportes","Parque de los Patricios", "Talislao Zen", datetime(1876, 8, 3))
#print("Antigüedad del club:", club.calcular_antiguedad())
#print("¿Es institución histórica?:", club.es_institucion_historica())
#print("Info del club:", club.obtener_info())

#club.set_presidente("Nuevo Presidente")
#print("Presidente actualizado:", club.get_presidente())

## --- Pruebas Clase Actividad ---
#actividad1 = Actividad("Voley", "Lunes", "18:00 a 20:00")
#print("Info de la actividad:", actividad1.obtener_informacion())

## --- Pruebas de estado del Socio ---
#socio1.suspender()
#print("Estado tras suspender:", socio1.estado)
#socio1.reactivar()
#print("Estado tras reactivar:", socio1.estado)


## --- Pruebas de autenticación ---
#print("¿Login correcto?:", socio1.iniciar_sesion("juanperez", "pass123"))
#print("¿Contraseña actualizada?:", socio1.actualizar_contrasenia("pass123", "nueva_pass"))

"""Prueba de la capa de base de datos."""
from datetime import date
from pathlib import Path
from base_datos.base_datoss import conectar, crear_tablas, guardar_socio
from modelo.socio import Socio
import sqlite3

RUTA = Path(__file__).parent / "club.db"


conexion = conectar(str(RUTA))
crear_tablas(conexion)


carlos = Socio(
    "Carlos Ramos ", 30, "DNI", "40322345", "Argentina",
    date(2026, 1, 1), "Activo", "carlos", "clave123"
)
guardar_socio(conexion, carlos)
print("Socio guardado.")

conexion.close()
