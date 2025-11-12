#archivo nota
from conexionBD import *
class Operaciones:
    @staticmethod
    def insertar(numero1,numero2,signo,resultado):
        try:
            sql="insert into operaciones (numero1,numero2,signo,resultado) values (%s, %s, %s, %s)"
            val=(numero1, numero2, signo, resultado)
            cursor.execute(sql,val)
            conexion.commit()
            return True
        except:
            return False
        
    def consultar(usuario_id):
        try:
            sql="select * from notas where usuario_id=%s"
            val=(usuario_id,)
            cursor.execute(sql,val)
            return cursor.fetchall()
        except:
            return []
        
    def actualizar(id, titulo, descripcion):
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

    def eliminar(id):
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