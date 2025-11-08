import os
from coches import *

os.system("cls")

#Solicitar los datos que posteriormente seran los atributos del objeto
num_coches=int(input("¿Cuantos coches tienes?"))

for i in range(0,num_coches):
    os.system("cls")
    print(f"\n\t...Datos del automovil #{i+1}...")
    marca=input("Ingrese la marca: ").upper()
    color=input("Ingrese el color: ").upper()
    modelo=input("Ingrese el modelo: ").upper()
    velocidad=int(input("Ingrese la velocidad: "))
    potencia=int(input("Ingrese la potencia: "))
    plazas=int(input("Ingrese el # de plazas: "))

    coche1=Coches(marca,color, modelo, velocidad, potencia, plazas)

    print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")

#coche1=Coches("VW","Blanco","2022",220,150,5)
#coche2=Coches("Nissan","Azul","2020",180,150,6)
#coche3=Coches("Honda","","",0,0,0)
#coche1.num_serie="B014567890"
#coche4=Coches("","","",0,0,0)
#coche4.marca2="Volvo"
#print(coche4.marca2)

#print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca} \n color: {coche2.getColor} \n Modelo: {coche2.getModelo} \n velocidad: {coche2.getVelocidad} \n caballaje: {coche2.getCaballaje} \n plazas: {coche2.getPlazas} ")

coche=Coches("VW","Blanco","2020",220,180,4)
print(coche.color,coche.acelerar())

camion=camiones("VW","blanco a perlado","2020",220,180,4,2,2500)
print(camion.color,camion.acelerar())

camioneta=camionetas("VW","Azul","2020",220,180,4,"Delantera",True)