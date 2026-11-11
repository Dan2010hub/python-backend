# Data Types
# print("Hello World")  #String
# print(10) # Integer
# print(3.90) # float 
# print(True) # boolean
# print(None) # none

# Concatenation:
name = "Nelson"
print("His name is ", name)

# Data type conversion
print(type(38)) # use to check the type

print(float(37)) # it turned from int to float
print(str(34)) # it turns int to str
print(bool(0)) # turns o to a boolean which is false 


# varaibles in python 
userName = "Nelson"
age = 16

print("Hello i am " + userName+ " and I am " + str(age) + " years old")

# F string

name = "Chimdi"
age = 16

print(f"Hey i am {name}, and i am {age} years old")

# Input 

name = input("What is your name ")
print(f"Hello, {name}!")


print("Enter two numbers to perform addition operation")
num1 = int(input("Enter first number"))
num2 = int(input("Enter Second number"))
total = num1 + num2
print(f"the sum of {num1} and {num2} is {total}")

# Assignment operators:

x =5
print(x)

x +=3 # equivalent to x = x + 3
x -=3 # equivalent to x = x - 3
x *=3 # equivalent to x = x * 3
x /=3 # equivalent to x = x / 3
x %=3 # equivalent to x = x % 3
x **=3 # equivalent to x = x ** 3
print(x)


# Comparioson operators:

x = 5
y = 5

print(x ==y) # equal to
print(x !=y) # not equal to
print(x > y) # greater than 
print(x < y) # less than
print(x >= y) # greater than or equal to
print(x <= y) # less than or equal to

#Logical opeerators 

x = 10
y = 20
z = 30

print(x < y and y < z) # and operator
print(x < y or y < z) # or operator 
print(not(x < y)) # not operator


# Conditonal statments 

signal = input("Enter a signal (red, yellow, green):")

if signal == "red":
    print("stop")

elif signal == "yellow":
    print("Caution")

else: 
    print("Invalid signal")
