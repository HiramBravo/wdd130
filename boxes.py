import math
items = int(input("Type the number of manufactured items "))
box = int(input("Type the number of items that the user will pack per box "))
num_box = math.ceil(items / box )
print()
print(f"For {items} items, packing {box} items in each box, you will need {num_box} boxes")