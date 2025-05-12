#1.Create Company class with a parameterized constructor with companyName
#2.Create Department class with Parameterized constructor having dname.
#3.Create Developer class with parameterized constructor language Write a function to print CompanyName,dName,and language.

class Company:
    def __init__(self, CompName):
        self.CompName = CompName

class Department(Company):
    def __init__(self, CompName, dname):
        super().__init__(CompName)
        self.dname = dname

class Developer(Department):
    def __init__(self, CompName, dname, Lang):
        super().__init__(CompName, dname)
        self.Lang = Lang

    def display(self):
        print("***Developer Details***")
        print("Company Name:", self.CompName)
        print("Department Name:", self.dname)
        print("Used Language:", self.Lang)

dev = Developer("Microsoft", "AI Research", "Python")
dev.display()

#4.Create Tester class with parameterized constructor noOfTestCases. Write a function to display companyName,deptName and noOfTestCases
class Company:
    def __init__(self, CompName):
        self.CompName = CompName

class Department(Company):
    def __init__(self, CompName, dname):
        super().__init__(CompName)
        self.dname = dname

class Tester(Department):
    def __init__(self, CompName, dname, NoOfTestCases):
        super().__init__(CompName, dname)
        self.NoOfTestCases = NoOfTestCases

    def display(self):
        print("\n***Tester Details***")
        print("Company Name:", self.CompName)
        print("Department Name:", self.dname)
        print("No.Of Test Cases:", self.NoOfTestCases)

dev = Tester("Microsoft", "AI Research", "120")
dev.display()

#5.Create Management class with parameterized constructor having typeOfManagement
#6.Create Manager class with parameterized constructor having noOfProjects Write a function to display cmpName,deptName,typeOfManagement,noOfProjects
class Company:
    def __init__(self, CompName):
        self.CompName = CompName

class Department(Company):
    def __init__(self, CompName, dname):
        super().__init__(CompName)
        self.dname = dname

class Management(Department):
    def __init__(self, CompName, dname, typeOfManagement ):
        super().__init__(CompName, dname)
        self.typeOfManagement = typeOfManagement

class Manager(Management):
    def __init__(self, CompName, dname, typeOfManagement, NoOfProject):
        super().__init__(CompName, dname, typeOfManagement)
        self.NoOfProject = NoOfProject

    def display(self):
        print("\n***Manager Details***")
        print("Company Name:", self.CompName)
        print("Department Name:", self.dname)
        print("Type Of Management:", self.typeOfManagement)
        print("No.Of Projects:", self.NoOfProject)

dev = Manager("Microsoft", "AI Research", "e-Management",20)
dev.display()

#7.Create HR class with parameterized constructor with noOfIncentives. Write a function to display cmpName,deptName,typeOfManagement, noOfIncentives
class Company:
    def __init__(self, CompName):
        self.CompName = CompName

class Department(Company):
    def __init__(self, CompName, dname):
        super().__init__(CompName)
        self.dname = dname

class Management(Department):
    def __init__(self, CompName, dname, typeOfManagement ):
        super().__init__(CompName, dname)
        self.typeOfManagement = typeOfManagement

class HR(Management):
    def __init__(self, CompName, dname, typeOfManagement, NoOfRecruiters):
        super().__init__(CompName, dname, typeOfManagement)
        self.NoOfRecruiters = NoOfRecruiters

    def display(self):
        print("\n***Human Resources Details***")
        print("Company Name:", self.CompName)
        print("Department Name:", self.dname)
        print("Type Of Management:", self.typeOfManagement)
        print("No.Of Recruiters:", self.NoOfRecruiters)

dev = HR("Microsoft", "AI Research", "e-Management",90)
dev.display()

