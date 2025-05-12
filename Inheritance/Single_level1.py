class college():
    clg_name = 'ICMS'
    clg_loc = 'Pandhrpur'
    clg_std_no = 0

    def info(self):

        name = ''
        age = ''

class student(college):

    name = ''
    age = ''

    def display(self):
            self.name = input("Enter student name : ")
            self.age = int(input("Enter student Age : "))
            print("College Name : ",self.clg_name)
            print("college location : ",self.clg_loc)


a = student()
a.info()
