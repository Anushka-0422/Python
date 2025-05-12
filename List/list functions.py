Mylist = [10,456,30,23,20,30,50,60]

#find the min value
print("Minimum value from list : ",min(Mylist))

#find the max value
print("Maximum value from list : ",max(Mylist))

#find the sum value
print("Sum of values from list : ",sum(Mylist))

#sorting the list
#Mylist.sort()
#print(Mylist)

#reversing the list
#Mylist.reverse()
#print(Mylist)

#index()
print("Index no. of 456 is :",Mylist.index(456))

# count()
print("Count of 30 : ",Mylist.count(30))

# reverse()
Mylist.reverse()
print("Reverse : ",Mylist)

#reverse + sort = sorted original list
Mylist.sort(reverse=True)
print("sort list : ",Mylist)

#reverse + sorted = sorted original list& give new list
Mylist=sorted(Mylist,reverse=False)
print("Sorted list : ",Mylist)

