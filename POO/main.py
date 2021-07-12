class PlayerCharacter:
    membership = True #class object atribute
    def __init__(self, name, age) -> object:  # constructor
        if(self.membership):
            self.name = name
            self.age = age

    def run(self):
        return "run"

    def Presentarse(self):
        return (f'mi nombre es {self.name}')


player1 = PlayerCharacter('Vicente', 27)

print(player1.age)
print(player1.run())
print(player1.Presentarse())

