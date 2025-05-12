class college:
    clg_name=''

    def input_clg(self):
        self.clg_name=input("Enter your college name : ")

class school:
    school_name =''

    def input_sch(self):
        self.sch_name=input("Enter your School name : ")

class stud(college,school):

    stud_name = 'Anushka'
    age = 20

    def stud_info(self):
        self.stud_name=input("Enter Student Name : ")
        self.age = int(input("Enter student Age :"))

    def display(self):
        print("School Name : ")
        print("College  Name : ")
        print("Student Name : ")
        print("Student Age : ")

ob=stud()
ob.input_clg()
ob.input_sch()
ob.display()


