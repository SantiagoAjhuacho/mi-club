import sqlite3

def conectar(ruta):
    """Abre una conexión a la base de datos en la ruta indicada.
    Si el archivo no existe, lo crea automáticamente."""
    conexion = sqlite3.connect(ruta)
    return conexion

def crear_tablas(conexion):
    """Crea las tablas necesarias si no existen."""
    cursor = conexion.cursor()

    # Tabla 1: socios (la que ya tenías)
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

    # Tabla 2: cuotas (la nueva)
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

    conexion.commit()

def guardar_socio(conexion, socio):
    """Recibe un objeto Socio y lo guarda en la tabla socios."""
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO socios (nombre_completo, fecha_nacimiento, tipo_identificacion, identificacion, nacionalidad, fecha_inscripcion, estado, rol, usuario, contrasenia)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        socio.nombre_completo,
        socio.fecha_nacimiento,
        socio.get_tipo_identificacion(),
        socio.get_identificacion(),
        socio.get_nacionalidad(),
        socio.fecha_inscripcion,
        socio.estado,
        socio.rol,
        socio.get_usuario(),
        socio.get_contrasenia(),
    ))
    conexion.commit()