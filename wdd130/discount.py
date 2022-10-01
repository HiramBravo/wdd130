from datetime import datetime
current_date = datetime.now()
day_of_week = current_date.weekday()
day_of_week = 2
discount_amount = 0.10
tax_amount = 0.06

print("Today is: " + str(current_date))
print(day_of_week)
print()
sub_total = float(input("Please enter the subtotal: "))
if (day_of_week == 1 or day_of_week == 2 ) and sub_total >= 50:
    discount = round(sub_total * discount_amount, 2)
    print(f"The discounts: ${discount:.2f}")
    sub_total -= discount
tax = round (sub_total * tax_amount, 2)
print(f"Sales tax amount: ${tax:.2f}")
print()
total = sub_total + tax
print (f"Total: {total:.2f}")


"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store's slowest sales days. On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.
"""
#Core requirements:
#Your program asks the user for the subtotal but does not ask the user for the day of the week. Your program gets the day of the week from your computer's operating system.
## Your program correctly computes and prints the discount amount if applicable.
## Your program correctly computes and prints the sales tax amount and the total amount due.
# Stretch Challenges
## If your team finishes the core requirements in less than an hour, complete one or more of these stretch challenges. Note that the stretch challenges are optional.

## Add code to your program that the computer will execute if today is Tuesday or Wednesday and the customer is not purchasing enough to receive the discount. This added code should compute and print the difference between $50 and the subtotal which is the additional amount the customer would need to purchase in order to receive the discount.
## Near the beginning of your program replace the code that asks the user for the subtotal with a loop that repeatedly asks the user for a price and a quantity and computes the subtotal. This loop should repeat until the user enters "0" for the price.

from datetime import datetime
current_day = datetime.now()
weekday = current_day.weekday()
price = 1
subtotal = 0

while price != 0:
    price = float(input("What is the price? $"))
    if price != 0:
        quantity = int(input("What is the quantity? "))
        subtotal += price * quantity
        # subtotal += subtotal
subtotal = round(subtotal,2)

discount_amount = 0
if weekday == 1 or weekday == 2:
    if subtotal >= 50:
        discount_amount = float(subtotal * .1)
        print(f"The discount is: ${discount_amount:.2f}")
    elif subtotal < 50:
        difference = 50 - subtotal
        print(f"If you buy ${difference:.2f} more, you'll get a discount.")
        discount_amount = 0

tax = (subtotal - discount_amount) * .06
total = subtotal - discount_amount + tax
print(f"Sales tax: ${tax:.2f}")
print(f"Total due: ${total:.2f}")



# if datetime.weekday == 1 or 2



# prices = []

# tax_rate = .0825

# savings = 0


# def receive_prices():
#     price = -1
#     while price != 0:
#         price = float(input("What is the price? "))
#         prices.append(price)


# def discount_prompt():
#     more = " "
#     subtotal = sum(prices)
#     difference = 50 - subtotal
#     if datetime.weekday == 1 or 2:
#         if more.lower() != "no":
#             subtotal = sum(prices)
#             if subtotal >= 50:
#                 discount = .1
#                 savings = subtotal * discount
#             else:
#                 while difference > 0:
#                     subtotal = sum(prices)
#                     difference = 50 - subtotal
#                     print(f"If you spend ${difference:.2f} more, you'll get a 10% discount!")
#                     more = input("Would you like to add more to the subtotal? Type 'yes' or 'no'. ")
#                     receive_prices()

# def print_totals():
#     tax = (subtotal - savings) * tax_rate
#     total = subtotal - savings + tax
#     if savings > 0:
#         print(f"Discount amount: ${savings:.2f}.")
#     print(f"Sales tax amount: ${tax:.2f}.")
#     print(f"Total due: ${total:.2f}.")


# subtotal = 0

# receive_prices()
# discount_prompt()
# print_totals()
#     # if subtotal >= 50:
#     #     discount = .1
#     #     savings = subtotal * discount

#     #     print(f"Discount amount: ${savings:.2f}.")
#     # else:
#     #     savings = 0
#     #     difference = 50 - subtotal
#     #     print(f"If you spend ${difference:.2f} more, you'll get a 10% discount!")
#     #     more = input("Would you like to add more to the subtotal? Type 'yes' or 'no'. ")
#     #     if more.lower() == "yes":
#     #         price = -1
#             # receive_prices()
