#Tuple
#immutable(can't modify,insert,remove)
#allow duplicacy
#store heterogeneous data

#without bracket considered :
# declaration= empty tuple Tuple=()

#Slicing :
tuple = (10,20,30,40,50)
print(tuple[0:2])
print(tuple[-4:-1])

t = ["we",20,"PQR",30,"ABC",40,50]
print(t[:])
print(t[0:])   #complete list
print(t[:-1])   #complete list

#length
print("Length : ",len(t))

#check given element in the list or not(using membership oper.)
print("PQR" in t)

#Traverse the list
for i in t :
    print(i,end="  ")

#printing single element repeatedly
t = (1,5,2,4,5)
for i in range (0,len(t)):
    if(t[i]==5) :
        print("\nindex of 5 : ",i)

