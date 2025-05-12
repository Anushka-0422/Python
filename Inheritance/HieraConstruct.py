class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent called.", self.name)

    def show(self):
        print(self.name,"is the child class of Parent class")

class Child1(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print("Age: ",self.age)

class Child2(Parent):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def display(self):
        print("Grade: ",self.grade)

c1 = Child1("Anushka", 19)
c2 = Child2("Rohan", "A+")

c1.show()
c1.display()

c2.show()
c2.display()
