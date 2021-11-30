# Inheritance example/stage/pillar

# "Reptile" is a more specific animal
# From the Animal file, import the Animal class
from Animals.Animal import Animal

class Reptile(Animal):

    def __init__(self):
        # super() refers to the class above: Animal
        # Animal is the parent class, while Reptile is the child
        super().__init__()
        self.cold_blooded = True
        self.heart_chamber = [3, 4]
        self.eggs = "Yes"

#  Methods
    def seek_heat(self):
        print("It's chilly, where's the sun?")

    def use_venom(self):
        print("if I've got it, I'm using it!")

    def attract_mate_through_scent(self):
        print("time to throw the eau de toilette")


jeremy_the_reptile = Reptile()
#
# print(jeremy_the_reptile.eggs)
# print(jeremy_the_reptile.alive)
# jeremy_the_reptile.attract_mate_through_scent()
# jeremy_the_reptile.breathe()

