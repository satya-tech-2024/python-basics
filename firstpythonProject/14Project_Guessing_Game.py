secret_number = 19
guess_count  = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("You guessed the secret number correct")
        break

else: # else for while
    print("You finished your guesses")