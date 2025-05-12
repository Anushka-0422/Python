#List=mutable,ordered,indexing=0,store heterogenous data
#declaration: list=[]
#initiallization
list = [1,2,3,4,5]
print(list)
print(list[0:4])
print(list[-3:-2])
print(list[0:])   #complete list
print(list[:-1])   #complete list without last index
print(list[::-1])  #reverse the list

#list operation
list1 = ["we",2,"PQR",3,"ABC",4,5]
list2 = [1,2,"dgs",4,"cby"]

#Merging lists
newlist = list1 + list2
print(newlist)

#length
print("Length",len(newlist))

#check given element in the list or not(using membership oper.)
print(30 in list1)

#Traverse the list
for i in newlist :
    print(i,end="  ") #to print element horizonatally

#printing single element repeatedly
list = [1,2,[3]*5,4,5]
print(list)

#list manupulation
a = ["we",2,"PQR",3,"ABC",4,5]

#Replace
a[3]="python"
print(a)

#append : add single value at last
a.append(999)
print(a)

#extend : add multiple value at the end
a.extend([34,"pfb",999])
print(a)

#insert : at random index
a.insert(2,786)
print(a)

#remove
a.remove('ABC')
print(a)

