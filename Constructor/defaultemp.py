class Emp:
    def __init__(self):
        self.empId = int(input("your id : "))
        self.empName=(input("Name : "))
        self.empSalary=float(input("your salary : "))

    def display(self):
        print("Employee ID :", self.empId)
        print("Employee Name:", self.empName)
        print("Salary :", self.empSalary)

a1.display()

a1=Emp()
a2=Emp()
a3=Emp()


a2.display()
a3.display()

sal=[a1.empSalary,a2.empSalary,a3.empSalary]
highest_sal=max(sal)
print("\n Highest Salary : ",highest_sal)