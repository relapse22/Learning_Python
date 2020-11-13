class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")
        return 'done'


player1 = PlayerCharacter('Max', 10)
player2 = PlayerCharacter('Abs', 18)

print(player1.name)
print(player1.age)
print(player1.run())

print(player2.name)
print(player2.age)


