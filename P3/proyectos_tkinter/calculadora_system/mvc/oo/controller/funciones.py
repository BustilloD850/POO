from tkinter import messagebox
from model import operaciones

#control app o controller
class funciones:
    @staticmethod
    def operaciones(n1,n2,signo):
        if signo=="+":
            ope=n1+n2
            tipo_ope="Suma"
        if signo=="-":
            ope=n1-n2
            tipo_ope="Resta"
        if signo=="x":
            ope=n1*n2
            tipo_ope="Multiplicacion"
        if signo=="/":
            ope=n1/n2
            tipo_ope="Division"
        messagebox.showinfo(title=tipo_ope,icon="info",message=f"{n1}{signo}{n2}={ope}")
        funciones.respuesta_sql(operaciones.Operaciones.insertar(n1,n2,signo,ope))

    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(title="Exito", icon="info", message=f".::Operacion realizada con exito::.")
        else:
            messagebox.showinfo(title="Error", icon="info", message=f".::Hubo en error al realizar accion::.")