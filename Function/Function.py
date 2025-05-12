no = 3

def square():  #declaration
    sq=no**2       #defination
    print(sq)
square()        #call

#function with return type
def cube (no):
    return no**3
print("Hello")

print(cube(no))

#function
def add(n1,n2):
    print("Addition :",n1+n2)

add(10,20)

#2.Named
def sub(n1,n2):
    return n1-n2
print("Substraction :",sub(n1=20,n2=10))

#3.default value
def mul(n1=10,n2=20):
    print("multiplication :",n1*n2)
mul(n1=50,n2=50)
mul(n1=100,n2=200)

#4.Variable
def loop(*p):
    for i in p:
        print(i)
loop(1,2,3,4,5,6,7,8,9,10,11,12)
