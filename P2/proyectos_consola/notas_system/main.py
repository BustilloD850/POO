#archivo main
from model import usuarios, notas
from model.usuarios import usuario
from model.notas import nota
import getpass

class funciones():
    @staticmethod
    def borrarPantalla():
        import os
        os.system("cls")

    @staticmethod
    def esperarTecla():
        input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

class main():
    def menu_usuarios():
        print("\n \t.:: Sistema de Gestión de Notas ::.. \n\t\t1.-  Registro  \n\t\t2.-  Login \n\t\t3.- Salir ")
        opcion=input("\t\t Elige una opción: ").upper().strip()
        return opcion

    def menu_registro():
        print("\n \t ..:: Registro en el Sistema ::..")
        nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
        apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
        email=input("\t Ingresa tu email: ").lower().strip()
        #password=input("\t Ingresa tu contraseña: ").strip()
        password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
        if not nombre or not apellidos or not email or not password:
            print(f"\n\tTodos los campos son obligatorios. Intenta de nuevo.")
            funciones.esperarTecla()
        #Agregar codigo
        resultado=usuario.registrar(nombre, apellidos, email, password)
        if resultado:
            print(f"\n\t{nombre} {apellidos} se registro correctamente, con el email {email}")
        else:
            print(f"\n\t...por favor intentelo de nuevo, no fue posible registrar al usuario")

    def menu_login():
        funciones.borrarPantalla()
        print("\n \t ..:: Inicio de Sesión ::.. ")     
        email=input("\t Ingresa tu E-mail: ").lower().strip()
        #password=input("\t Ingresa tu contraseña: ").strip()
        password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
        #Agregar codigo
        registro=usuario.iniciar_sesion(email,password)
        if registro:
            usuario.menu_notas(registro[0],registro[1],registro[2])
        else:
            print(f"\n\tEmail y/o contraseña incorrecta(s), vuelva a intentarlo...")

    def menu_notas():
        print("\n \t .::  Menu Notas ::. \n\t1.- Crear \n\t2.- Mostrar \n\t3.- Cambiar \n\t4.- Eliminar \n\t5.- Salir """)
        opcion = input("\t\t Elige una opción: ").upper().strip()
        return opcion   

    def main():
        opcion=True
        while opcion:
            funciones.borrarPantalla()
            opcion=usuario.menu_usuarios()

            if opcion=="1" or opcion=="REGISTRO":
                funciones.borrarPantalla()
                usuario.menu_registro()
                funciones.esperarTecla()

            elif opcion=="2" or opcion=="LOGIN": 
                usuario.menu_login()
                funciones.esperarTecla()
            
            elif opcion=="3" or opcion=="SALIR": 
                print("Termino la Ejecución del Sistema")
                opcion=False
                funciones.esperarTecla()
            else:
                print("Opcion no valida")
                opcion=True
                funciones.esperarTecla()

    def menu_notas(usuario_id,nombre,apellidos):
        while True:
            funciones.borrarPantalla()
            print(f"\n\t\t\tBienvenido {nombre} {apellidos}, has iniciado sesión ...")
            opcion=usuario.menu_notas()

            if opcion == '1' or opcion=="CREAR":
                funciones.borrarPantalla()
                print(f"\n\t.:: Crear Nota ::.")
                titulo=input("\tTitulo: ")
                descripcion=input("\tDescripción: ")
                if not titulo.strip() or not descripcion.strip():
                    print(f"\n\t El titulo y la descripcion no puede estar vacios.")
                    funciones.esperarTecla()
                    continue
                #Agregar codigo
                respuesta=nota.crear(usuario_id, titulo, descripcion)
                if respuesta:
                    print(f"\n\tSe creo la nota: {titulo} exitosamente")
                else:
                    print(f"\n\tNo fue posible crear la nota en este momento vuelve a intenter...")
                funciones.esperarTecla() 
            elif opcion == '2' or opcion=="MOSTRAR":
                funciones.borrarPantalla()
                #Agregar codigo
                lista_notas=nota.mostrar(usuario_id)
                if len(lista_notas)>0:
                    print(f"\n\tMostrar las Notas")
                    print(f"{'ID':<10}{'Titulo':<15}{'Categoria':<15}{'Descripcion':<15}{'Fecha':<15}")
                    print(f"-"*80)
                    for fila in lista_notas:
                        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
                        print(f"-"*80)
                else:
                    print(f"\n\tNo existen Notas de acuerdo al usuario")
                funciones.esperarTecla()
            elif opcion == '3' or opcion=="CAMBIAR":
                funciones.borrarPantalla()
                print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar una Nota ::. \n")
                id = input("\t \t ID de la nota a actualizar: ")
                titulo = input("\t Nuevo título: ")
                descripcion = input("\t Nueva descripción: ")
                if not id.isdigit():
                    print(f"\n\tEl ID debe ser un numero.")
                    funciones.esperarTecla()
                    continue
                #Agregar codigo
                respuesta = nota.cambiar(id,titulo,descripcion)
                if respuesta:
                    print(f"\n\tSe actualizo la nota: {titulo} exitosamente")
                else:
                    print(f"\n\tNo fue posible actualizar la nota en este momento vuelva a intentar...")
                funciones.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                funciones.borrarPantalla()
                print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
                id = input("\t \t ID de la nota a eliminar: ")
                if not id.isdigit():
                    print(f"\n\tEl ID debe ser un numero.")
                    funciones.esperarTecla()
                    continue
                #Agregar codigo
                respuesta = nota.borrar(id)
                if respuesta:
                    print(f"\n\tSe borro la nota: {id} exitosamente")
                else:
                    print(f"\n\tNo fue posible borrar la nota en este momento vuelva a intentar...")
                funciones.esperarTecla()
                funciones.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                break
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                funciones.esperarTecla()

    if __name__ == "__main__":
        main()