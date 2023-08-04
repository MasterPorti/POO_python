class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f'El estudiante {self.nombre} está estudiando')

estudiante1 = Estudiante('Juan', 20, 4)
print(estudiante1.estudiar())