# 1) Function to return the cube of a number
def cube(n):
    return n*n*n
n = int(input("Enter a number: "))
print("Cube:", cube(n))

# 2) Function to find area, circumference, and diameter of a circle
def circle(r):
    A = 3.14 * r * r
    C = 2 * 3.14 * r
    D = 2 * r
    return A, C, D

r= float(input("Enter radius: "))
A,C,D = circle(r)
print("Area:",A, "Circumference:",C, "Diameter:", D)

# 3) Calculator function (add, sub, mul, div)
def cal(a, b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum, sub, mul, div
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
sum, sub, mul, div=cal(a ,b)
print("Addition : ",sum)
print("Subtraction : ",sub)
print("Multiplication : ",mul)
print("Division : ",div)

# 4) Function to calculate Simple Interest
def interest(p,r,t):
    keyword= (p * r * t) / 100
    return keyword                     #return keyword argument
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
result = interest(p,r,t)
print("Simple Interest:",result)

# 5) Functions to calculate areas of figures
def tri_area(b, h=10):
    return 0.5 * b * h

def rect_area(l, b=5):
    return l * b

def square_area(s):
    return s * s

b = float(input("Enter base of triangle: "))
l = float(input("Enter length of rectangle: "))
s= float(input("Enter side of square: "))

print("Triangle Area:", tri_area(b))
print("Rectangle Area:", rect_area(l))
print("Square Area:", square_area(s))

