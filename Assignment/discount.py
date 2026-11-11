amount = int(input("Enter amount: "))

if amount > 10000:
    discount = amount - 1000
    print(f"You are eligible for a discount of 1000,You are to pay {discount}")

elif amount >=5000 and amount <= 10000:
    discount = amount - 500
    print(f"You are eligible for a discount of 500, You are to pay {discount}")

else:
    print("You are not eligible for a discount")

