from tkinter import *

def entrar():#mostrar etiqueta abajo que diga bienvenido
    lbl_titulo.config(
    text="POO con Python",
    bg="green",
    fg="red",
    width=50,
    height=4,
    font=("Arial",30,"bold"),
    border=2,
    relief=GROOVE
)

ventana=Tk()
ventana.title("Entry")
ventana.geometry("500x500")


lbl_titulo=Label(ventana, background="lightblue", text="Acceso al Sistema")
lbl_titulo.config(
    bg="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"italic"),
    border=2,
    relief=GROOVE
)
lbl_titulo.pack(pady=50)

lbl_nombre=Label(ventana,text="Ingrese el Nombre: ")
lbl_nombre.pack(pady=5)

txt_nombre=Entry(ventana)
txt_nombre.pack()

lbl_password=Label(ventana,text="Ingrese la Contraseña: ")
lbl_password.pack(pady=5)

txt_password=Entry(ventana,show="*")
txt_password.pack()

btn_entrar=Button(ventana, text="Entrar",command=entrar)
btn_entrar.pack(pady=5)

btn_borrar=Button(ventana, text="Regresa clic aqui",command="borrar")
btn_borrar.pack(pady=5)

lbl_resultado=Label(ventana,text="")
lbl_resultado.pack(pady=5)

ventana.mainloop()