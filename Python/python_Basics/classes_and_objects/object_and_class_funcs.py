# # we can create FUNCTIONS
# from create_class import Student
#
# student01 = Student("Oscar", "Accounting", 3.1, False)
# student02 = Student("Phyllis", "Business", 3.8, False)
#
# print(student01.on_honour_roll())
# print(student02.on_honour_roll())

# w3schools Inheritance exercise
# Parent class
class Person:
    def __init__(self, fname):
        self.firstname = fname
    # Method
    def printname(self):
        print(self.firstname)

# child class -> Student class inherits from the Person class
class Student(Person):
    pass

x = Student("Mike")
x.printname() # this prints Mike, as the printname method says:
#               print(self.firstname)