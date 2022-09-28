import random
keep = "yes"
while keep == "yes":
    number = random.randint(1, 100)
    guess_count = 0
    guess = -1
    while guess != number:
        guess = int(input("Guess the number:"))
        guess_count = guess_count + 1
        if guess < number :
            print("Higher")
        elif guess > number :
            print("Lower")
        else:
            print("You guessed it!")
    print(f"It took you {guess_count} guesses")
    keep = input("Would you like to plain again (yes/no) ").lower()
print("Thank you for playing.")
#02 Prepare: Preparation Material ( size format )