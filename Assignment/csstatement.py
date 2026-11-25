number = int(input("Enter number to check it's state: "))

if number % 2 == 0:
    print("Even number")

else:
    print("Odd number")

#
match number:
    case _ if number % 2 == 0:
        print("Even number")
    case _:
        print("Odd number")


#
checker = "Even number" if number % 2 == 0 else "Odd number"
print(checker)