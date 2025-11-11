from tkinter import messagebox

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