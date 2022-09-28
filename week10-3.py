cart = []
balances = []

while True:
    print('''
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit''')
    print()
    action = input("Please enter an action: ")
    print()
    # add item
    if action == "1":
        item = input("What item would you like to add? ")
        cart.append(item)
        price = float(input(f"What is the price of '{item}'? "))
        balances.append(price)
        print(f"'{item}' has been added to the cart.")

    # view cart
    elif action == "2":
        total = 0
        print("The contents of the shopping cart are:")
        print()
        for i in range(len(cart)):
            item = cart[i]
            print(f"{cart[i]} - ${balances[i]:.2f}")

            total += balances[i]
        average = total / len(balances)

    # remove item
    elif action == "3":
        remove = int(input("Which item would you like to remove? "))
        cart.remove(item)
        print("Item removed.")

    # compute total EN ESTE MARCA ERROR
    elif action == "4":
        total = 0
        for i in range(len(cart)):
            item = cart[i]

            total += balances[i]
        average = total / len(balances)
        print(f"The total price of the items in the shopping cart is ${average}")

    # quit
    elif action == "5":
        print("Thank you. Goodbye.")
        break 


