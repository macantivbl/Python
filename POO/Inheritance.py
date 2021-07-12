class User():
    def sig_in(self):
        print('logged in')

    def __init__(self, email):
        self.email = email

class Mago(User):
    def __init__(self, nombre, poder, email):
        super().__init__(email)
        self.nombre = nombre
        self.poder = poder
    def ataque(self):
        return self.poder

class Arquero(User):
    def __init__(self, nombre, flechas):
        self.nombre = nombre
        self.flechas = flechas
    def ataque(self):
        return (f'ataquando con flechas {self.flechas}')

def jugador_ataqua(personaje):
    personaje.ataque()

mago1 = Mago('Merlin', 50, 'macantivbl@gmail.com')
arquero1 = Arquero('Robin', 34)
print(mago1.ataque())
print(arquero1.ataque())

print(isinstance(mago1,Mago))

print(jugador_ataqua(mago1))

print(mago1.email)


