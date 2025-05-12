#set :
#represeted by curly braces
#unordered(no indexing ,no slicing)
#don't allow duplicate values
#allow only unique value
#declaration: empty set : set = set()
#Initiallization :
mydata = {10,20,30,40,50,'ABC',60.45}

data={10,20,30,40,"ABC",5.8,10,20}
print(data)

#set operation
#add
data.add(100)
print(data)

#add more than one value
data.update({222,"XYZ",444})
print(data)

#remove single value
data.remove(20)
print(data)

#remove single value
data.discard(100000)       #if the value is not there it doesn't give any error message
print(data)

#set function
a={1,2,3,4,5,7,7,8,9}
b={10,11,12,13,14,15,16}

#merge both set
print(a.union(b))
#or
print(a | b)

#get common data
print(a.intersection(data))
#or
print(a & b)

#get difference
print(b.difference(a))
print(a.difference(b))
#or
print(b-a)

#length
print(len(a))

#check value is in set or not
print(112 in a)

#print set without bracket
for i in a :
    print(i,end="  ")