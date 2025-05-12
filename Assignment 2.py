#1.Create a list with data 1,22,11,33,22, and 77,44 then count the number 22 in a given list.
list=[1,22,11,33,22,77,44]
print(list.count(22))

#2.Write a program to display the first and last colors from the following list. Given list
color_list = ["Red","Green","White" ,"Black"]
print(color_list)
print(color_list[3])
#or
print(color_list[-1])

#3.Write a Program to create a List of Numbers and find the sum of elements.
list2=[2,34,15,33,24,77,44]
print(list2)
print("Sum of the list : ",sum(list2))

#4.Create a Student list with atleast 10 names ask values from user and append the list with 10 Subjects .
# Perform the following on the List formed,
#i)remove the element at index 1
#ii)remove the last element
#iii)print the list in reverse order
std_list = []
for _ in range(4):
    name = input("Enter the name of student : ")
    std_list.append(name)

for  _ in range(4):
    subject = input("Enter the subject name : ")
    std_list.append(subject)

print(std_list)

# i) remove the element at index 1
del std_list[1]

# ii) remove the last element
std_list.pop() #removes last one element from the list

# iii) print the list in reverse order
std_list.reverse()
print("Reverse : ",std_list)

#5.Create a List with atleast 10 numbers and find the largest and smallest element in List.
list2=[2,34,15,33,24,77,44]
#min value

#max value
print("Maximum value from list : ",max(list2))

#6.Write a program to replace the last element in a list with another list.
A = [1, 2, 3, 4, 5]
B = [10, 20, 30]
A[-1:] = B
print("list with added another list :", A)

#7.Write a program to create a List and then insert the context “ Python is a language ” in the 3rd index.
color_list = ["Red","Green","White" ,"Black"]
color_list.insert(3, "Python is a language")
print(color_list)

#8 .Write a Program to Create a List with and check the element is present or not.
list2=[2,34,15,33,24,77,44]
print(33 in list2)

#9.Create a list with empId name salary taking input from user and then perform the action to update the name
emp_list = []
for i in range(3):
    emp_id=int(input("Enter your id : "))
    name=str(input("Enter your name : "))
    salary=float(input("Enter your salary : "))
    emp_list.append([emp_id, name, salary])

#before updating
print("\nEmployee List before update:")
print(emp_list)

emp_update = input("\nEnter the employee ID to update the name: ")
for emp in emp_list:
    if emp[0] == emp_update:
        emp[1] = input("Enter the new name: ")

print("\nEmployee List after update:")
print(emp_list)

#10.Write a program to take input from user and create a List as Languages and convert it to Tuples .Also try it vice versa.
# Taking input from user and creating a list
lang = input("Enter languages separated by spaces: ").split()

# Converting the list to a tuple
lang_tuple = tuple(lang)

#11. Create a List of your favorite songs. Then create a list of your favorite movies. Join the two lists together (Hint: List1 + List2).
# Finally,append your favorite book to the end of the list and print it.
song=[]
movies=[]
print("list",song+movies)

#12.Create a Set and add some data to it by taking it from the user and traverse it.Also perform the following operations:
#i)union
#ii)intersection
#iii)difference
my_set = set()
n = int(input("Enter the number of elements: "))

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    my_set.add(element)

print("\nThe set contains:", my_set)

# Traversing
print("\nTraversing the set:")
for item in my_set:
    print(item)
a={1,2,3,4,5,7,7,8,9}
b={10,11,12,3,14,5,16}

#merge both set
print(a.union(b))
#or
print(a | b)

#get common data
print(a.intersection(b))
#or
print(a & b)

#get difference
print(b.difference(a))
print(a.difference(b))
#or
print(b-a)

#14.Create a dictionary and values from List,Set and tuples.Create a List of colors...
# Creating a dictionary with values from List, Set, and Tuple
dict = {
    "list": [1, 2, 3, 4, 5],        # List as a value
    "set": {10, 20, 30, 40},  # Set as a value
    "tuple": ('a', 'e', 'i', 'o', 'u')  # Tuple as a value
}
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
print("\nDictionary with List, Set, and Tuple:")
for key, value in dict.items():
    print(f"{key}: {value}")

print("\nList of Colors:", colors)
