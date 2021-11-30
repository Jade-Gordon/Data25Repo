# Polymorphism pillar/stage

from Snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False


peter = Python()
patty = Python()
patty.venom = True
print(peter.venom)
print(patty.venom)