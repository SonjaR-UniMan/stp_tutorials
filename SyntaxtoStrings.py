"""
Python Syntax training and Operators tests
"""

print ("Hello,world!")

#indentation is important, standard is 4 space
if 5 > 2:
    print("Five is greater than two")
#but has to be not too extreme like line 13
if 5 > 2:
    print("Five is greater than two")
#            print("Five is still greater")
#Variables can be all types:
x = 5
y = "Hello, world"
print(x)
print(y)
#Comments are important like this or """ """
#Variables can be changed later and the latest is valid - are case sensitive (x is not X)
x = "Sally"
print(x)
print(y)
#Casting specifies variable types
x = str(7)
y = int(32.6)
z = float(8)
print(x)
print(y)
print(z)
#print of type gives class
print(type(y))
#Single and double quotes are the same in python
#Variable names may only contain A-z, 0-9 and _ NOT POSSIBLE: - or space or Number at beginning
#Use Camel Case Pascal Case or Snake Case
mySugr = "A Camel Case name"
MySugarFilm = "A Pascal Case name"
my_typical_filenames = "Snake Case names"
print(mySugr)
print(MySugarFilm)
print(my_typical_filenames)
# multiple values assignment
x, y, z = "Apple", "Orange", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)
# unpacking values - extracting from collection into variables
fruits = ["apple ", "banana ", "cherry "]
x, y, z = fruits
print(x)
print(y)
print(z)
#printing several variables into one line: using + means add space to str otherwise they are collated
print(x, y, z)
print(x + y + z)
# With the + numbers get added
# var types must not be string + number. The , takes all types and prints to one line
x = 5
print(x, y)
#global variables: outside of a function can be used by everyone - versus local variables
x = "awesome"
def myfunc():
    #global x
    x = "fantastique"
    print("Python is " + x)

myfunc()

print("Python is " + x)

#Numeric types are int float (with comma . or E or e) and complex
x = 3
y = 3+5j
z = -354.67e5
print(type(x))
print(type(y))
print(type(z))

#Conversion is possible, except from complex to anything. Specifying a variable type is called casting: int() or float() or str()
a = float(x)
b = int(z)
c = complex(z)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# Python module random: not a function - prints a random number in range

import random
print(random.randrange(1,10))

#Multiline strings: use triple quotes (egal welche) when assigning to variables
a = """Ein Werwolf eines Nachts entwich
von Weib und Kind 
und sich begab
an eines Dorfschullehrers Grab"""
print(a)
#String index is in [], beginning with 0
print(a[1])
#for loop prints each letter in separate lines
for x in "Cherry":
    print(x)
#determining the length len() function
print(len(a))
#determining "und" in string a returns boolean value and if loop can print info:
print("und" in a)
if "und" in a:
    print("Yes, 'und' is present.")
print("aber" not in a)
if "aber" not in a:
    print("No, 'aber' is NOT present.")

#String Slicing - position 1 is [0] and last position is never included!! Left out means from start or to end.
# Minus means from end where again the last character is not included though you have to write it.
b = "Hello, World!"
print(b[2:5])
print(b[2:])
print(b[:5])
print(b[-5:-1])

#print to upper or lower case:
print(b.upper())
print(b.lower())

a = "   Hello, World!   "
# .strip() removes whitespaces from beginning/end
print(a.strip())
# .replace("x", "y") replaces x with y
print(a.replace("W", "C"))
# .split(",") returns ["Hello", "World!"] splitting by the comma separator
print(a.split(","))

# String concatenation, add " " to enter a space
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)

#To combine in a print str and numbers use format() method sequence can be chosen by numbering from 0 to x
age = 48
hobbies = "singing"
sports = "swimming"
txt = "My name is Sonja, I am {0} and I like {2} and {1}"
print(txt.format(age, hobbies, sports))

#Escape characters to allow illegal characters in a string like ""
txt = "We are the \"Vikings\" from the north."
print(txt)



