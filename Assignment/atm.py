balance = 500.00
fee = 1.50

withdrawal = float(input("How much do you want to withdraw? "))

if withdrawal % 10 != 0:
    print("Error withdrawal must be a multiple of 10")
elif withdrawal + fee > balance:
    print("Insufficent funds")

else:
    balance = balance - withdrawal - fee
    print(f"Withdrawal successful, your new balance is ${balance}")
