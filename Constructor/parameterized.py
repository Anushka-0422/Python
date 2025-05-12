class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("name :",self.name)
        print("age :", self.age)

p1 = Person("Rani",21)
p2 = Person("Tanuja", 21)
p3 = Person("Rutuja", 21)

p1.display()
p2.display()
p3.display()

class Anushka:
    def __init__(self,id,name):
        self.id = id
        self. name = name

    def display(self):
        print("id:",self.id )
        print("name:",self.id )

A=Anushka(1,"Rutu")
A1=Anushka(2,"Prachi")

A.display()
A1.display()


