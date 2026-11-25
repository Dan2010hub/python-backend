password = "heyhelloxup"
password_count = 0
password_limit = 3

while password_count < password_limit:
    proposed_password = input("Enter Password: ")

    password_count += 1 

    if proposed_password == password:
        print("Password granted")
        break
    else:
        print(f"Wrong you have {password_limit - password_count} tries left")

    if password_count == password_limit and proposed_password != password:
        print("Account locked")


    


