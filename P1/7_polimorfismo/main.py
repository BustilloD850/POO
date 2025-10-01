import os
from coches import *


def autos():
    os.system("cls")
    print(f"\n\t...Datos del vehiculo...")
    marca=input("Ingrese la marca: ").upper()
    color=input("Ingrese el color: ").upper()
    modelo=input("Ingrese el modelo: ").upper()
    velocidad=int(input("Ingrese la velocidad: "))
    potencia=int(input("Ingrese la potencia: "))
    plazas=int(input("Ingrese el # de plazas: "))

    coche1=Coches(marca,color, modelo, velocidad, potencia, plazas)

    print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.marca()} \n color: {coche1.color()} \n Modelo: {coche1.modelo()} \n velocidad: {coche1.velocidad()} \n caballaje: {coche1.caballaje()} \n plazas: {coche1.plazas()}")

def camionetas():
    os.system("cls")
    print(f"\n\t...Datos del vehiculo...")
    marca=input("Ingrese la marca: ").upper()
    color=input("Ingrese el color: ").upper()
    modelo=input("Ingrese el modelo: ").upper()
    velocidad=int(input("Ingrese la velocidad: "))
    potencia=int(input("Ingrese la potencia: "))
    plazas=int(input("Ingrese el # de plazas: "))

    traccion=input("Ingresar la traccion:").upper()
    cerrada=input("Ingresar SI/NO si es cerada o no: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False

    coche1=camionetas(marca,color, modelo, velocidad, potencia, plazas,traccion,cerrada)

    print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.marca()} \n color: {coche1.color()} \n Modelo: {coche1.modelo()} \n velocidad: {coche1.velocidad()} \n caballaje: {coche1.caballaje()} \n plazas: {coche1.plazas()} \n traccion: {coche1.traccion()} \n cerrada: {coche1.cerrada()}")

def camiones():
    os.system("cls")
    print(f"\n\t...Datos del vehiculo...")
    marca=input("Ingrese la marca: ").upper()
    color=input("Ingrese el color: ").upper()
    modelo=input("Ingrese el modelo: ").upper()
    velocidad=int(input("Ingrese la velocidad: "))
    potencia=int(input("Ingrese la potencia: "))
    plazas=int(input("Ingrese el # de plazas: "))
    eje=int(input("Ingresar el numero de ejes: "))
    capacidad=int(input("Ingresar la capacidad de carga: "))

    coche1=camiones(marca,color, modelo, velocidad, potencia, plazas,eje,capacidad)

    print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.marca()} \n color: {coche1.color()} \n Modelo: {coche1.modelo()} \n velocidad: {coche1.velocidad()} \n caballaje: {coche1.caballaje()} \n plazas: {coche1.plazas()} \n ejes: {coche1.eje()} \n capacidad de carga: {coche1.capacidadCarga()}")

opcion=1
while opcion!="4":
    os.system("cls")
    opcion=input("\n\t\t.::Menu pricipal::.\n\t1.- Autos\n\t2.- Camionetas\n\t3.- Camiones\n\t4.- Salir\n\tElige una opción: ").lower().strip()
    match opcion:
        case "1":
            print("Autos")
            autos()
            input("OPRIMA TECLA PARA CONTINUAR")

        case "2":
            print("Camionetas")
            camionetas()
            input("OPRIMA TECLA PARA CONTINUAR")
        
        case "3":
            print("Camiones")
            camiones()
            input("OPRIMA TECLA PARA CONTINUAR")

        case "4":
            input("Salir del sistema")
   
        case _:
            input("Opcion invalida... vuelva a intentarlo...")