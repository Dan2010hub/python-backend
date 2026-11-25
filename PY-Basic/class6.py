# Function 
# Function are like containers that wraps a block of code together. 
# They're powerful because they enable code reusability, 
# and in python, functions are defined using the "def" keyword

def check_greatest(my_list):
    biggest = my_list[0]

    for m in my_list:
        if m > biggest:
            biggest = m

    print(f"the biggest number is: {biggest}")

check_greatest([54, 81, 23, 92, 34])


# Write the function that returns the cube of any number given to it

def cube_number(number):
    result = number * number * number
    print(result)

cube_number(4)

# write a function that takes a users name and greets the person 
def greet(name):
    print(f"Hello His Majesty {name}")

greet("Nelson")


