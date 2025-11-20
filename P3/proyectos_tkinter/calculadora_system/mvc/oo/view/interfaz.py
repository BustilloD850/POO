from tkinter import *
from tkinter import messagebox
from controller import funciones
from model import operaciones

#Interfaz VIEW
class Vista:
    def __init__(self,ventana):
        ventana.title("Calculadora Basica")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.interfaz_principal(ventana)

    @staticmethod
    def interfaz_principal(ventana):

        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)
        n1=IntVar()
        n2=IntVar()

        numero2=Entry(ventana, textvariable=n1,width=5,justify="right")
        numero1=Entry(ventana, textvariable=n2,width=5,justify="right")
        numero1.focus()
        numero1.pack(side="top",anchor="center")
        numero2.pack(side="top",anchor="center")

        btn_suma=Button(ventana,text="+",command=lambda: funciones.funciones.operaciones(n1.get(),n2.get(),signo="+"))
        btn_suma.pack()
        btn_resta=Button(ventana,text="-",command=lambda: funciones.funciones.operaciones(n1.get(),n2.get(),signo="-"))
        btn_resta.pack()
        btn_mult=Button(ventana,text="x",command=lambda: funciones.funciones.operaciones(n1.get(),n2.get(),signo="x"))
        btn_mult.pack()
        btn_div=Button(ventana,text="/",command=lambda: funciones.funciones.operaciones(n1.get(),n2.get(),signo="/"))
        btn_div.pack()

        resultado=Label(ventana,text="")
        resultado.pack()

        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack()

    @staticmethod
    def menuPrincipal(ventana):
        menuBar = Menu(ventana)
        ventana.config(menu=menuBar)

        operacionesMenu = Menu(menuBar , tearoff=False)
        menuBar.add_cascade(label="Operaciones" , menu=operacionesMenu)
        operacionesMenu.add_command(label="Agregar",command=lambda: Vista.interfaz_principal(ventana))
        operacionesMenu.add_command(label="Consultar",command=lambda: Vista.consultar(ventana))
        operacionesMenu.add_command(label="Cambiar",command=lambda: Vista.actualizar(ventana))
        operacionesMenu.add_command(label="Borrar",command=lambda: Vista.eliminar(ventana))
        operacionesMenu.add_separator()
        operacionesMenu.add_command(label="Salir",command=ventana.quit)

    @staticmethod
    def eliminar(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)
        subtitl=Label(ventana, text=".:: Borrar una Operación ::.")
        subtitl.pack()

        id_op=Label(ventana,text="ID de la Operacion: ")
        id_op.pack()

        id=IntVar()

        data_id=Entry(ventana, textvariable=id, justify=RIGHT, width=5)
        data_id.focus()
        data_id.pack(pady=5)

        btn_eliminar=Button(ventana,text="Eliminar", command=lambda: Vista.mostrar_respuesta(operaciones.Operaciones.eliminar(id.get())))
        btn_eliminar.pack(pady=5)
        btn_volver=Button(ventana,text="Volver", command=lambda:Vista.interfaz_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def consultar(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)

        subtitl = Label(ventana, text=".:: Listado de las Operaciones ::.")
        subtitl.pack(pady=10)

        filas = ""
        registros = operaciones.Operaciones.consultar()

        if len(registros) > 0:
            num_operacion = 1
            for fila in registros:
                filas += (
                    f"\nOperacion: {num_operacion} | ID: {fila[0]} | Fecha: {fila[1]}\n"
                    f"  Operación: {fila[2]} {fila[4]} {fila[3]} = {fila[5]}\n"
                )
                num_operacion += 1

            lbl_listado = Label(ventana, text=filas, justify="left", anchor="w")
            lbl_listado.pack(pady=10)

        else:
            messagebox.showinfo(icon="info", message="No existen operaciones guardadas en la BD...")

        btn_volver = Button(ventana, text="Volver", command=lambda: Vista.interfaz_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def actualizar(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)

        subtitl = Label(ventana, text=".:: Cambiar una operación ::.")
        subtitl.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la operación:")
        lbl_id.pack(pady=5)

        check_id=IntVar()
        entry_id=Entry(ventana, text="", justify=CENTER, width=20,textvariable=check_id)
        entry_id.focus()
        entry_id.pack(pady=5)

        lbl_n1=Label(ventana,text="Nuevo numero 1:")
        lbl_n1.pack(pady=5)

        new_1=IntVar()
        entry_num1=Entry(ventana, text="", textvariable=new_1, justify=CENTER, width=20)
        entry_num1.focus()
        entry_num1.pack(pady=5)

        lbl_n2=Label(ventana,text="Nuevo numero 2:")
        lbl_n2.pack(pady=5)

        new_2=IntVar()
        entry_num2=Entry(ventana, text="",textvariable=new_2 ,justify=CENTER, width=20)
        entry_num2.focus()
        entry_num2.pack(pady=5)

        lbl_sign=Label(ventana,text="Nuevo Signo:")
        lbl_sign.pack(pady=5)

        new_sign=StringVar()
        entry_sign=Entry(ventana, text="", textvariable=new_sign, justify=CENTER, width=20)
        entry_sign.focus()
        entry_sign.pack(pady=5)

        lbl_res=Label(ventana,text="Nuevo Resultado:")
        lbl_res.pack(pady=5)

        new_result=DoubleVar()
        entry_res=Entry(ventana, text="", justify=CENTER, width=20,textvariable=new_result)
        entry_res.focus()
        entry_res.pack(pady=5)

        btn_guardar = Button(ventana, text="Guardar", command=lambda: Vista.mostrar_respuesta(operaciones.Operaciones.actualizar(check_id.get(),new_1.get(),new_2.get(),new_sign.get(),new_result.get())))
        btn_guardar.pack(pady=5)

        btn_volver = Button(ventana, text="Volver", command=lambda: Vista.interfaz_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def mostrar_respuesta(resultado):
        funciones.funciones.respuesta_sql(resultado)