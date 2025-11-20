import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_operaciones_basicas'
    )

    cursor=conexion.cursor(buffered=True)
except:
    print(f"Ocurrio un error con el Sistema")