#Python Dictionary
#It consists of key and values
#Key : unique/immutable
#Value : can be duplicate/mutable
#use : to store data in structured way(quick access & modification)

#Syntax : dict ={"K1":"V1","K2":"V2"}
#eg.
my_dict={"name":"Vaishu","age":"9","city":"Pune"}
print(my_dict)

#Access
print(my_dict["name"])

#Add/update
my_dict.pop("city")
print(my_dict)

#delete
del my_dict["age"]
print(my_dict)

dict={"1":"Vaishu",2:"Rony","3":"Avi"}
#Iteration
for key,value in dict.items():
    print(key,value)

