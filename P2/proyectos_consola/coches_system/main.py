#Instanciar los objetos para posterior implementarlos 
from model import coches,cochesBD

import os

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\n\t\t Oprima tecla para continuar ...")

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("No. de plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas):
    borrarPantalla()
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

def respuesta_sql(respuesta):
    if respuesta:
        print("\n\t...¡Accion realizada con exito!...")
    else:
        print("\n\t...No fue posible realizar la accion correctamente, vuelva a intentar ...")
        esperarTecla()

def lista_vehiculos():
     print(f"{'-'*70}")
     print(f"{'ID':<5}{'MARCA':<10}{'COLOR':<10}{'MODELO':<10}{'VELOCIDAD':<10}{'CABALLAJE':<10}{'PLAZAS':<10}")
     print(f"{'-'*70}")
     autitos=cochesBD.Autos.consultar()
     for auto in autitos:
        id,marca,color,modelo,velocidad,caballaje,plazas=auto
        print(f"{id:<5}{marca:<10}{color:<10}{modelo:<10}{velocidad:<10}{caballaje:<10}{plazas:<10}")
        print(f"{'-'*70}")

def buscar_por_id(id_buscar):
    """Devuelve el registro (tupla) cuyo id==id_buscar, o None si no existe."""
    try:
        registros = cochesBD.Autos.consultar()
        for reg in registros:
            if reg[0] == id_buscar:
                return reg
    except Exception as e:
        print("Error al consultar registros:", e)
    return None

def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=cochesBD.Autos(marca,color,modelo,velocidad,potencia,plazas)
    borrarPantalla()
    imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas)
    esperarTecla()
    return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas

def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    traccion=input("traccion: ").upper().strip()
    cerrada=input("cerrada (Si/No): ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False
    coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"Traccion: {coche.traccion} \n Cerrada: {coche.cerrada}")
    esperarTecla()
    return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.traccion,coche.cerrada

def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camion")
    eje=int(input("No. de Ejes: "))
    capacidadCarga=int(input("Capacidad de Carga (Kg): "))
    coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"Ejes: {coche.eje} \n Capacidad de Carga (Kg): {coche.capacidadCarga}")
    esperarTecla()
    return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.eje,coche.capacidadCarga

def menu_acciones(tipo):
    print(f"\n\t\t ...::: Menu de {tipo} :::...\n\t1.-Insertar\n\t2.-Consultar\n\t3.-Actualizar\n\t4.-Eliminar\n\t5.-Regresar")
    opcion = input("\n\t\tElige una opción: ").upper().strip()
    return opcion

def menu_autos():
    while True:
        borrarPantalla()
        opcion=menu_acciones("Autos")
        if opcion=="1" or opcion=="INSERTAR":
            marca,color,modelo,velocidad,caballaje,plazas=autos()
            #agregar a la base de datos
            auto=cochesBD.Autos(marca,color,modelo,velocidad,caballaje,plazas)
            respuesta=auto.insertar()
            respuesta_sql(respuesta)
        elif opcion=="2" or opcion=="CONSULTAR":
            borrarPantalla()
            registro=cochesBD.Autos.consultar()
            if len(registro)>0:
                num_autos=1
                for fila in registro:
                    print(f"Auto # {num_autos} con ID {fila[0]}\nMarca: {fila[1]}\nColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\nPotencia: {fila[5]}\nPlazas: {fila[6]}")
                    num_autos+=1
                    esperarTecla()
            else:
                print("\n\t\t¡No existen datos que mostrar, por el momento!...")
                esperarTecla()
        elif opcion=="3" or opcion=="ACTUALIZAR":
            borrarPantalla()
            id=input("Ingrese el ID a actualizar: ").strip()
            marca,color,modelo,velocidad,caballaje,plazas=autos()
            respuesta=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
            respuesta_sql(respuesta)
        elif opcion=="4" or opcion=="ELIMINAR":
            borrarPantalla()
            id=input("Ingrese el ID a eliminar: ").strip()
            respuesta=cochesBD.Autos.eliminar(id)
            respuesta_sql(respuesta)
        elif opcion=="5" or opcion=="REGRESAR":
            break
        else:
            print("\n\t\t¡Opcion no valida. Intenta de nuevo!...")
            esperarTecla()

