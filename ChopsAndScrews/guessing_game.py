secret_number = 4
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int (input("Guess number from 1 - 9"))
    guess_count += 1

    if guess == 4:
        print("You have won!")
        break
else:
    print("Sorry! you ran out of guesses")