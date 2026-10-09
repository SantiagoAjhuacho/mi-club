import sqlite3
from datetime import date #date es para convertir las fechas de la BD a objetos date y viceversa
from modelo.socio import Socio
from modelo.cuota import Cuota
from modelo.club import Club
from modelo.actividad import Actividad


# Conectar a la base de datos.
# Abre (o crea si no existe) el archivo .db y devuelve la conexión.
def conectar(ruta):
    """Abre una conexión a la base de datos en la ruta indicada.
    Si el archivo no existe, lo crea automáticamente."""
    conexion = sqlite3.connect(ruta)
    return conexion


# Crear la tabla de socios.
# Tabla cuotas, con socio_id que referencia a socios.
# Tablas clubes, actividades y socio_actividad.
def crear_tablas(conexion):
    """Crea las tablas necesarias si no existen."""
    cursor = conexion.cursor()

    # Tabla socios 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo     TEXT NOT NULL,
            fecha_nacimiento    TEXT,
            tipo_identificacion TEXT,
            identificacion      TEXT,
            nacionalidad        TEXT,
            fecha_inscripcion   TEXT,
            estado              TEXT DEFAULT 'Activo',
            rol                 TEXT NOT NULL,
            usuario             TEXT UNIQUE NOT NULL,
            contrasenia         TEXT NOT NULL
        )
    """)

    # Tabla cuotas (BD II - Recap)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cuotas (
            id                INTEGER PRIMARY KEY AUTOINCREMENT,
            socio_id          INTEGER NOT NULL,
            periodo           TEXT NOT NULL,
            estado            TEXT DEFAULT 'Pendiente',
            fecha_vencimiento TEXT,
            FOREIGN KEY (socio_id) REFERENCES socios(id)
        )
    """)

    # Tabla clubes (BD II - Paso 2)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clubes (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre          TEXT NOT NULL,
            descripcion     TEXT,
            ubicacion       TEXT,
            presidente      TEXT,
            fecha_fundacion TEXT
        )
    """)

    # Tabla actividades (BD II - Paso 3): cada actividad pertenece a un club (club_id)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actividades (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre  TEXT NOT NULL,
            dia     TEXT,
            horario TEXT,
            club_id INTEGER,
            FOREIGN KEY (club_id) REFERENCES clubes(id)
        )
    """)

    # Tabla socio_actividad (BD II - Paso 4): relación muchos a muchos entre socios y actividades
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socio_actividad (
            socio_id INTEGER,
            actividad_id INTEGER,
            PRIMARY KEY (socio_id, actividad_id),
            FOREIGN KEY (socio_id) REFERENCES socios(id),
            FOREIGN KEY (actividad_id) REFERENCES actividades(id)
        )
    """)

    conexion.commit()


# Función para guardar un socio.
# Recibe un objeto Socio y lo inserta en la tabla socios (las fechas se guardan como texto con isoformat()).
def guardar_socio(conexion, socio):
    """Recibe un objeto Socio y lo guarda en la tabla socios."""
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO socios (nombre_completo, fecha_nacimiento, tipo_identificacion, identificacion, nacionalidad, fecha_inscripcion, estado, rol, usuario, contrasenia)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        socio.nombre_completo,
        socio.fecha_nacimiento.isoformat(),
        socio.get_tipo_identificacion(),
        socio.get_identificacion(),
        socio.get_nacionalidad(),
        socio.fecha_inscripcion.isoformat(),
        socio.estado,
        socio.rol,
        socio.get_usuario(),
        socio.get_contrasenia(),
    ))
    conexion.commit()


# Buscar un socio por usuario (sirve para el login).
# Devuelve el objeto Socio completo o None si no existe. El id de la BD se descarta con _id.
def buscar_socio_por_usuario(conexion, usuario):
    """Devuelve el objeto Socio con ese usuario, o None si no existe."""
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT id, nombre_completo, fecha_nacimiento, tipo_identificacion,
               identificacion, nacionalidad, fecha_inscripcion, estado, rol,
               usuario, contrasenia
        FROM socios WHERE usuario = ?
    """, (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return None

    (_id, nombre_completo, fecha_nacimiento, tipo_identificacion,
     identificacion, nacionalidad, fecha_inscripcion, estado, rol,
     usuario, contrasenia) = fila

    return Socio(
        nombre_completo,
        date.fromisoformat(fecha_nacimiento), #fromisoformat convierte el texto de la BD a un objeto date
        tipo_identificacion,
        identificacion,
        nacionalidad,
        date.fromisoformat(fecha_inscripcion), #fromisoformat convierte el texto de la BD a un objeto date
        rol,
        estado,
        usuario,
        contrasenia,
    )


# guardar_cuota(conexion, usuario, cuota): guarda una cuota para un socio.
# Busca el id del socio por su usuario y lo usa como socio_id en la tabla cuotas.
def guardar_cuota(conexion, usuario, cuota):
    """Guarda una cuota asociada al socio con ese usuario."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        raise ValueError("El socio no existe")
    socio_id = fila[0]

    cursor.execute("""
        INSERT INTO cuotas (socio_id, periodo, estado, fecha_vencimiento)
        VALUES (?, ?, ?, ?)
    """, (
        socio_id,
        cuota.periodo,
        cuota.get_estado(),
        cuota.fecha_de_vencimiento.isoformat(),
    ))
    conexion.commit()


#  lista las cuotas de un socio.
# Devuelve una lista de objetos Cuota (o una lista vacía si el socio no existe).
def listar_cuotas_de_socio(conexion, usuario):
    """Devuelve una lista de objetos Cuota para el socio con ese usuario."""
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return []
    socio_id = fila[0]

    cursor.execute(
        "SELECT periodo, estado, fecha_vencimiento FROM cuotas WHERE socio_id = ?",
        (socio_id,)
    )

    cuotas = []
    for periodo, estado, fecha_vencimiento in cursor.fetchall():
        cuota = Cuota(estado, date.fromisoformat(fecha_vencimiento), periodo)
        cuotas.append(cuota)
    return cuotas


# guardar_club(conexion, club).
# Guarda el club en la tabla clubes, solo si todavía no existe uno.
def guardar_club(conexion, club):
    """Guarda el club en la tabla clubes (solo si no existe uno)."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM clubes LIMIT 1")
    if cursor.fetchone() is not None:
        return
    cursor.execute("""
        INSERT INTO clubes (nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        VALUES (?, ?, ?, ?, ?)
    """, (
        club.nombre,
        club.descripcion,
        club.ubicacion,
        club.get_presidente(),
        club.get_fecha_fundacion().isoformat(),
    ))
    conexion.commit()


