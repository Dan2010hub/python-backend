# # Age checker with input

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")

# else:
#     print("You are not eligible to vote")

# # Even and odd number checker 

# num = int(input("Enter a number:  "))

# if num % 2 == 0 :
#     print("even number")

# else:
#     print("odd number")


# age = 30 
# if (age >= 65):
#     print("You are a senior citizen")
# elif (age >= 18 and age <= 64):
#     print("You are an adult")
# elif (age <= 18):
#     print("You are a minor")

# 
# mark = 90

# if (mark >=90):
#     print("A")
# elif(mark >=80 and mark <=89):
#     print("B")
# elif(mark >=70 and mark <=79):
#     print("C")
# elif(mark >=60 and mark <=69):
#     print("D")
# elif(mark >=50 and mark <=59):
#     print("E")
# else:
#     print("f")

# Three varaibles named num1, num2 and num3 are assigned values, the if statemtn checks which of the three numbers is the largest and prints the largest number

num1 = 20
num2 = 30
num3 = 70

if num1 > num2 and num1 > num3:
    print(f"{num1} is the Largest")
elif num2 >num1 and num2 > num3:
    print(f"{num2} is the Largest")
elif num3 > num2 and num3 > num1:
    print(f"{num3} is the largest")

else:
    print("All numbers are equal")
