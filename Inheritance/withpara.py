class person():
    def __init__(self,name): #parameterised constructor
        self.name=name

class student(person):               #student class inherites person
    def __init__(self,name):
        super().__init__(name)

student=student("Anushka")
print(student.name)