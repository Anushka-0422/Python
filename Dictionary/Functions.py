dict={"1":"Vaishu","2":"Rony","3":"Avi"}

#keys(): Returns all keys
print("keys of Dic : ",dict.keys())

#values(): Returns all values
print("values of dic : ",dict.values())

#items(): Returns key-value pairs
print("Items in dic : ",dict.items())

#clear(): Removes all elements
# print(dict.clear())

#copy(): Creates a shallow copy
copydata=dict.copy()
print(copydata)
copydata[4]="jyh"
print(copydata)

#get(key, default): Returns value of key if exists,else default
