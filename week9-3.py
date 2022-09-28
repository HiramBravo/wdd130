item = []
cost = []

name = None

print("Please add all the articles you want, when you finish write 'quit' please. ")

while name != "quit":
    name = input("What item would you like to add? ")
    if name != "quit":
        item.append(name)
print()
for item in item:
    print(f"'{item}' has been added to the cart")
