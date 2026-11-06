import tkinter as tk
from tkinter import ttk


class PanelAdmin(tk.Toplevel):
    def __init__(self, master, socio):
        super().__init__(master)
        self.title("Panel del Administrador")
        self.geometry("400x300")
        self.socio = socio

        # Al cerrar el panel con la 'X', cierra toda la aplicación
        self.protocol("WM_DELETE_WINDOW", master.destroy)

        ttk.Label(self, text=f"Administrador: {socio.nombre_completo}", font=("Arial", 12, "bold")).pack(pady=20)
        ttk.Label(self, text="Panel de gestión de socios").pack(pady=10)

        ttk.Button(self, text="Cerrar", command=master.destroy).pack(pady=20)