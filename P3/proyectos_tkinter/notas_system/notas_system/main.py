"""
1.- implementar el mvc
2.- paradigma poo
3.- app de escritorio con interfaz grafica
"""

from view import view1
from tkinter import *

class App:
    def __init__(self, ventana):
        self.vista = view1.View(ventana)

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()