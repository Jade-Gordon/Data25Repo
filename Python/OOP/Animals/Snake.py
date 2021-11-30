# Encapsulation example/stage/pillar

from Animals.Reptile import Reptile

class Snake(Reptile):
    # Snake inherits from Animal
    # -> Animal > Reptile > Snake
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = False
        self.venom = None # lets say by default, snakes have no venom
        self.limbs = False

    def use_tongue_to_smell(self):
        print("Do I say it smells or tastes nice")

sydney = Snake()
# print(sydney.cold_blooded)
# sydney.seek_heat() # this also acts as a print without having to type print

# Use __ to encapsulate