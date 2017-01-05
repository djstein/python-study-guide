class Dog():
    kind = 'canine'    # class variable shared by all instances

    # init must take argument if given
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = []

    def add_tricks(self):
        self.tricks.append('sit')


class BigDog(Dog):
    
    def add_tricks(self):
        self.tricks.append('eat turkey')

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.name)
big = Dog('Pupper')
big.add_tricks()
print(big.tricks)