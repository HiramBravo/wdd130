print("Enter the names and balances of bank accounts (type: quit when done)")
names = []
balances = []

name = None

while name != "quit":
    name = input("What is the name of this account? ")

    if name != "quit":
        balance = float(input("What is the balance? "))

        names.append(name)
        balances.append(balance)

total = 0

print("Account information:")
for i in range(len(names)):
    print(f"{names[i]} - ${balances[i]}")

    total += balances[i]

average = total / len(balances)

print()
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")

highest_name = None
highest_balance = -1

for i in range(len(names)):
    name = names[i]
    balance = balances[i]
    
    if balance > highest_balance:
        highest_balance = balance
        highest_name = name
    
print(f"Highest balance: {highest_name} - ${highest_balance:.2f}")

change_account = "yes"

while change_account == "yes":
    change_account = input("Do you want to update? ")

    if change_account == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))

        balance[index] = new_amount
    print("Account Information:")
    for i in range(len(names)):
        print(f"{i}. {names[i]} - ${balances[i]:.2f}")