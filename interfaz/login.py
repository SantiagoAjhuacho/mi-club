import tkinter as tk
# tkinter es la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). Se importa como tk para simplificar el acceso a sus clases y funciones.

from tkinter import ttk, messagebox
# ttk proporciona widgets con mejor apariencia y soporte de temas visuales. messagebox se importa para mostrar ventanas emergentes de alerta y error al usuario.

from servicios.servicio_autenticacion import autenticar
# Esto importa la función autenticar desde el módulo servicio_autenticacion, que verifica las credenciales del usuario contra la base de datos sin hacer SQL directo.

from interfaz.panel_socio import PanelSocio
# Esto importa la clase PanelSocio desde el módulo panel_socio, que representa la ventana principal para los socios tras iniciar sesión.

from interfaz.panel_admin import PanelAdmin
# Importa la clase PanelAdmin desde el módulo panel_admin, que representa la ventana principal de gestión para los administradores.


class VentanaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Mi Club - Lakers Edition")
        self.geometry("380x320")
        # geometry establece el tamaño de la ventana en 380 píxeles de ancho por 320 píxeles de alto.
        
        self.resizable(False, False)
        # resizable(False, False) evita que el usuario pueda cambiar el tamaño de la ventana, manteniéndola fija.

        # Paleta de colores oficiales de Los Angeles Lakers
        COLOR_PURPLE = "#552583"  # Morado Lakers principal
        COLOR_GOLD = "#FDB927"    # Dorado Lakers para letras y detalles
        COLOR_WHITE = "#FFFFFF"   # Blanco para textos de etiquetas

        # Fondo principal de la ventana configurado en morado
        self.configure(bg=COLOR_PURPLE)

        # Configuración de estilos personalizados con TTK para aplicar los colores del club
        style = ttk.Style(self)
        style.theme_use("clam")  # Permite modificar los colores de fondo y frente de los botones en TTK

        # Estilo para marcos y etiquetas
        style.configure("Lakers.TFrame", background=COLOR_PURPLE)
        style.configure("LakersTitle.TLabel", background=COLOR_PURPLE, foreground=COLOR_GOLD, font=("Arial", 16, "bold"))
        style.configure("LakersText.TLabel", background=COLOR_PURPLE, foreground=COLOR_WHITE, font=("Arial", 10, "bold"))

        # Estilo para el botón dorado con letras moradas
        style.configure("Lakers.TButton",
                        background=COLOR_GOLD,
                        foreground=COLOR_PURPLE,
                        font=("Arial", 11, "bold"),
                        borderwidth=0,
                        focusthickness=3)
        # Se cambia el color al pasar el cursor o hacer clic sobre el botón
        style.map("Lakers.TButton",
                  background=[("active", "#E0A220")],
                  foreground=[("active", COLOR_PURPLE)])


        # Marco contenedor del formulario de ingreso
        frame = ttk.Frame(self, style="Lakers.TFrame", padding=15)
        frame.pack(fill="both", expand=True)
        # frame crea un marco contenedor con relleno interno. fill="both" y expand=True hacen que ocupe todo el espacio disponible.

        # Campo Usuario
        ttk.Label(frame, text="Usuario:", style="LakersText.TLabel").pack(anchor="w", pady=(5, 2))
        self.entry_usuario = tk.Entry(
            frame,
            bg="#2D1348",               # Fondo morado oscuro para las cajas de entrada
            fg=COLOR_GOLD,              # Texto ingresado en dorado
            insertbackground=COLOR_GOLD, # Cursor del texto en dorado
            font=("Arial", 11),
            relief="flat",
            bd=5
        )
        self.entry_usuario.pack(fill="x", pady=(0, 10))
        self.entry_usuario.focus()
        # .focus() coloca automáticamente el cursor en el campo de usuario apenas abre la ventana.

        # Campo Contraseña
        ttk.Label(frame, text="Contraseña:", style="LakersText.TLabel").pack(anchor="w", pady=(5, 2))
        self.entry_contrasenia = tk.Entry(
            frame,
            show="*",                   # show="*" oculta los caracteres tipeados para proteger la clave
            bg="#2D1348",
            fg=COLOR_GOLD,
            insertbackground=COLOR_GOLD,
            font=("Arial", 11),
            relief="flat",
            bd=5
        )
        self.entry_contrasenia.pack(fill="x", pady=(0, 15))

        # Botón Ingresar
        btn_ingresar = ttk.Button(frame, text="INGRESAR", style="Lakers.TButton", command=self.iniciar_sesion)
        btn_ingresar.pack(fill="x", pady=10)

        # Atajo Tecla Enter
        self.bind('<Return>', lambda event: self.iniciar_sesion())
        # lambda event: self.iniciar_sesion() es una función anónima que permite ejecutar iniciar_sesion() al presionar Enter.

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get().strip()
        # .get() obtiene el texto ingresado y .strip() elimina espacios en blanco al inicio o al final.
        contrasenia = self.entry_contrasenia.get().strip()
        # Obtiene el texto de la clave y elimina espacios en blanco innecesarios.

        # 1. Validar campos vacíos
        if not usuario or not contrasenia:
            messagebox.showwarning("Atención", "Debe completar todos los campos.")
            return

        # 2. Llamar al servicio de autenticación (sin hacer SQL directo en la interfaz)
        socio = autenticar(usuario, contrasenia)

        # 3. Validar resultado de la autenticación
        if socio is None:
            messagebox.showerror("Error de Autenticación", "Usuario o contraseña incorrectos.")
            return

        # 4. Ocultar la ventana de login
        self.withdraw()
        # self.withdraw() oculta la ventana principal de login sin destruirla por completo en memoria.

        # 5. Abrir el panel según el rol del socio
        if socio.rol.lower() == "admin":
            PanelAdmin(self, socio)
        else:
            PanelSocio(self, socio)