class Parent:
    def show(self):
        print("Parent class")

class Child1(Parent):
    def display(self):
        print("First Child class")

class Child2(Parent):
    def display(self):
        print("Second Child class")

# Creating objects
c1 = Child1()
c2 = Child2()

c1.show()  # Inherited from Parent
c1.display()

c2.show()  # Inherited from Parent
c2.display()
