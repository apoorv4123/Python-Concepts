# print("My name is")
# print("Apoorv Srivastava")
# print("My name is","Apoorv Srivastava")

# print(23)
# print(23+35)

# --------------------------------------------------

# variable is a name given to a memory location in a program
# variable names should be simple, short and meaningful

# Identifiers (They are names...eg. a variable name or a function name, etc. is an identifier):
# Identifiers can be a combination of uppercase & lowercase letters, digits or an underscore.
# Identifiers cannot start with a digit
# Identifiers can be of any length
# We can't use special symbols in our identifiers like !,@#$%^&*()-+=


name = "Ajit"
age = 22
price = 25.66

# print(name)
# print(age)
# print(price)
# print("My name is : ", name, ", my age is : ", age)

age2 = age
# print(age2)

# print(type(name))
# print(type(age))
# print(type(price))

# Data types:
# Python automatically detects the type(datatype) of values
# Data Types in Python : Integer(int), String(str), Float(float), Boolean(bool), None(NoneType)
# String can be writtn in single quotes, double quotes and triple quotes
# Possible vaues of boolean = True/False
# Eg: a = None (means a ko koi value nhi di gyi)

name1 = 'as'
name2 = "as" #(preferable)
name3 = '''as'''
# print(name1, name2, name3)

flag = False
a = None
# print(type(flag))
# print(type(a))

# Keywords:
# Keywords are reserver words which cannot be used as identifiers
# and, as, assert, break, class, continue, def, del, elif, else, except, finally, False, for, from, global, if, import, in, is, lambda, nonlocal, None, not, or, pass, raise, return, True, try, with, while, yield

# Python is a case sensetive language


# Print Sum:
# a = 2
# b = 5
# sum = a + b
# print(sum)

# a = 3.4
# sum = a + b
# print(sum)

# https://www.geeksforgeeks.org/type-conversion-in-python/
# b = False 
# print(type(b))
# sum = a + b
# print(sum)

# a = "No"
# print(type(a))
# print(sum)


#  Comments: Non executable text
# 1. Single line comments start with #
# 2. Multi line comments are enclosed between {"""......."""}
"""
multi-line 
comment
"""


# Operators(Symbol that performs certain operations between operands):
"""
Arithematic Operators -> For mathematical operations: +,-,/,*,%,**
Relational/Comparison operators -> Return a boolean value : ==, !=, >, <, >=, <=
Assignment Operators: =, +=, -=, *=, /=, %=, **=
Logical Operators -> Operate on boolean values : not, and, or
"""

'''
a = 4
b = 2

sum = a + b # assigning sum to a variable
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) # remainder
print(a**b) # power
print(a+False) # just fyi

print(a == b)
print(a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)

num = 10
num += 10 # num = num + 10
print(num)

print(not False)
print(not True)
print(not (a > b))

val1 = True
val2 = False
print("and operator:", val1 and val2)
print("or operator:", val1 or val2)
print((a == b) or (a > b))
'''

#  Type Conversion : Converting the variable of one type to another 
'''
2 types of conversions are there in Python:
1. Type Conversion/Implicit: Python interpreter does ths automatically
2. Type Casting/Explicit:  We need to inform python that we are converting vatianle of one type of variable of another type
'''

"""
a = 2 # int
b = 4.25 # float

sum = a + b #When we are doing arithematic operations between int and float, python would automatically convert int to float(as float is superior as compared to int) as float can store more/extra data 
# So, above: sum = 2.0 + 4.25 -> Python automatically would've performed type

a1 = "2"
print(a1 + b) # Error as we can only concatenate str(not float) to str. Here python did not do automatic conversion
"""

'''
# Type Casting is done using several functions like: int(value) -> this would give out value as int, float(value) -> this would give out value as float, str(value)
a,b = 1,"2"
c = int(b)
d = float(b)
sum = a + c
print(sum)
sum = a + d
print(sum)
#  only numerical strings can be converted to float or int using type casting, we can't convert a character string to float value

a = 3.14
a = str(a)
print(type(a))
'''

'''
Type Casting Functions:
1. int(y [base]) -> converts y to an integer and base specifies the number base. For example, if you want to convert the string in decima numbers then you'll use 10 as base.
2. float(y) -> converts y to a floating point number
3. complex(real [imag]) -> creates a complex number.
4. str(y) -> converts y top a string
5. tuple(y) -> converts y to a tuple
6. list(y) -> converts y to a list
7. set(y) -> converts y to a set
8. dict(y) -> creates a dictionary and y should be a sequence of (key, value) tuples
9. ord(y) -> converts a character into an integer
10. hex(y) -> converts an integer to a hexadecimal string
11. oct -> converts an integer to an octal string
'''

# Input in python: Taking input from user in python
"""
input() statement is used to accept values (using keyboard) from the user at run-time
result for input is always a str. So, we need to use type casting based on the input we are desiring, as follows:
int( input()) # int
float( input() ) # float
"""

'''
name = input("enter your name: ")
print("Welcome: ", name)

val = input("Enter some value: ")
print(val, type(val)) # 99.99 <class 'str'>

name = input("enter name: ")
age = int(input("enter age: "))
marks = float(input("enter marks: "))
print("Name: ", name, ", Age: ", age, ", Marks: ", marks)
'''

# Practice problems:
'''
# Q: Write a program to input 2 number and print their sum:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is: ", a + b)

# Q: Write a program in input side of a square and print its area.
side = float(input("Side of square: "))
print("Area: ", side * side)

#  Q: Write a program to input two floating point numbers and print their average.
one = float(input("First number: "))
two = float(input("Second number: "))
print("Average: ", (one + two) / 2)

# Q: Write a program to input 2 int numbers a & b. Print True if a >= b. If not, print False.
a = int(input("first number: "))
b = int(input("second number: "))
print(a >= b)
'''