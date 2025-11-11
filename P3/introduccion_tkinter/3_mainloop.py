from tkinter import*

ventana= Tk()
ventana.title("mainloop")
ventana.geometry("800x600")

marco= Frame(ventana)
marco.config(
    bg="#000000",
    bd=5,
    height=400,
    width=600,
    relief=RAISED
)

marco.pack(
    padx=50,
    pady=50
)

ventana.mainloop()