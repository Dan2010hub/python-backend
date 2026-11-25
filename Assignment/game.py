# Write a guess game, where you store a number 1 -10, 
# then propmt the user to guess the number you store, 
# if the user guesses right dispaly "success", 
# if not display "game over" on the third attempt

number = 9
guess_limit = 3
guess_count = 0 

while guess_count < guess_limit:
    guess = int(input("guess a random number from 1-10: "))
    guess_count += 1

    if guess == number:
        print("Success")
        break
    else:
        print(f"Game over you have {guess_limit-guess_count} tries left")

    


