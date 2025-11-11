from tkinter import *

def cambiartexto():
    mensajecambiante.config(
        text="texto cambiado"
    )

def texto_original():
    mensajecambiante.config(
        text="Texto original"
    )

ventana=Tk()
ventana.title("Uso de botones")
ventana.geometry("800x600")

frame_principal=Frame(ventana)
frame_principal.config(
    bg="silver",
    width=800,
    height=50,
    border=2,
    relief=SOLID
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)

label_titulo=Label(frame_principal, text="Uso de botones")
label_titulo.config(
    bg="silver",
    width=20
)
label_titulo.pack(pady=10)

mensajecambiante=Label(ventana,text="Texto original")
mensajecambiante.pack()

boton_cambiar=Button(ventana,text="Cambiar texto",command=cambiartexto)
boton_cambiar.pack()

boton_regresar=Button(ventana,text="Regresar texto",command=texto_original)
boton_regresar.pack()

ventana.mainloop()