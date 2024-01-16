'''
Aaron Lopez
Milestone part 4
Python

price child floating
Adults meal floating
tax rat floating

num children integer
Number of adults integer
'''
# price of meals for adults and children this will be in floats

price_child = float(input("What is the price of a child's meal? "))
price_adult = float(input("What is the price of an adult's meal? "))

# Number of people for adults and children this will be in integers

number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there? "))

# Sales tax rate float

sales_tax_rate = float(input("What is the sales tax rate? "))

#creating the subtotal

meals_subtotal_children = price_child * number_children
meals_subtotal_adults = price_adult * number_adults
total_subtotal = meals_subtotal_adults + meals_subtotal_children

# creating sales tax

sales_tax = total_subtotal * sales_tax_rate/100

# computing the display total price

sales_total_price = sales_tax + total_subtotal


print()
print(f"Subtotal: ${total_subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${sales_total_price:.2f}")
print()


print()
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - sales_total_price
print(f"Change: ${change:.2f}")
print()

#calculating tip
tax1 = total_subtotal * .15
tax2 = total_subtotal * .20
tax3 = total_subtotal * .25

print(f"Suggested tip amount for 15 percent pre sales tax ${tax1:.2}")
print(f"Suggested tip amount for 20 percent pre sales tax ${tax2:.2}")
print(f"Suggested tip amount for 25 percent pre sales tax ${tax3:.2}")