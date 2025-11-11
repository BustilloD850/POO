from tkinter import *

def mostrar():
    valor=lista.get(lista.curselection())
    lbl_seleccion.config(text=f"Seleccionaste: {valor}")

ventana=Tk()
ventana.title("ListBox")
ventana.geometry("500x500")

lista=Listbox(ventana,width=50,height=5,selectmode="single")
lista.pack()

opciones={"Azul","Rojo","Negro","Amarillo"}
for i in opciones:
    lista.insert(END,i)

btn_mostrar=Button(ventana,text="Mostrar Seleccion del Usuario", command=mostrar)
btn_mostrar.pack()
lbl_seleccion=Label(ventana,text="")
lbl_seleccion.pack()

ventana.mainloop()