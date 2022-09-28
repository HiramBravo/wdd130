print("Please asnwer the following questions with a number from 1 to 10")
large_loan = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
payment = int(input("How large is your down payment? "))
should_loan = False
if large_loan >= 5:
    if credit >= 7 and income >= 7:
        should_loan = True
    elif credit >= 7 or income >= 7:
        if payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if credit < 4:
        should_loan = False
    else: 
        if income >= 7 or payment >= 7:
            should_loan = True
        elif income >= 4 and payment >= 4:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print("Your loan has been approved")
else:
    print("We are sorry but we cannot give you a loan  at the moment")
