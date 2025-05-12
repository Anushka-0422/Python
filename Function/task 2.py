class Person:
    def inputPerson(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

    def displayPerson(self):
        print("Name:", self.name)
        print("Age:", self.age)

person1 = Person()
person2 = Person()

print("Enter details for Person 1...")
person1.inputPerson()

print("\nEnter details for Person 2...")
person2.inputPerson()

print("\nDetails of Person 1:")
person1.displayPerson()

print("\nDetails of Person 2:")
person2.displayPerson()
