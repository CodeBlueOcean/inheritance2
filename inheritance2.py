# object is use as the parent class User(object)
class User:
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def _init_(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print()
      
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print()

wizard1 = Wizard('Merlin', 60)

# isinstance(instance, Class)
print(isinstance(wizard1, object))




