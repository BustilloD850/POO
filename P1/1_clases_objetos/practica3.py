import os
os.system("cls")

class Alumnos:
    def __init__(self, nombre, edad, matricula):
        self._nombre = nombre
        self._edad = edad
        self._matricula = matricula

    def inscribirse(self):
        pass
    
    def estudiar(self):
        pass


class Profesores:
    def __init__(self, nombre, experiencia, num_profesor):
        self._nombre = nombre
        self._experiencia = experiencia
        self._num_profesor = num_profesor

    def impartir(self):
        pass

    def evaluar(self):
        pass


class Cursos:
    def __init__(self, nombre, codigo, creditos):
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos

    def asignar(self):
        pass


# Crear objetos
alumno1 = Alumnos("Diego", 19, 12345)
alumno2 = Alumnos("Carlos", 20, 54321)

profesor1 = Profesores("Eduardo", 2, 9876)
profesor2 = Profesores("Enrique", 5, 5432)

curso1 = Cursos("Inglés", 100, 10)
curso2 = Cursos("Cálculo", 200, 5)


# Mostrar resultados
print(f"El alumno {alumno1._nombre} tiene {alumno1._edad} años y su matrícula es {alumno1._matricula}")
print(f"El alumno {alumno2._nombre} tiene {alumno2._edad} años y su matrícula es {alumno2._matricula}")
print(f"El profesor {profesor1._nombre} tiene experiencia {profesor1._experiencia} y su número de profesor es {profesor1._num_profesor}")
print(f"El profesor {profesor2._nombre} tiene experiencia {profesor2._experiencia} y su número de profesor es {profesor2._num_profesor}")
print(f"El curso {curso1._nombre} tiene el código {curso1._codigo} y sus créditos son {curso1._creditos}")
print(f"El curso {curso2._nombre} tiene el código {curso2._codigo} y sus créditos son {curso2._creditos}")