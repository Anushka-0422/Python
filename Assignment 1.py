#Q.1 WAP to take two no from user and performs basic operations
a=int(input ("Enter 1st no.:"))
b=int(input ("Enter 2nd no.:"))
print("Addition:",(a+b))
print("Subtraction:",(a-b))
print("Multiplication:",(a*b))
print("Division:",(a/b))
print("Module:",(a%b))
print("Floor Div:",(a//b))
print("Power:",(a**b))

#Q.2 WAP to take input from user for empID,name,salary and print emp details
EmpID=int(input("\nenter your empID :"))
Name=str(input("enter your Name :"))
Salary=float(input("enter your Salary:"))
print("\nEmployee Details..!!!")
print("EmpID : ",EmpID)
print("Name : ",Name)
print("Salary : ",Salary)

#Q.3WAP to calculate the area of triangle.Ask input from user.
b=float(input("\nenter base :"))
h=float(input("enter height :"))
area=0.5*b*h
print("Base : ",b)
print("Height : ",h)
print("Area of triangle : ",area)

#Q.4 WAP to ask three subject marks from user & calculate the average
a=int(input("\nEnter english marks:"))
b=int(input("Enter python marks:"))
c=int(input("Enter web marks:"))
d=(a+b+c)/3
print("english=",a)
print("python=",b)
print("web=",c)
print("average=",d)

#Q.5 WAP to convert temperature into fahrenheit
fahrenheit=float(input("\nEnter temperature in fahrenheit : "))
Celsius=(fahrenheit-32)*5/9
print("Temperature in celsius : ",Celsius)

#Q.6 WAP to take year from user and find whether it is a leap year or not
Year=int(input("\nEnter Year :"))
if(Year%4==0):
    print("Entered year is Leap")
else:
    print("Entered year is not Leap")

#Q.7 WAP for marksheet
marks=float(input("\nEnter your marks :"))
if(marks>30 and marks<50):
    print("passed.")
elif (marks>=50 and marks<70):
    print("C Grade")
elif(marks>=70 and marks<90):
    print("B Grade")
elif(marks>=90 and marks<=100):
    print("A Grade")
else:
    print("Invalid marks..!!")

#Q.8 WAP to find the cube upto the given numbers by the users.
A=int(input("\nEnter a number : "))
N=1
while N<=A:
    print(f"The cube of {N} is {N**3}") #f=strings makes o/p clear & readable
    N+=1

#Q.9 WAP to find the sum of digits of a no.
n=int(input("\nEnter a number : "))
Sum=0
while n>0:
    digit=n % 10
    Sum+=digit
    n//=10
print(f"The sum of digits is : {Sum}")

#Q.10 WAP to find whether a no.entered by the user is a palindrome or not.
n=int(input("\nEnter a number : "))
original=n
reversed=0
while n>0:
    digit=n%10
    reversed=reversed*10+digit
    n//=10
if original==reversed:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")




