import tkinter as tk
from tkinter import ttk


class PanelSocio(tk.Toplevel):
    def __init__(self, master, socio):
        super().__init__(master)
        self.title("Panel del Socio")
        self.geometry("400x300")
        self.socio = socio

        # Al cerrar el panel con la 'X', cierra toda la aplicación
        self.protocol("WM_DELETE_WINDOW", master.destroy)
        #wm_delete_window es un protocolo de eventos en Tkinter que se activa cuando el usuario intenta cerrar la ventana. Al establecerlo en master.destroy, se asegura que al cerrar el panel del socio, también se cierre la ventana principal de la aplicación.

        ttk.Label(self, text=f"Bienvenido/a: {socio.nombre_completo}", font=("Arial", 12, "bold")).pack(pady=20)
        ttk.Label(self, text=f"Usuario: {socio.get_usuario()}").pack(pady=5)
        ttk.Label(self, text=f"Estado: {socio.estado}").pack(pady=5)
        ttk.Label(self, text=f"Rol: {socio.rol}").pack(pady=5)

        ttk.Button(self, text="Cerrar", command=master.destroy).pack(pady=20)