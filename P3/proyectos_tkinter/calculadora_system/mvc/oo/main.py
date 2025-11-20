"""
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- mostrar el Resultado en una alerta
4.- Programado de forma OO
5.- Considerar el mvc
"""
from view import interfaz
from tkinter import*

class App:
    @staticmethod
    def main(ventana):
        view=interfaz.Vista(ventana)

if __name__=="__main__":
    ventana=Tk()
    App.main(ventana)
    ventana.mainloop()