# guardar_actividad(conexion, actividad).
# Guarda la actividad en la tabla actividades y la vincula al club cargado (club_id).
def guardar_actividad(conexion, actividad):
    """Guarda una actividad en la tabla actividades, vinculada al club."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM clubes LIMIT 1")
    fila = cursor.fetchone()
    club_id = fila[0] if fila is not None else None

    cursor.execute("""
        INSERT INTO actividades (nombre, dia, horario, club_id)
        VALUES (?, ?, ?, ?)
    """, (actividad.nombre, actividad.dia, actividad.horario, club_id))
    conexion.commit()


# anotar_socio_actividad(conexion, usuario, nombre_actividad).
# Anota al socio en la actividad (INSERT OR IGNORE evita duplicados).
def anotar_socio_actividad(conexion, usuario, nombre_actividad):
    """Anota al socio en la actividad indicada."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return "El socio no existe."
    socio_id = fila[0]

    cursor.execute("SELECT id FROM actividades WHERE nombre = ?",
                   (nombre_actividad,))
    fila = cursor.fetchone()
    if fila is None:
        return f"La actividad {nombre_actividad} no existe."
    actividad_id = fila[0]

    cursor.execute(
        "INSERT OR IGNORE INTO socio_actividad (socio_id, actividad_id) VALUES (?, ?)",
        (socio_id, actividad_id)
    )
    conexion.commit()
    return f"Te anotaste en {nombre_actividad}."


# desanotar_socio_actividad(conexion, usuario, nombre_actividad).
# Saca al socio de la actividad (borra la fila de socio_actividad).
def desanotar_socio_actividad(conexion, usuario, nombre_actividad):
    """Saca al socio de la actividad indicada."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return "El socio no existe."
    socio_id = fila[0]

    cursor.execute("SELECT id FROM actividades WHERE nombre = ?",
                   (nombre_actividad,))
    fila = cursor.fetchone()
    if fila is None:
        return f"La actividad {nombre_actividad} no existe."
    actividad_id = fila[0]

    cursor.execute(
        "DELETE FROM socio_actividad WHERE socio_id = ? AND actividad_id = ?",
        (socio_id, actividad_id)
    )
    conexion.commit()
    return f"Te desanotaste de {nombre_actividad}."


# listar_actividades_de_socio(conexion, usuario).
# Usa JOIN para juntar actividades con socio_actividad y devuelve una lista de objetos Actividad.
def listar_actividades_de_socio(conexion, usuario):
    """Devuelve una lista de objetos Actividad del socio con ese usuario."""
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT a.nombre, a.dia, a.horario
        FROM actividades a
        JOIN socio_actividad sa ON sa.actividad_id = a.id
        JOIN socios s ON s.id = sa.socio_id
        WHERE s.usuario = ?
    """, (usuario,))

    actividades = []
    for nombre, dia, horario in cursor.fetchall():
        actividades.append(Actividad(nombre, dia, horario))
    return actividades


#Paso 8: obtener_club(conexion).
# Devuelve el objeto Club o None si no hay club cargado.
def obtener_club(conexion):
    """Devuelve el objeto Club o None si no hay club cargado."""
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, descripcion, ubicacion, presidente, fecha_fundacion FROM clubes LIMIT 1")
    fila = cursor.fetchone()
    if fila is None:
        return None
    nombre, descripcion, ubicacion, presidente, fecha_fundacion = fila
    return Club(nombre, descripcion, ubicacion, presidente, date.fromisoformat(fecha_fundacion))