def menu_camionetas():
    while True:
        borrarPantalla()
        opcion=menu_acciones("Camionetas")
        if opcion=="1" or opcion=="INSERTAR":
            marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada=camionetas()
            #acceder a la base de datos
            respuesta=cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
            respuesta_sql(respuesta)
        elif opcion=="2" or opcion=="CONSULTAR":
            borrarPantalla()
            registro=cochesBD.Camionetas.consultar()
            if len(registro)>0:
                num_autos=1
                for fila in registro:
                    print(f"Camioneta # {num_autos} con ID {fila[0]}\nMarca: {fila[1]}\nColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\nPotencia: {fila[5]}\nPlazas: {fila[6]}\nTraccion: {fila[7]}\nCerrada: {fila[8]}")
                    num_autos+=1
                    esperarTecla()
            else:
                print("\n\t\t¡No existen datos que mostrar, por el momento!...")
                esperarTecla()
        elif opcion=="3" or opcion=="ACTUALIZAR":
            borrarPantalla()
            id=input("Ingrese el ID a actualizar: ").strip()
            marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada=camionetas()
            respuesta=cochesBD.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
            respuesta_sql(respuesta)
        elif opcion=="4" or opcion=="ELIMINAR":
            borrarPantalla()
            id=input("Ingrese el ID a eliminar: ").strip()
            respuesta=cochesBD.Camionetas.eliminar(id)
            respuesta_sql(respuesta)
        elif opcion=="5" or opcion=="REGRESAR":
            break
        else:
            print("\n\t\t¡Opcion no valida. Intenta de nuevo!...")
            esperarTecla()

def menu_camiones():
    while True:
        borrarPantalla()
        opcion=menu_acciones("Camiones")
        if opcion=="1" or opcion=="INSERTAR":
            marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga=camiones()
            #acceder a la base de datos
            respuesta=cochesBD.Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
            respuesta_sql(respuesta)
        elif opcion=="2" or opcion=="CONSULTAR":
            borrarPantalla()
            registro=cochesBD.Camiones.consultar()
            if len(registro)>0:
                num_autos=1
                for fila in registro:
                    print(f"Camion # {num_autos} con ID {fila[0]}\nMarca: {fila[1]}\nColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\nPotencia: {fila[5]}\nPlazas: {fila[6]}\nEje: {fila[7]}\nCapacidad de Carga: {fila[8]}")
                    num_autos+=1
                    esperarTecla()
            else:
                print("\n\t\t¡No existen datos que mostrar, por el momento!...")
                esperarTecla()
        elif opcion=="3" or opcion=="ACTUALIZAR":
            borrarPantalla()
            id=input("Ingrese el ID a actualizar: ").strip()
            marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga=camiones()
            respuesta=cochesBD.Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
            respuesta_sql(respuesta)
        elif opcion=="4" or opcion=="ELIMINAR":
            borrarPantalla()
            id=input("Ingrese el ID a eliminar: ").strip()
            respuesta=cochesBD.Camiones.eliminar(id)
            respuesta_sql(respuesta)
        elif opcion=="5" or opcion=="REGRESAR":
            break
        else:
            print("\n\t\t¡Opcion no valida. Intenta de nuevo!...")
            esperarTecla()

def main():
  opcion=True
  while opcion:
    borrarPantalla()
    opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.-Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
    match opcion:
        case "1":
            menu_autos()
            esperarTecla()
        case "2":
            menu_camionetas()
            esperarTecla()  
        case "3":
            menu_camiones()
            esperarTecla()
        case "4":
            borrarPantalla()
            input("\n\t\tSalir del Sistema")
            opcion=False   
        case _:
            input("Opcion invalida... vuelva a intertarlo...")
            opcion=True    

if __name__=="__main__":
    main()