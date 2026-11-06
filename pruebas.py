from datetime import date
from pathlib import Path

# Importaciones de la base de datos
from base_datos.base_datoss import (
    conectar,
    crear_tablas,
    guardar_socio,
    buscar_socio_por_usuario,
    guardar_cuota,
    listar_cuotas_de_socio,
    guardar_club,
    obtener_club,
    guardar_actividad,
    anotar_socio_actividad,
    desanotar_socio_actividad,
    listar_actividades_de_socio,
    # SQLite 1.3 - Modificaciones y Bajas
    actualizar_estado_cuota,
    cambiar_estado_socio,
    actualizar_contrasenia_socio,
    eliminar_socio,
)

# Importaciones del modelo
from modelo.socio import Socio
from modelo.cuota import Cuota
from modelo.club import Club
from modelo.actividad import Actividad

# Ruta del archivo de base de datos
RUTA = Path(__file__).parent / "club.db"

# 1. Conectar y crear tablas
conexion = conectar(str(RUTA))
crear_tablas(conexion)

# 2. Guardar y buscar socio
if buscar_socio_por_usuario(conexion, "carlosramirez") is None:
    carlos = Socio(
        #"Carlitos Ramirez", date(1993, 5, 10), "DNI", "40322775", "Argentina",
        #date(2026, 1, 1), "socio", "Activo", "carlosramirez", "clave111"
        "Santiago Ajhuacho", date(2000, 9, 20), "DNI", "49761707", "Argentina",
        date(2026, 1, 1), "socio", "Activo", "sanemogi", "santiago2009"
    )
    guardar_socio(conexion, carlos)
    #aca en guadar_socio se guarda el socio en la base de datos, y si no existe un socio con el usuario "carlosramirez", se crea uno nuevo con los datos proporcionados. En este caso, se está creando un socio llamado "Santiago Ajhuacho" con el usuario "sanemogi" y la contraseña "2009san".
    print("Socio guardado.")

#socio = buscar_socio_por_usuario(conexion, "carlosramirez")
#print("Socio encontrado:", socio)

socio = buscar_socio_por_usuario(conexion, "sanemogi")
print("Socio encontrado:", socio)

# 3. Guardar y listar cuotas
#guardar_cuota(conexion, "carlosramirez", Cuota("Pendiente", date(2026, 11, 30), "Noviembre 2026"))
#for cuota in listar_cuotas_de_socio(conexion, "carlosramirez"):
#    print("Cuota:", cuota.periodo, cuota.get_estado())

guardar_cuota(conexion, "sanemogi", Cuota("Pendiente", date(2026, 11, 30), "Noviembre 2026"))
for cuota in listar_cuotas_de_socio(conexion, "sanemogi"):
    print("Cuota:", cuota.periodo, cuota.get_estado())

# 4. Guardar y obtener club
guardar_club(conexion, Club("Instituto Deportivo de la Gloria", "Club de deportes",
                            "Parque de los Patricios", "Talislao Zen", date(1960, 8, 3)))
club = obtener_club(conexion)
if club:
    print("Club:", club.nombre, "-", club.calcular_antiguedad(), "años")

# 5. Guardar actividades y gestionar relaciones
guardar_actividad(conexion, Actividad("Futbol", "Lunes", "18:00"))
guardar_actividad(conexion, Actividad("Handball", "Martes", "19:00"))

#print(anotar_socio_actividad(conexion, "carlosramirez", "Futbol"))

print(anotar_socio_actividad(conexion, "sanemogi", "Futbol"))

#for act in listar_actividades_de_socio(conexion, "carlosramirez"):
#    print("Actividad inscrita:", act.obtener_informacion())

for act in listar_actividades_de_socio(conexion, "sanemogi"):
    print("Actividad inscrita:", act.obtener_informacion())

# 6. --- PRUEBAS SQLITE 1.3 (Modificaciones y Bajas) ---
print("\n--- Pruebas SQLite 1.3 ---")
#la /n sirve para separar la salida en la consola y hacerla más legible

# Actualizar estado de cuota
#print(actualizar_estado_cuota(conexion, "carlosramirez", "Noviembre 2026", "Pagada"))

print(actualizar_estado_cuota(conexion, "sanemogi", "Noviembre 2026", "Pagada"))

# Cambiar estado del socio a Suspendido
#print(cambiar_estado_socio(conexion, "carlosramirez", "Suspendido"))

print(cambiar_estado_socio(conexion, "sanemogi", "Suspendido"))


# Actualizar contraseña del socio
#print(actualizar_contrasenia_socio(conexion, "carlosramirez", "nuevaClave2026"))

print(actualizar_contrasenia_socio(conexion, "sanemogi", "2009san"))

# Eliminar socio y sus datos relacionados
#print(eliminar_socio(conexion, "carlosramirez"))

#print(eliminar_socio(conexion, "sanemogi"))

# Cerrar la conexión
conexion.close()