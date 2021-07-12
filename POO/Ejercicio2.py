class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Lushy(Cat):
    def sing(self, sounds):
        return f'{sounds}'

mi_gatos= [Simon('Simon',4), Sally('Sally', 1), Lushy('Lushy', 3)]

mis_animales= Pets(mi_gatos)

mis_animales.walk()
print(mi_gatos[2].sing('nyan'))