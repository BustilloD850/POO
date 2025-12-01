from tkinter import *
from tkinter import messagebox
from controller import funciones
from model import autos,camiones,camionetas

class Vista:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.title("Gestion de Autos")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        Vista.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: Menú Principal ::..", justify=CENTER)
        lbl_titulo.pack()

        btn_autos=Button(ventana, text="1.- Autos", command= lambda: Vista.menu_autos(ventana,"Autos"))
        btn_autos.pack(pady=10)
        btn_camoines=Button(ventana, text="2.- Camiones", command= lambda: Vista.menu_autos(ventana,"Camiones"))
        btn_camoines.pack(pady=10)
        btn_camionetas=Button(ventana, text="3.- Camionetas", command= lambda: Vista.menu_autos(ventana,"Camionetas"))
        btn_camionetas.pack(pady=10)
        btn_salir=Button(ventana, text="4.- Salir", command= lambda: ventana.quit())
        btn_salir.pack(pady=10)
    
    @staticmethod
    def menu_autos(ventana,tipo):
        Vista.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"..:: Menú de {tipo} ::..", justify=CENTER)
        lbl_titulo.pack()

        btn_autos=Button(ventana, text="1.- Insertar", command= lambda: Vista.insertar_autos(ventana,tipo))
        btn_autos.pack(pady=10)
        btn_camoines=Button(ventana, text="2.- Consultar", command= lambda: Vista.consultar_autos(ventana,tipo))
        btn_camoines.pack(pady=10)
        btn_camionetas=Button(ventana, text="3.- Cambiar", command= lambda: Vista.cambiar_autos(ventana,tipo))
        btn_camionetas.pack(pady=10)
        btn_camionetas=Button(ventana, text="3.- Borrar", command= lambda: Vista.borrar_autos(ventana,tipo))
        btn_camionetas.pack(pady=10)
        btn_volver=Button(ventana, text="4.- Volver", command= lambda: Vista.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def insertar_autos(ventana,tipo):
        Vista.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"..:: Insertar {tipo} ::..", justify=CENTER)
        lbl_titulo.pack()

        btn_volver=Button(ventana, text="4.- Volver", command= lambda: Vista.menu_autos(ventana,tipo))
        btn_volver.pack(pady=10)

    @staticmethod
    def consultar_autos(ventana,tipo):
        Vista.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"..:: Consultar {tipo} ::..", justify=CENTER)
        lbl_titulo.pack()

        btn_volver=Button(ventana, text="4.- Volver", command= lambda: Vista.menu_autos(ventana,tipo))
        btn_volver.pack(pady=10)

    @staticmethod
    def cambiar_autos(ventana, tipo):
        Vista.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"..:: Cambiar {tipo} ::..", justify=CENTER)
        lbl_titulo.pack()

        btn_volver=Button(ventana, text="4.- Volver", command= lambda: Vista.menu_autos(ventana,tipo))
        btn_volver.pack(pady=10)
    
    @staticmethod
    def borrar_autos(ventana,tipo):
        Vista.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"..:: Eliminar {tipo} ::..", justify=CENTER)
        lbl_titulo.pack()

        btn_volver=Button(ventana, text="4.- Volver", command= lambda: Vista.menu_autos(ventana,tipo))
        btn_volver.pack(pady=10)