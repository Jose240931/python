class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad=edad
    def saludad(self):
        print(f"Hola {self.nombre}, tienes {self.edad} años!")

    @staticmethod
    def cambiarNombre(self,nuevoNombre):
        self.nombre = nuevoNombre