from Clases.Persona import Persona


class Alumno(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

