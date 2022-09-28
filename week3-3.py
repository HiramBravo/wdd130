price_child = float (input("What is the price of a child´s meal? "))
price_adult = float (input("What is the price of an adult´s meal? "))
children = int (input("How many children are there? "))
adult = int (input("Howmany adults are there? "))
tax = int (input("What is the sales tax rate? "))
print(" ")
sub_total = price_child * children + price_adult *adult
print(f"Subtotal: ${sub_total:.2f}")
sales_tax = sub_total * tax / 100
print(f"Sales Tax: ${sales_tax}")
tip = float (input("How much do you want to tip? "))
total = sub_total + sales_tax + tip
print(f"Total: ${total}")
print(" ")
payment = float (input("What is the payment amount? "))
Change = payment - total
print(f"Change: ${Change:.2f}")