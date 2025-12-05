from tkinter import *
from tkinter import messagebox
from controller.funciones import funciones

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

        lbl_marca = Label(ventana, text="Marca")
        lbl_marca.pack()
        marca = StringVar()
        Entry(ventana, textvariable=marca, width=15).pack(pady=5)

        lbl_color = Label(ventana, text="Color")
        lbl_color.pack()
        color = StringVar()
        Entry(ventana, textvariable=color, width=15).pack(pady=5)

        lbl_modelo = Label(ventana, text="Modelo")
        lbl_modelo.pack()
        modelo = IntVar()
        Entry(ventana, textvariable=modelo, width=15).pack(pady=5)

        lbl_velo = Label(ventana, text="Velocidad")
        lbl_velo.pack()
        velocidad = IntVar()
        Entry(ventana, textvariable=velocidad, width=15).pack(pady=5)

        lbl_caba = Label(ventana, text="Caballaje")
        lbl_caba.pack()
        caballaje = IntVar()
        Entry(ventana, textvariable=caballaje, width=15).pack(pady=5)

        lbl_plaza = Label(ventana, text="Plazas")
        lbl_plaza.pack()
        plazas = IntVar()
        Entry(ventana, textvariable=plazas, width=15).pack(pady=5)


        def guardar():
            auto = funciones.Autos(
                marca.get(),
                color.get(),
                modelo.get(),
                velocidad.get(),
                caballaje.get(),
                plazas.get()
            )

            if auto.insertar():
                messagebox.showinfo("Éxito", "Auto guardado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el auto.")


        Button(ventana, text="Guardar", command=guardar).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)

    @staticmethod
    def consultar_autos(ventana):

        Vista.borrarPantalla(ventana)

        Label(ventana, text="..:: Autos Registrados ::..").pack(pady=10)

        autos = funciones.Autos.consultar()

        if not autos:
            Label(ventana, text="No hay autos registrados.").pack(pady=10)
        else:
            for auto in autos:
                texto = f"""
    ID: {auto[0]}  
    Marca: {auto[1]}  
    Color: {auto[2]}  
    Modelo: {auto[3]}  
    Velocidad: {auto[4]}  
    Caballaje: {auto[5]}  
    Plazas: {auto[6]}
    """
                Label(ventana, text=texto, justify=LEFT, anchor="w").pack()

        Button(ventana, text="Volver", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)

    @staticmethod
    def cambiar_autos_pedir_id(ventana):
        Vista.borrarPantalla(ventana)

        Label(ventana, text="..:: Cambiar Auto ::..").pack()
        Label(ventana, text="Ingrese el ID del auto a modificar:").pack()

        id_var = IntVar()
        Entry(ventana, textvariable=id_var, width=15).pack(pady=5)

        def buscar():
            datos = funciones.Autos.consultar()

            for auto in datos:
                if auto[0] == id_var.get():
                    Vista.cambiar_autos_formulario(ventana, auto)
                    return

            messagebox.showerror("Error", "No existe un auto con ese ID.")

        Button(ventana, text="Buscar", command=buscar).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)

    @staticmethod
    def cambiar_autos_formulario(ventana, datos_auto):
        Vista.borrarPantalla(ventana)

        Label(ventana, text="..:: Modificar Auto ::..").pack()

        id_auto = datos_auto[0]

        Label(ventana, text="Marca").pack()
        marca = StringVar(value=datos_auto[1])
        Entry(ventana, textvariable=marca, width=15).pack(pady=5)

        Label(ventana, text="Color").pack()
        color = StringVar(value=datos_auto[2])
        Entry(ventana, textvariable=color, width=15).pack(pady=5)

        Label(ventana, text="Modelo").pack()
        modelo = IntVar(value=datos_auto[3])
        Entry(ventana, textvariable=modelo, width=15).pack(pady=5)

        Label(ventana, text="Velocidad").pack()
        velocidad = IntVar(value=datos_auto[4])
        Entry(ventana, textvariable=velocidad, width=15).pack(pady=5)

        Label(ventana, text="Caballaje").pack()
        caballaje = IntVar(value=datos_auto[5])
        Entry(ventana, textvariable=caballaje, width=15).pack(pady=5)

        Label(ventana, text="Plazas").pack()
        plazas = IntVar(value=datos_auto[6])
        Entry(ventana, textvariable=plazas, width=15).pack(pady=5)

        def guardar_cambios():
            from controller.funciones import funciones

            ok = funciones.Autos.actualizar(
                marca.get(),
                color.get(),
                modelo.get(),
                velocidad.get(),
                caballaje.get(),
                plazas.get(),
                id_auto
            )

            if ok:
                messagebox.showinfo("Éxito", "Auto actualizado correctamente.")
                Vista.menu_autos(ventana)
            else:
                messagebox.showerror("Error", "No se pudo actualizar el auto.")

        Button(ventana, text="Guardar Cambios", command=guardar_cambios).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)

    @staticmethod
    def borrar_autos(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Borrar Auto ::..").pack()

        Label(ventana, text="Ingrese el ID del auto a eliminar").pack()

        id_var = IntVar()
        Entry(ventana, textvariable=id_var, width=15).pack(pady=5)

        def buscar():
            autos = funciones.Autos.consultar()

            for auto in autos:
                if auto[0] == id_var.get():
                    Vista.borrar_autos_confirmacion(ventana, auto)
                    return

            messagebox.showerror("Error", "No existe un auto con ese ID.")

        Button(ventana, text="Buscar", command=buscar).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)

    @staticmethod
    def borrar_autos_confirmacion(ventana, auto):
        Vista.borrarPantalla(ventana)

        Label(ventana, text="..:: Confirmar Eliminación ::..").pack(pady=5)

        texto = f"""
    ID: {auto[0]}
    Marca: {auto[1]}
    Color: {auto[2]}
    Modelo: {auto[3]}
    Velocidad: {auto[4]}
    Caballaje: {auto[5]}
    Plazas: {auto[6]}
    """
        Label(ventana, text=texto, justify=LEFT).pack(pady=5)

        def eliminar():
            funciones.Autos.eliminar(auto)
        Button(ventana, text="Eliminar", command=eliminar).pack(pady=10)
        Button(ventana, text="Cancelar", command=lambda: Vista.menu_autos(ventana)).pack(pady=10)

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

        marca = StringVar()
        color = StringVar()
        modelo = IntVar()
        velocidad = IntVar()
        caballaje = IntVar()
        plazas = IntVar()
        ejes = IntVar()
        capacidad = IntVar()

        campos = [
            ("Marca", marca),
            ("Color", color),
            ("Modelo", modelo),
            ("Velocidad", velocidad),
            ("Caballaje", caballaje),
            ("Plazas", plazas),
            ("Ejes", ejes),
            ("Capacidad de Carga (T)", capacidad),
        ]

        for texto, var in campos:
            Label(ventana, text=texto).pack()
            Entry(ventana, textvariable=var, width=15).pack(pady=5)

        def guardar():
            camion = funciones.Camiones(
                marca.get(),
                color.get(),
                modelo.get(),
                velocidad.get(),
                caballaje.get(),
                plazas.get(),
                ejes.get(),
                capacidad.get()
            )

            if camion.insertar():
                messagebox.showinfo("Éxito", "Camión guardado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el camión.")

        Button(ventana, text="Guardar", command=guardar).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)

    @staticmethod
    def consultar_camiones(ventana):

        Vista.borrarPantalla(ventana)

        Label(ventana, text="..:: Camiones Registrados ::..").pack(pady=10)

        camiones = funciones.Camiones.consultar()

        if not camiones:
            Label(ventana, text="No hay camiones registrados.").pack(pady=10)
        else:
            for camion in camiones:
            # camion = [id, marca, color, modelo, vel, caballaje, plazas, ejes, capacidad]
                texto = f"""
ID: {camion[0]}  
Marca: {camion[1]}  
Color: {camion[2]}  
Modelo: {camion[3]}  
Velocidad: {camion[4]}  
Caballaje: {camion[5]}  
Plazas: {camion[6]}
Ejes: {camion[7]}
Capacidad: {camion[8]} T
"""
                Label(ventana, text=texto, justify=LEFT, anchor="w").pack()

        Button(ventana, text="Volver", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)

    @staticmethod
    def cambiar_camiones_pedir_id(ventana):
        Vista.borrarPantalla(ventana)

        Label(ventana, text="..:: Cambiar Camión ::..").pack()
        Label(ventana, text="Ingrese el ID del camión a modificar:").pack()

        id_var = IntVar()
        Entry(ventana, textvariable=id_var, width=15).pack(pady=5)

        def buscar():
            datos = funciones.Camiones.consultar()

            for camion in datos:
                if camion[0] == id_var.get():
                    Vista.cambiar_camiones_formulario(ventana, camion)
                    return

            messagebox.showerror("Error", "No existe un camión con ese ID.")

        Button(ventana, text="Buscar", command=buscar).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)

    @staticmethod
    def cambiar_camiones_formulario(ventana, datos):
        Vista.borrarPantalla(ventana)

        Label(ventana, text="..:: Modificar Camión ::..").pack()

        id_camion = datos[0]

        marca = StringVar(value=datos[1])
        color = StringVar(value=datos[2])
        modelo = IntVar(value=datos[3])
        velocidad = IntVar(value=datos[4])
        caballaje = IntVar(value=datos[5])
        plazas = IntVar(value=datos[6])
        ejes = IntVar(value=datos[7])
        capacidad = IntVar(value=datos[8])

        campos = [
            ("Marca", marca),
            ("Color", color),
            ("Modelo", modelo),
            ("Velocidad", velocidad),
            ("Caballaje", caballaje),
            ("Plazas", plazas),
            ("Ejes", ejes),
            ("Capacidad de Carga (T)", capacidad),
        ]

        for texto, var in campos:
            Label(ventana, text=texto).pack()
            Entry(ventana, textvariable=var, width=15).pack(pady=5)

        def guardar_cambios():
            ok = funciones.Camiones.actualizar(
                marca.get(),
                color.get(),
                modelo.get(),
                velocidad.get(),
                caballaje.get(),
                plazas.get(),
                ejes.get(),
                capacidad.get(),
                id_camion
            )

            if ok:
                messagebox.showinfo("Éxito", "Camión actualizado correctamente.")
                Vista.menu_camiones(ventana)
            else:
                messagebox.showerror("Error", "No se pudo actualizar el camión.")

        Button(ventana, text="Guardar Cambios", command=guardar_cambios).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)

    @staticmethod
    def borrar_camiones(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="..:: Borrar Camión ::..").pack()

        Label(ventana, text="Ingrese el ID del camión a eliminar").pack()

        id_var = IntVar()
        Entry(ventana, textvariable=id_var, width=15).pack(pady=5)

        def buscar():
            camiones = funciones.Camiones.consultar()

            for camion in camiones:
                if camion[0] == id_var.get():
                    Vista.borrar_camiones_confirmacion(ventana, camion)
                    return

            messagebox.showerror("Error", "No existe un camión con ese ID.")

        Button(ventana, text="Buscar", command=buscar).pack(pady=10)
        Button(ventana, text="Volver", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)

    @staticmethod
    def borrar_camiones_confirmacion(ventana, camion):
        Vista.borrarPantalla(ventana)

        Label(ventana, text="..:: Confirmar Eliminación ::..").pack(pady=5)

        texto = f"""
ID: {camion[0]}
Marca: {camion[1]}
Color: {camion[2]}
Modelo: {camion[3]}
Velocidad: {camion[4]}
Caballaje: {camion[5]}
Plazas: {camion[6]}
Ejes: {camion[7]}
Capacidad: {camion[8]} T
"""
        Label(ventana, text=texto, justify=LEFT).pack(pady=5)

        def eliminar():
            funciones.Camiones.eliminar(camion)

        Button(ventana, text="Eliminar", command=eliminar).pack(pady=10)
        Button(ventana, text="Cancelar", command=lambda: Vista.menu_camiones(ventana)).pack(pady=10)