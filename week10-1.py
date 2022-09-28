print("Please enter the items of the shopping list (type: quit to finish): ")

list = []
item = None

while item != "quit":
    item = input("Item: ")

    if item != "quit":
        list.append(item)
    
print("The shopping list is:")
for item in list:
    print(item)

print("The shopping list with indexes is:")
for i in range(len(list)):
    item = list[i]
    print(f"{i}. {item}")

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")
print()
list[index] = new_item

print("The shopping list with indexes is:")
for i in range (len(list)):
    item = list[i]
    print(f"{i}. {item}")