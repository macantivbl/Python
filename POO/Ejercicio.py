class Gato:
    specie = 'mamimero'
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def EdadGatito(*numero):
    return max(numero)


gatito0 = Gato('Lushi', 4)
gatito1 = Gato('Pelusa', 2)
gatito2 = Gato('Boni', 3)

x = EdadGatito(gatito0.edad,gatito1.edad,gatito2.edad)
print(x)