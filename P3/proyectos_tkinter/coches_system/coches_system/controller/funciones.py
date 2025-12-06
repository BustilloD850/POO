from conexionBD import *
from tkinter import messagebox
from model import autos,camiones,camionetas

#control app o controller

class funciones:
    class Autos:
        def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
            self._marca=marca
            self._color=color
            self._modelo=modelo
            self._velocidad=velocidad
            self._caballaje=caballaje
            self._plazas=plazas

        @property
        def marca(self):
            return self._marca

        @property
        def color(self):
            return self._color

        @property
        def modelo(self):
            return self._modelo

        @property
        def velocidad(self):
            return self._velocidad

        @property
        def caballaje(self):
            return self._caballaje

        @property
        def plazas(self):
            return self._plazas

        def insertar(self):
            try:
                cursor.execute(
                    "insert into coches values(null,%s,%s,%s,%s,%s,%s)",
                    (self._marca,self._color,self._modelo,self._velocidad,self._caballaje,self._plazas)
                )
                conexion.commit()
                return True
            except:
                return False
            
        @staticmethod   
        def consultar():
            try:
                cursor.execute("select * from coches")
                return cursor.fetchall()
            except:
                return []

        @staticmethod
        def actualizar(marca,color,modelo,velocidad,caballaje,plazas,id):
            try:
                cursor.execute(
                    "update coches set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s where id=%s",(marca,color,modelo,velocidad,caballaje,plazas,id)
                )
                conexion.commit()
                return True
            except:
                return False
            
        @staticmethod
        def eliminar(id):
            try:
                cursor.execute(
                    "delete from coches where id=%s",(id,)
                    )
                conexion.commit()
                return True
            except:
                return False

    class Camionetas:
        
        @staticmethod
        def insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
            try:
                cursor.execute(
                "insert into camionetas values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
                (marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
            )
                conexion.commit()
                return True
            except:
                return False
            
        @staticmethod   
        def consultar():
            try:
                cursor.execute("select * from camionetas")
                return cursor.fetchall()
            except:
                return []
            
        @staticmethod
        def actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id_camioneta):
            try:
                cursor.execute(
                    "UPDATE camionetas SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s WHERE id_camionetas=%s",
                    (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id_camioneta)
                )
                conexion.commit()
                return True
            except Exception as e:
                print("ERROR al actualizar camioneta:", e)
                return False

            
        @staticmethod
        def eliminar(id):
            try:
                cursor.execute(
                    "delete from camionetas where id_camionetas=%s",(id,)
                    )
                conexion.commit()
                return True
            except:
                return False

    class Camiones:
        
        @staticmethod
        def insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
            try:
                cursor.execute(
                "insert into camiones values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
                (marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
            )
                conexion.commit()
                return True
            except:
                return False

        @staticmethod   
        def consultar():
            try:
                cursor.execute("select * from camiones")
                return cursor.fetchall()
            except:
                return []

        @staticmethod
        def actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id):
            try:
                cursor.execute(
                    "UPDATE camiones SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, eje=%s, capacidadCarga=%s WHERE id_camion=%s",
                    (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id)
                )
                conexion.commit()
                return True
            except Exception as e:
                print("ERROR en actualizar:", e)
                return False

            
        @staticmethod
        def eliminar(id_camion):
            try:
                cursor.execute("DELETE FROM camiones WHERE id_camion=%s", (id_camion,))
                conexion.commit()
                return True
            except Exception as e:
                print("ERROR al eliminar:", e)
                return False