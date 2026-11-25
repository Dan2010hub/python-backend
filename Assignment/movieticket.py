age = int(input("How old are you: "))
day = input("What day is it? ").lower()

if age < 12:
    price  = 8
elif age >= 65:
    price = 10
else:
    price = 15

if day == "wednesday":
    price = price -2
    print(f"Wednesday discount applied, Your ticket is ${price}")

else:
    print(f"No discount today, your ticket is ${price}")
