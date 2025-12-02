from tkinter import *
from tkinter import messagebox

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

        Button(ventana, text="1.- Autos", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)
        Button(ventana, text="2.- Camiones", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)
        Button(ventana, text="3.- Camionetas", command=lambda: Vista.menu_camionetas(ventana)).pack(pady=10)
        Button(ventana, text="4.- Salir", command=lambda: ventana.quit()).pack(pady=10)

    @staticmethod
    def menu_autos(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Menú de Autos ::..").pack()

        Button(ventana, text="Insertar", command=lambda: Vista.insertar_autos(ventana)).pack(pady=10)
        Button(ventana, text="Consultar", command=lambda: Vista.consultar_autos(ventana)).pack(pady=10)
        Button(ventana, text="Cambiar", command=lambda: Vista.cambiar_autos_pedir_id(ventana)).pack(pady=10)
        Button(ventana, text="Borrar", command=lambda: Vista.borrar_autos(ventana)).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_principal(ventana)).pack(pady=10)

    @staticmethod
    def insertar_autos(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Insertar Auto ::..").pack()

        for texto in ["Marca","Color","Modelo","Velocidad","Caballaje","Plazas"]:
            Label(ventana, text=texto).pack()
            Entry(ventana, width=15).pack(pady=5)

        Button(ventana, text="Guardar", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)

    @staticmethod
    def consultar_autos(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Consultar Autos ::..").pack()

        Label(ventana, text="Aquí irían los resultados").pack(pady=20)
        Button(ventana, text="Volver", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)

    @staticmethod
    def cambiar_autos_pedir_id(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Cambiar Auto ::..").pack()

        Label(ventana, text="ID del Auto").pack()
        id_entry = Entry(ventana, width=15)
        id_entry.pack(pady=5)

        Button(
            ventana,
            text="Continuar",
            command=lambda: Vista.cambiar_autos_form(ventana, id_entry.get())
        ).pack(pady=10)

        Button(ventana, text="Volver", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)

    @staticmethod
    def cambiar_autos_form(ventana, id_auto):
        Vista.borrarPantalla(ventana)
        Label(ventana, text=f"..:: Editando Auto ID {id_auto} ::..").pack(pady=10)

        for texto in ["Marca","Color","Modelo","Velocidad","Caballaje","Plazas"]:
            Label(ventana, text=texto).pack()
            Entry(ventana, width=15).pack(pady=5)

        Button(ventana, text="Guardar", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)

    @staticmethod
    def borrar_autos(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Borrar Auto ::..").pack()

        Label(ventana, text="ID a eliminar").pack()
        Entry(ventana, width=15).pack(pady=5)

        Button(ventana, text="Guardar", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)

    @staticmethod
    def menu_camiones(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Menú de Camiones ::..").pack()

        Button(ventana, text="Insertar", command=lambda: Vista.insertar_camiones(ventana)).pack(pady=10)
        Button(ventana, text="Consultar", command=lambda: Vista.consultar_camiones(ventana)).pack(pady=10)
        Button(ventana, text="Cambiar", command=lambda: Vista.cambiar_camiones_pedir_id(ventana)).pack(pady=10)
        Button(ventana, text="Borrar", command=lambda: Vista.borrar_camiones(ventana)).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_principal(ventana)).pack(pady=10)

    @staticmethod
    def insertar_camiones(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Insertar Camión ::..").pack()

        Label(ventana, text="Datos del camión").pack()
        Entry(ventana, width=15).pack(pady=5)

        Button(ventana, text="Guardar", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)

    @staticmethod
    def consultar_camiones(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Consultar Camiones ::..").pack()

        Label(ventana, text="Aquí irían los resultados").pack(pady=20)
        Button(ventana, text="Volver", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)

    @staticmethod
    def cambiar_camiones_pedir_id(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Cambiar Camión ::..").pack()

        Label(ventana, text="ID del camión").pack()
        id_entry = Entry(ventana, width=15)
        id_entry.pack(pady=5)

        Button(
            ventana,
            text="Continuar",
            command=lambda: Vista.cambiar_camiones_form(ventana, id_entry.get())
        ).pack(pady=10)

        Button(ventana, text="Volver", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)

    @staticmethod
    def cambiar_camiones_form(ventana, id_camion):
        Vista.borrarPantalla(ventana)
        Label(ventana, text=f"..:: Editando Camión ID {id_camion} ::..").pack(pady=10)

        for texto in ["Dato del camión"]:
            Label(ventana, text=texto).pack()
            Entry(ventana, width=15).pack(pady=5)

        Button(ventana, text="Guardar", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)

    @staticmethod
    def menu_camionetas(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Menú de Camionetas ::..").pack()

        Button(ventana, text="Insertar", command=lambda: Vista.insertar_camionetas(ventana)).pack(pady=10)
        Button(ventana, text="Consultar", command=lambda: Vista.consultar_camionetas(ventana)).pack(pady=10)
        Button(ventana, text="Cambiar", command=lambda: Vista.cambiar_camionetas_pedir_id(ventana)).pack(pady=10)
        Button(ventana, text="Borrar", command=lambda: Vista.borrar_camionetas(ventana)).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_principal(ventana)).pack(pady=10)

    @staticmethod
    def insertar_camionetas(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Insertar Camioneta ::..").pack()

        Label(ventana, text="Datos").pack()
        Entry(ventana, width=15).pack(pady=5)

        Button(ventana, text="Guardar", command=lambda: Vista.menu_camionetas(ventana)).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_camionetas(ventana)).pack(pady=10)

    @staticmethod
    def consultar_camionetas(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Consultar Camionetas ::..").pack()

        Label(ventana, text="Aquí irían los resultados").pack(pady=20)
        Button(ventana, text="Volver", command=lambda: Vista.menu_camionetas(ventana)).pack(pady=10)

    @staticmethod
    def cambiar_camionetas_pedir_id(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Cambiar Camioneta ::..").pack()

        Label(ventana, text="ID de la camioneta").pack()
        id_entry = Entry(ventana, width=15)
        id_entry.pack(pady=5)

        Button(
            ventana,
            text="Continuar",
            command=lambda: Vista.cambiar_camionetas_form(ventana, id_entry.get())
        ).pack(pady=10)

        Button(ventana, text="Volver", command=lambda: Vista.menu_camionetas(ventana)).pack(pady=10)

    @staticmethod
    def cambiar_camionetas_form(ventana, id_camioneta):
        Vista.borrarPantalla(ventana)
        Label(ventana, text=f"..:: Editando Camioneta ID {id_camioneta} ::..").pack(pady=10)

        for texto in ["Dato de la camioneta"]:
            Label(ventana, text=texto).pack()
            Entry(ventana, width=15).pack(pady=5)

        Button(ventana, text="Guardar", command=lambda: Vista.menu_camionetas(ventana)).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_camionetas(ventana)).pack(pady=10)

    @staticmethod
    def borrar_camionetas(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Borrar Camioneta ::..").pack()

        Label(ventana, text="ID a eliminar").pack()
        Entry(ventana, width=15).pack(pady=5)

        Button(ventana, text="Guardar", command=lambda: Vista.menu_camionetas(ventana)).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_camionetas(ventana)).pack(pady=10)