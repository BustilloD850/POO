"""
sin el metodo constructor
que todos los atributos sean publicos
que los metodos acelerar y frenar no hagan nada (usar pass)
"""

import os

os.system("cls")

#class Coches():
#    marca= ""
#    color= ""
#    modelo= ""
#    velocidad= 0
#    caballaje = 0
#    plazas= 0

#    def acelerar():
#        pass

#    def frenar():
#        pass

#coche1=Coches()
#coche1.marca="VW"
#coche1.color="Blanco"
#coche1.modelo="2022"
#coche1.velocidad=220
#coche1.caballaje=150
#coche1.plazas=5

#coche2=Coches()
#coche2.marca="Nissan"
#coche2.color="Azul"
#coche2.modelo="2020"
#coche2.velocidad=180
#coche2.caballaje=150
#coche2.plazas=6

#print(f"coche1: \n{coche1.marca}\n{coche1.color}\n{coche1.modelo}\n{coche1.velocidad}\n{coche1.caballaje}\n{coche1.plazas}")
#print(f"coche2: \n{coche2.marca}\n{coche2.color}\n{coche2.modelo}\n{coche2.velocidad}\n{coche2.caballaje}\n{coche2.plazas}")

import os
os.system("clear")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    #Metodo constructor para inicializar los valores de los atributos a la hora de crear o instanciar el objeto de la clase
    
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
      self.marca=marca
      self.color=color
      self.modelo=modelo
      self.velocidad=velocidad
      self.caballaje=caballaje
      self.plazas=plazas

    #Crear los setters y getters. estos metodos son importantes y necesarios en todas las clases para que el programador interacue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto
    # En teoria se deberia de crear yn metodo Getters y Setters por cada atributo que contenga la clase 

    #1er forma
    def getMarca(self):
      return self.marca
    
    def setMarca(self,marca):
       self.marca=marca
    #2da forma
    @property
    def marca2(self):
       return self.marca
    
    @marca2.setter
    def marca2(self,marca):
       self.marca=marca

    def getColor(self):
      return self.color
    
    def setColor(self,color):
       self.color=color

    def getModelo(self):
      return self.modelo
    
    def setModelo(self,modelo):
       self.modelo=modelo

    def getVelocidad(self):
      return self.velocidad
    
    def setVelocidad(self,velocidad):
       self.velocidad=velocidad

    def getCaballaje(self):
      return self.caballaje
    
    def setCaballaje(self,caballaje):
       self.caballaje=caballaje

    def getPlazas(self):
      return self.plazas
    
    def setPlazas(self,plazas):
       self.plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0)
coche1.num_serie="B014567890"
coche4=Coches("","","",0,0,0)
coche4.marca2="Volvo"
print(coche4.marca2)

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca} \n color: {coche1.getColor} \n Modelo: {coche1.getModelo} \n velocidad: {coche1.getVelocidad} \n caballaje: {coche1.getCaballaje} \n plazas: {coche1.getPlazas} \n Numero de Serie: {coche1.num_serie}")

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca} \n color: {coche2.getColor} \n Modelo: {coche2.getModelo} \n velocidad: {coche2.getVelocidad} \n caballaje: {coche2.getCaballaje} \n plazas: {coche2.getPlazas} ")

