"""
Booleans chapter training w3 - True or False
"""
print(10 > 5)
print(9 > 10)
print(8 == 10)

a = 200
b = 33

if b > a:
    print("b is greater a")
else:
    print("b not greater a")
#Values with content are true
#Strings are true except EMPTY STRINGS
#Numbers are true except 0
#Lists, Tuples, Sets and Dictionaries are True except EMPTY
#None is False, False is False

#Object from class with a __len__() that returns 0 is False
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#Function can return Boolean
def myFunction() :
    return True
print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")
# isinstance() can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))
