#Creating a list
from codecs import replace_errors

Num=[1,22,11,33,22,77,44]
print(Num)

#Q1.count the number 22
print("count of 22 number : ",Num.count(22))

#Q2.WAP to print first & last color
color_list=["Red","Green","White","Black"]
print(color_list)

#Q3.WAP create list of numbers & find largest &smallest element
L1=[67,82,16,33,23]
print("max number of values from list : ",max(L1))

#find the sum value
print("minimum number of values from list : ",min(L1))

#4.Create a Student list with atleast 10 names ask values from user and append the
#list with 10 Subjects . Perform the following on the List formed,
#i)remove the element at index 1
#ii)remove the last element
#iii)print the list in reverse order
#initiallizing empty set for inserting values
stud=[]
for i in range(1,3,1):
    name=input("Enter student Name : ")
    sub=input("Enter sub : ")
    stud.extend([name,sub])

print("List of Student : ",stud)

#removing List value of Index 1
del stud[1]
print(stud)

del stud[-1]
print(stud)

stud.sort(reverse=True)
print(stud)

#5.Create a List with atleast 10 numbers and find the largest and smallest
#element in List.
List=[10,456,30,23,20,30,50,60,678,234]

print(max(List))
print(min(List))

#6.Write a program to replace the last element in a list with another list.
original_list=[10,456,30,23,20,30,50,60,678,234]
print(original_list)


replacement_list=[1,2,3,4]

original_list[-1]=replacement_list
print(original_list)

#7.Write a program to create a List and then insert the context "Python is a language"
# in the 3rd index.
a=["10","20","30","ABC","50","XYZ","60"]
a.insert(3,"Python is a language")
print(a)

#Q8.Write a Program to Create a List with and check the element is present
#or not.
# Create a list
my_list = [10, 20, 30, 40, 50]

# Element to check
element_to_check = 30

# Check if the element is present
if element_to_check in my_list:
    print(f"{element_to_check} is present in the list.")
else:
    print(f"{element_to_check} is not present in the list.")

#9.Create a list with empId name salary taking input from user and then perform
#the action to update the name
emp=[]
for i in range(1,3,1):
    empId=int(input("empId : "))
    Name=input("Enter Name : ")
    Salary=float(input("Enter your salary :"))
    emp.extend([empId,Name,Salary])

print("List of Student : ",emp)

#11. Create a List of your favorite songs. Then create a list of your
#favorite movies. Join the two lists together (Hint: List1 + List2). Finally,
#append your favorite book to the end of the list and print it.
Songs=['Kakan','Gulabi sadi','Zingat']
Movies=['Kalaki','Genius','Hi papa']

print("List :",Songs+Movies)