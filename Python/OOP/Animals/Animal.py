# Abstraction example/stage/pillar
class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in and one breath out")

    def eat(self):
        print("nom nom nom")

    def procreate(self):
        print("Time to find a mate")


# Instantiate an animal
cat = Animal()
# cat.breathe()
