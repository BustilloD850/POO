#archivo nota
from conexionBD import *
import datetime

class Nota:
    @staticmethod
    def crear(usuario_id, titulo,descripcion):
        try:
            fecha=datetime.datetime.now()
            sql="insert into notas (usuario_id, titulo,descripcion,fecha) values (%s, %s, %s, %s)"
            val=(usuario_id, titulo, descripcion,fecha)
            cursor.execute(sql,val)
            conexion.commit()
            return True
        except:
            return False
        
    def mostrar(usuario_id):
        try:
            sql="select * from notas where usuario_id=%s"
            val=(usuario_id,)
            cursor.execute(sql,val)
            return cursor.fetchall()
        except:
            return []
        
    def cambiar(id, titulo, descripcion):
        try:
            cursor.execute("SELECT * FROM notas WHERE id=%s", (id,))
            nota_existente = cursor.fetchone()
            if nota_existente:
                cursor.execute("UPDATE notas SET titulo=%s, descripcion=%s, fecha=NOW() WHERE id=%s",
                            (titulo, descripcion, id))
                conexion.commit()
                return True
            else:
                return False
        except:
            return False

    def borrar(id):
        try:
            cursor.execute("SELECT * FROM notas WHERE id=%s", (id,))
            nota_existente = cursor.fetchone()
            if nota_existente:
                cursor.execute("DELETE FROM notas WHERE id=%s", (id,))
                conexion.commit()
                return True
            else:
                return False
        except:
            return False