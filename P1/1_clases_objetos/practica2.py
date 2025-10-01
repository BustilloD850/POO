"""
Ejercicio Practico #2 "modelar y Diagramar en POO"
"""
import os

os.system("cls")

#crear una clase
class Coches:
    #metodo constructor que inicializa los valores de los atributos cuando se instancie un objeto de la clase
    def __init__(self, color, marca, velocidad):
        self.color=color
        self.marca=marca
        self.velocidad=velocidad

    def acelerar(self,incremento):
        self.velocidad= self.velocidad+incremento
        return self.velocidad
    
    def frenar(self, decremento):
        self.velocidad= self.velocidad-decremento
        return self.velocidad
    
    def tocar_claxon(self):
        return "PIIIII"
    
#instanciar objetos de la clase Coches

coche1=Coches("blanco", "toyota", 220)
coche2=Coches("amarillo", "nissan", 180)

#print(f"los valores del objeto 1 son: {coche1.color},{coche1.marca}, {coche1.velocidad}")
#print(f"la velocidad original del coche 1 es: {coche1.velocidad} y cambio a: {coche1.acelerar(50)}")
#print(f"los valores del objeto 2 son: {coche2.color},{coche2.marca}, {coche2.velocidad}")
#print(f"la velocidad original del coche 1 es: {coche2.velocidad} y cambio a: {coche2.frenar(100)}")