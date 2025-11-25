from tkinter import *
from tkinter import messagebox
from controller import controlador1

class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.title("Gestion de Notas")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: Menú Principal ::..", justify=CENTER)
        lbl_titulo.pack()

        btn_registro=Button(ventana, text="1.- Registro", command= lambda: View.registro(ventana))
        btn_registro.pack(pady=15)
        btn_login=Button(ventana, text="2.- Login", command= lambda: View.login(ventana))
        btn_login.pack(pady=15)
        btn_salir=Button(ventana, text="3.- Salir", command= lambda: ventana.quit)
        btn_salir.pack(pady=15)

    @staticmethod
    def registro(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: Registro en el sistema ::..", justify=CENTER)
        lbl_titulo.pack()

        lbl_nombre=Label(ventana, text="¿Cual es tu nombre?", justify=CENTER)
        lbl_nombre.pack()
        txt_nombre=Entry(ventana)
        txt_nombre.focus()
        txt_nombre.pack(pady=15)

        lbl_apellidos=Label(ventana, text="¿Cuales son tus apellidos?", justify=CENTER)
        lbl_apellidos.pack()
        txt_apellidos=Entry(ventana)
        txt_apellidos.focus()
        txt_apellidos.pack(pady=15)

        lbl_email=Label(ventana, text="Ingresa tu E-mail", justify=CENTER)
        lbl_email.pack()
        txt_email=Entry(ventana)
        txt_email.focus()
        txt_email.pack(pady=15)

        lbl_password=Label(ventana, text="Ingresa tu contraseña", justify=CENTER)
        lbl_password.pack()
        txt_password=Entry(ventana, show="*")
        txt_password.focus()
        txt_password.pack(pady=15)

        btn_registrar=Button(ventana, text="Registrar", command=lambda: {
                             controlador1.Controlador.registro(txt_nombre.get(),txt_apellidos.get(),txt_email.get(),txt_password.get()),
                             View.login(ventana)
                             })
        btn_registrar.pack(pady=15)
        btn_volver=Button(ventana, text="Volver", command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=15)

    @staticmethod
    def login(ventana):
            View.borrarPantalla(ventana)
            lbl_titulo=Label(ventana, text="..:: Inicio de Sesión ::..", justify=CENTER)
            lbl_titulo.pack()

            lbl_email=Label(ventana, text="Ingresa tu E-mail", justify=CENTER)
            lbl_email.pack()
            txt_email=Entry(ventana)
            txt_email.focus()
            txt_email.pack(pady=15)

            lbl_password=Label(ventana, text="Ingresa tu contraseña", justify=CENTER)
            lbl_password.pack()
            txt_password=Entry(ventana, show="*")
            txt_password.focus()
            txt_password.pack(pady=15)

            btn_login=Button(ventana, text="Entrar", command=lambda:
                 controlador1.Controlador.inicio_sesion(ventana,txt_email.get(),txt_password.get()))
            btn_login.pack(pady=15)
            btn_volver=Button(ventana, text="Volver", command=lambda: View.menu_principal(ventana))
            btn_volver.pack(pady=15)

    @staticmethod
    def menu_notas(ventana,usuario_id,nombre, apellidos):
        global id_user,nom_user,ape_user
        id_user=usuario_id
        nom_user=nombre
        ape_user=apellidos
        
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: Bienvenido {nombre}{apellidos}, has iniciado sesion::..", justify=CENTER)
        lbl_titulo.pack()

        btn_crear=Button(ventana, text="1.- Crear", command= lambda: View.crear_notas(ventana))
        btn_crear.pack(pady=15)
        btn_mostrar=Button(ventana, text="2.- Mostrar", command= lambda: View.mostrar_notas(ventana))
        btn_mostrar.pack(pady=15)
        btn_cambiar=Button(ventana, text="3.- Cambiar", command= lambda: View.cambiar_notas(ventana))
        btn_cambiar.pack(pady=15)
        btn_eliminar=Button(ventana, text="4.- Eliminar", command= lambda: View.eliminar_notas(ventana))
        btn_eliminar.pack(pady=15)
        btn_volver=Button(ventana, text="5.- Volver", command= lambda: View.login(ventana))
        btn_volver.pack(pady=15)

    @staticmethod
    def crear_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: Titulo: ::..", justify=CENTER)
        lbl_titulo.pack()

        txt_titulo=Entry(ventana)
        txt_titulo.focus()
        txt_titulo.pack(pady=15)

        lbl_descripcion=Label(ventana, text="..:: Descripcion: ::..", justify=CENTER)
        lbl_descripcion.pack(pady=15)

        txt_descripcion=Entry(ventana)
        txt_descripcion.focus()
        txt_descripcion.pack(pady=15)

        btn_guardar=Button(ventana, text="Guardar", command= lambda: View.login(ventana))
        btn_guardar.pack(pady=15)

        btn_volver=Button(ventana, text="Volver", command= lambda: View.login(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=15)

    @staticmethod
    def mostrar_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: Titulo: ::..", justify=CENTER)
        lbl_titulo.pack()

        filas=""
        registros = [
            ["1","100","Nota 1","Descripcion de la Nota 1","2025-11-24"]
                     ]
        num_nota=1
        if len(registros)>0:
            for fila in registros:
                filas += (
                f"Nota: {num_nota}\n"
                f"ID: {fila[0]}.- Titulo: {fila[2]}. "
                f"Fecha de creacion: {fila[4]}\n"
                f"Descripcion: {fila[3]}\n\n"
            )
            num_nota += 1
        else:
            messagebox.showinfo(icon="warning",message="...¡No existen notas para este usuario!...")

        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_volver=Button(ventana, text="Volver", command= lambda: View.login(ventana))
        btn_volver.pack(pady=15)

    @staticmethod
    def cambiar_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..::{nombre}{apellidos} vamos a modificar tu nota",justify=CENTER)
        lbl_titulo.pack(pady=15)

        lbl_id=Label(ventana, text="ID de la Nota a cambiar:")
        lbl_id.pack(pady=15)

        tx_id=Entry(ventana)
        tx_id.focus()
        tx_id.pack(pady=15)

        lbl_titulo=Label(ventana, text="Nuevo Titulo:")
        lbl_titulo.pack(pady=15)

        tx_titulo=Entry(ventana)
        tx_titulo.focus()
        tx_titulo.pack(pady=15)

        lbl_descripcion=Label(ventana, text="Nueva Descripcion:")
        lbl_descripcion.pack(pady=15)

        tx_descripcion=Entry(ventana)
        tx_descripcion.focus()
        tx_descripcion.pack(pady=15)

        btn_guardar=Button(ventana, text="Guardar", command= lambda: View.login(ventana))
        btn_guardar.pack(pady=15)

        btn_volver=Button(ventana, text="Volver", command= lambda: View.login(ventana))
        btn_volver.pack(pady=15)
    
    @staticmethod
    def eliminar_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..::{nombre}{apellidos} vamos a eliminar tu nota",justify=CENTER)
        lbl_titulo.pack(pady=15)

        lbl_id=Label(ventana, text="ID de la Nota a eliminar:")
        lbl_id.pack(pady=15)

        tx_id=Entry(ventana)
        tx_id.focus()
        tx_id.pack(pady=15)

        btn_guardar=Button(ventana, text="Eliminar", command= lambda: "")
        btn_guardar.pack(pady=15)

        btn_volver=Button(ventana, text="Volver", command= lambda: View.login(ventana))
        btn_volver.pack(pady=15)