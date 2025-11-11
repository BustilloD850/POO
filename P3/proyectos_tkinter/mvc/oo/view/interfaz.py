from tkinter import *
from tkinter import messagebox
from controller import funciones

#Interfaz VIEW
class Vista:
    def __init__(self,ventana):
        ventana.title("Calculadora Basica")
        ventana.geometry("500x500")
        ventana.resizable(False,False)
        self.interfaz_principal(ventana)

    def interfaz_principal(self,ventana):

        n1=IntVar()
        n2=IntVar()

        numero2=Entry(ventana, textvariable=n1,width=5,justify="right")
        numero1=Entry(ventana, textvariable=n2,width=5,justify="right")
        numero1.pack(side="top",anchor="center")
        numero2.pack(side="top",anchor="center")

        btn_suma=Button(ventana,text="Suma",command=lambda: funciones.funciones.operaciones(n1.get(),n2.get(),signo="+"))
        btn_suma.pack()
        btn_resta=Button(ventana,text="Resta",command=lambda: funciones.funciones.operaciones(n1.get(),n2.get(),signo="-"))
        btn_resta.pack()
        btn_mult=Button(ventana,text="Multiplicacion",command=lambda: funciones.funciones.operaciones(n1.get(),n2.get(),signo="x"))
        btn_mult.pack()
        btn_div=Button(ventana,text="Division",command=lambda: funciones.funciones.operaciones(n1.get(),n2.get(),signo="/"))
        btn_div.pack()

        resultado=Label(ventana,text="")
        resultado.pack()

        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack()