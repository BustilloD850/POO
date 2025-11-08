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
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

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
#coche1.marca="VW"
#coche1.color="Blanco"
#coche1.modelo="2022"
#coche1.velocidad=220
#coche1.caballaje=150
#coche1.plazas=5

coche1=Coches()
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)

coche2=Coches()
coche1.setMarca("Nissan")
coche1.setColor("Azul")
coche1.setModelo("2020")
coche1.setVelocidad(180)
coche1.setCaballaje(150)
coche1.setPlazas(6)

coche3=Coches()
coche3.marca2="Honda"
print(coche3.marca2)

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca} \n color: {coche1.getColor} \n Modelo: {coche1.getModelo} \n velocidad: {coche1.getVelocidad} \n caballaje: {coche1.getCaballaje} \n plazas: {coche1.getPlazas} ")

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca} \n color: {coche2.getColor} \n Modelo: {coche2.getModelo} \n velocidad: {coche2.getVelocidad} \n caballaje: {coche2.getCaballaje} \n plazas: {coche2.getPlazas} ")

#coche2.marca="Nissan"
#coche2.color="Azul"
#coche2.modelo="2020"
#coche2.velocidad=180
#coche2.caballaje=150
#coche2.plazas=6

#print(f"Datos del Vehiculo: \n Marca:{coche1.marca} \n color: {coche1.color} \n Modelo: {coche1.modelo} \n velocidad: {coche1.velocidad} \n caballaje: {coche1.caballaje} \n plazas: {coche1.plazas} ")
#print(f"\nDatos del Vehiculo: \n Marca:{coche2.marca} \n color: {coche2.color} \n Modelo: {coche2.modelo} \n velocidad: {coche2.velocidad} \n caballaje: {coche2.caballaje} \n plazas: {coche2.plazas} ")