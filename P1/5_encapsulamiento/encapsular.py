import os
os.system("cls")

class Clase:
    atributo_publico= "Soy un atributo publico"
    _atributo_protegido= "Soy un atributo protegido"
    __atributo_privado= "Soy un atributo privado"

    def __init__(self,color,tamanio):
        self.__color=color
        self.__tamanio=tamanio

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def tamanio(self):
        return self.__tamanio
    
    @color.setter
    def tamanio(self,tamanio):
        self.__tamanio=tamanio

    def _getAtributoPrivado(self):
        return self.atributo_protegido
    
    def getAtributoPrivado2(self):
        self.__atributo_privado()
    
    def setAtributoPrivado(self,atributo_privado):
        self.__atributo_privado=atributo_privado

#Usar los atributos y metodos de acuerdo a su encapsulamiento
objeto=Clase("Rojo","Grande")
print(f"Mi objeto tiene los siguientes atributos: {objeto.color} y {objeto.tamanio}")

print(f"Soy el contenido del atributo publico: {objeto.atributo_publico}")
print(f"Soy el contenido del atributo protegido: {objeto._atributo_protegido}")
print(f"Soy el contenido del atributo privado: {objeto._getAtributoPrivado2()}")
objeto.setAtributoPrivado("Se ha cambiado el valor del atributo privado")
print(f"Soy el contenido del atributo privado: {objeto.getAtributoPrivado()}")