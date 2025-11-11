from tkinter import *

def mostrarEstado():
    if opcion.get()==1:
        lbl_notificacion.config(text=f"Notificaciones Activadas")
    else:
        lbl_notificacion.config(text=f"Notificaciones Desactivadas")

ventana=Tk()
ventana.title("Check Buttons")
ventana.geometry("500x500")

opcion=IntVar()
check_btn=Checkbutton(ventana,text="¿Deseas recibir notificaciones?",variable=opcion,onvalue=1,offvalue=0)
check_btn.pack()

btn_confirmar=Button(ventana,text="Confirmar",command=mostrarEstado)
btn_confirmar.pack()

lbl_notificacion=Label(ventana,text="")
lbl_notificacion.pack()

ventana.mainloop()