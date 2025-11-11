"""Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- mostrar el Resultado en una alerta"""

from tkinter import *
from tkinter import messagebox

#Control app ó Controller
def operaciones(tipo,resultado,numero1,icono,numero2):
    messagebox.showinfo(title=f"{tipo}",icon="info",message=f"{numero1}{icono}{numero2}={resultado}")
    return

def sumar(numero1,numero2):
    resultado=numero1 + numero2
    tipo="suma"
    icono="+"
    return operaciones(tipo,resultado,numero1,icono,numero2)

def restar(numero1,numero2):
    resultado=numero1 - numero2
    tipo="resta"
    icono="-"
    return operaciones(tipo,resultado,numero1,icono,numero2)

def multiplicar(numero1,numero2):
    resultado=numero1 * numero2
    tipo="multiplicacion"
    icono="X"
    return operaciones(tipo,resultado,numero1,icono,numero2)

def dividir(numero1,numero2):
    resultado=numero1 / numero2
    tipo="division"
    icono="/"
    return operaciones(tipo,resultado,numero1,icono,numero2)

#Interfaz VIEW
ventana=Tk()
ventana.title("Calculadora Basica")
ventana.geometry("500x500")
ventana.resizable(False,False)

n1=IntVar()
n2=IntVar()

numero2=Entry(ventana, textvariable=n1,width=5,justify="right")
numero1=Entry(ventana, textvariable=n2,width=5,justify="right")
numero1.pack(side="top",anchor="center")
numero2.pack(side="top",anchor="center")

btn_suma=Button(ventana,text="Suma",command=lambda: sumar(n1.get(),n2.get()))
btn_suma.pack()
btn_resta=Button(ventana,text="Resta",command=lambda: restar(n1.get(),n2.get()))
btn_resta.pack()
btn_mult=Button(ventana,text="Multiplicacion",command=lambda: multiplicar(n1.get(),n2.get()))
btn_mult.pack()
btn_div=Button(ventana,text="Division",command=lambda: dividir(n1.get(),n2.get()))
btn_div.pack()

btn_salir=Button(ventana,text="Salir",command=ventana.quit)
btn_salir.pack()

ventana.mainloop()