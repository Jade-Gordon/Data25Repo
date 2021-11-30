# We can create/define our own datatype - AKA class

# Let's create a student class
class Student:
# Initialise - define attributes after self
    def __init__(self, name, major, gpa, is_on_probation):
        # assign vals
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honour_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
