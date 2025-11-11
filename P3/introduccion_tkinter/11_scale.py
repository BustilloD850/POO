from tkinter import *

def lbl_total():
    lbl_mostar.config(text=f"Valor seleccionado por el usuario: {valor.get()}")

ventana=Tk()
ventana.title("Scale")
ventana.geometry("500x500")

valor=IntVar()
escala=Scale(ventana, from_=0, to_=100,orient="horizontal",variable=valor)
escala.pack()

btn_mostrar=Button(ventana, text="Mostrar valor",command=lbl_total)
btn_mostrar.pack()
lbl_mostar=Label(ventana, text="")
lbl_mostar.pack()

ventana.mainloop()