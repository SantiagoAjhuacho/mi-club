from pathlib import Path
from base_datos.base_datoss import conectar, buscar_socio_por_usuario

# Ruta a la base de datos subiendo un nivel desde la carpeta servicios
RUTA_DB = Path(__file__).parent.parent / "club.db"


def autenticar(usuario, contrasenia):
    # Función para autenticar a un socio dado su usuario y contraseña.
    # 1. Abrir conexión a la base de datos
    conexion = conectar(str(RUTA_DB))

    # 2. Buscar al socio por usuario
    socio = buscar_socio_por_usuario(conexion, usuario)

    # 3. Cerrar la conexión inmediatamente
    conexion.close()

    # 4. Verificar si el socio no existe
    if socio is None:
        return None

    # 5. Comparar la contraseña ingresada con la guardada en el objeto Socio
    if socio.get_contrasenia() == contrasenia:
        return socio

    # 6. Si la contraseña no coincide, devuelve None
    return None