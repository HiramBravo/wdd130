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

