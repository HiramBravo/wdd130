quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
again = "yes"
while again == "yes":
    number = int(input("Please enter a number: "))
    for i, letter in enumerate(quote):
        if i % number ==0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    print()
    again = input("Would you like to enter another number? yes/no ")
print("Goodbye")