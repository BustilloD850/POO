from tkinter import messagebox
from model import usuario,nota
from view import view1

class Controlador:
    @staticmethod
    def registro(nombre,apellidos,email,password):
        resultado=usuario.Usuario.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon='info',message=f"{nombre}{apellidos}, se registro correctamente con el email: {email}",title="Usuarios")
        else:
            messagebox.showinfo(icon='info',message=f"** por favor intentelo de nuevo, no fue posible insertar el registro **...",title="Usuarios")

    @staticmethod
    def inicio_sesion(ventana,email,password):
        registro=usuario.Usuario.registrar(email,password)
        if registro:
            messagebox.showinfo(icon="info", message=f".:: {registro[1]}{registro[2]}, iniciaste sesion correctamente ::.",title="Usuarios")
            view1.View.menu_nota(ventana, registro[0],registro[1],registro[2])
        else:
            messagebox.showinfo(icon="info",message=f"** Email y/o contraseña incorrectas... Vuelva a intentarlo", title="usuarios")

    @staticmethod
    def crear_nota(usuario_id,titulo, descripcion):
        respuesta=nota.Nota.crear(usuario_id,titulo, descripcion)
        Controlador.respuesta_sql(respuesta)

    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(icon='info',message="Operación realizada correctamente",title="Notas")
        else:
            messagebox.showinfo(icon='info',message="** por favor intentelo de nuevo, no fue posible insertar el registro **...",title="Usuarios")
