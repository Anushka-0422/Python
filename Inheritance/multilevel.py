class School:
    def __init__(self, name):  #with default Constructor
        print("School:", name)

class Student(School):
    def __init__(self, school, student, grade):         # #with parameterised Constructor
        super().__init__(school)
        print("Student: ",student, ", Grade: " ,grade)

class Exam(Student):
    def __init__(self, school, student, grade, subject, marks):
        super().__init__(school, student, grade)
        print("Exam:",subject, ", Marks: ",marks)

exam1 = Exam("ABC School", "Alice", "10th", "Math", 95)
