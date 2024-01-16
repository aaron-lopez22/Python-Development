loan_size = float(input("Loan size? "))
credit_score = float(input("How good is the credit score? "))
income = float(input("How high is your income? "))
down_payment = float(input("How large is your down payment? "))

should_loan = False

if loan_size >= 5:
    if credit_score >= 7 and income >= 7:
        should_loan = True
    elif credit_score >= 7 or income >= 7:
       if down_payment >= 5:
        should_loan = True
       else:
        should_loan = False
    else:
       should_loan = False
else:
    if credit_score < 4:
      should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print("the deicision is yes. this is a good loan.")
else:
    print("The decision is no. You should not loan this money.")
    
