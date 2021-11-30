# object
# in the create_class file, a "student" was defined
# here we'll create a student AKA an object

from create_class import Student

# Below is a "student" object
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Paige", "Art", 2.5, True)

print(student1.name)
#prints out the student1's name
print(student2.is_on_probation)
# prints out that student2 IS on probation
