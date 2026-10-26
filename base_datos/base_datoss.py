import sqlite3 # el módulo sqlite3 es parte de la librería estándar de Python y permite trabajar con bases de datos SQLite
from datetime import date #el datetime lo uso y lo importo aca ya que me sirve para convertir de string a date y viceversa, y lo uso en varias funciones de este archivo
from modelo.socio import Socio
from modelo.cuota import Cuota
from modelo.club import Club
from modelo.actividad import Actividad


def conectar(ruta):
    #Conecta a la base de datos SQLite en la ruta especificada. Si el archivo no existe, lo crea automáticamente.
    conexion = sqlite3.connect(ruta)
    return conexion


def crear_tablas(conexion):
    """Crea las tablas necesarias si no existen."""
    cursor = conexion.cursor()

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

    # Paso 2 - Tabla de clubes
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

    # Paso 3 - Tabla de actividades
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

    # Paso 4 - Tabla socio_actividad (muchos a muchos)
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


# Paso 1 - Buscar un socio por usuario (sirve para el login)
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
        date.fromisoformat(fecha_nacimiento),
        tipo_identificacion,
        identificacion,
        nacionalidad,
        date.fromisoformat(fecha_inscripcion),
        rol,
        estado,
        usuario,
        contrasenia,
    )


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


# Paso 5 - Funciones de club y actividades
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


# Paso 6 - Anotarse y desanotarse
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


# Paso 7 - Listar actividades de un socio
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


# Paso 8 - Obtener el club
def obtener_club(conexion):
    """Devuelve el objeto Club o None si no hay club cargado."""
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, descripcion, ubicacion, presidente, fecha_fundacion FROM clubes LIMIT 1")
    fila = cursor.fetchone()
    if fila is None:
        return None
    nombre, descripcion, ubicacion, presidente, fecha_fundacion = fila
    return Club(nombre, descripcion, ubicacion, presidente, date.fromisoformat(fecha_fundacion))

    # ==========================================
#  SQLITE 1.3 - MODIFICACIONES Y BAJAS
# ==========================================

def actualizar_estado_cuota(conexion, usuario, periodo, nuevo_estado):
    """Actualiza el estado de la cuota de un socio para un período específico."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return "El socio no existe."
    socio_id = fila[0]

    cursor.execute("""
        UPDATE cuotas
        SET estado = ?
        WHERE socio_id = ? AND periodo = ?
    """, (nuevo_estado, socio_id, periodo))
    
    if cursor.rowcount == 0:
        return f"No se encontró la cuota del período '{periodo}'."
    
    conexion.commit()
    return f"Cuota del período '{periodo}' actualizada a '{nuevo_estado}'."


def cambiar_estado_socio(conexion, usuario, nuevo_estado):
    """Cambia el estado del socio ('Activo' / 'Suspendido')."""
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE socios
        SET estado = ?
        WHERE usuario = ?
    """, (nuevo_estado, usuario))
    
    if cursor.rowcount == 0:
        return "El socio no existe."
        
    conexion.commit()
    return f"Estado del socio '{usuario}' cambiado a '{nuevo_estado}'."


def actualizar_contrasenia_socio(conexion, usuario, nueva_contrasenia):
    """Actualiza la contraseña de acceso de un socio."""
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE socios
        SET contrasenia = ?
        WHERE usuario = ?
    """, (nueva_contrasenia, usuario))
    
    if cursor.rowcount == 0:
        return "El socio no existe."
        
    conexion.commit()
    return f"Contraseña actualizada para '{usuario}'."


def eliminar_socio(conexion, usuario):
    #Elimina un socio y todos sus datos asociados (cuotas, actividades).
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return "El socio no existe."
    socio_id = fila[0]

    # Mantiene la integridad referencial borrando datos relacionados
    cursor.execute("DELETE FROM socio_actividad WHERE socio_id = ?", (socio_id,))
    cursor.execute("DELETE FROM cuotas WHERE socio_id = ?", (socio_id,))
    cursor.execute("DELETE FROM socios WHERE id = ?", (socio_id,))
    
    conexion.commit()
    return f"Socio '{usuario}' y sus datos asociados fueron eliminados de la BD."