import random
word = ("airplane")
guess_count = 0
guess = -1
guess_letter =[]
keep = ("yes")
print("Welcome to the world guessing game!")
print("Your hint is:","_" * len(word))
while keep == "yes":
    while guess != word:
        guess = input("What is your guess? ")
        guess_count = guess_count + 1
        for letter in word:
            if letter.lower()==guess.lower():
                print(letter.upper(),end="")
            elif guess.lower() in word:
                print(letter.lower(),end="")
            else:
                print("_",end="")    
    print("Congratulations! You guessed it!")
    print(f"It took you {guess_count} guesses")
    keep = input("Would you like to plain again (yes/no) ").lower()
print("Thank you for playing.")

