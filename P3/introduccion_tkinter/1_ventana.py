"""
Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones en python para escritorio
"""

#from tkinter import *

#ventata=Tk()

import tkinter as tk

ventana=tk.Tk() #crear ventana

ventana.title("Mi primer App grafica en Tkinter")
ventana.geometry("800x600")
ventana.resizable(True,False) #metodo para redimensionar el tamanño de la ventana
ventana.mainloop() # metodo que permite mantener la ventana abierta e interactuar con ella