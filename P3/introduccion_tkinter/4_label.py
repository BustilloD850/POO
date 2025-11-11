from tkinter import *

ventana=Tk()
ventana.geometry=("800x600")
ventana.title("etiquetas")

#Etiquetas o label
etiqueta1=Label(ventana,text="Nombre de la persona").pack()

marco1=Frame(ventana, bg="#ECEAEA",width=200,height=100)
marco1.pack_propagate(False)

etiqueta2=Label(marco1, text="Soy una etiqueta dentro de un marco", bg="#aeaeae").pack()

ventana.mainloop()