

from datetime import datetime

current_date = datetime.now(tz=None)
weekday = datetime.weekday(current_date)
subtotal = float(input("Please enter the subtotal: "))

if subtotal < 50:
    subtotal_tax = .06 * subtotal
    new_total = subtotal_tax + subtotal
    print(f"Sales tax amount: {subtotal_tax: .2f}")
    print(f"Total: {new_total: .2f}")
elif weekday == 1 or weekday == 2:
        discount_tax =  .1 * subtotal
        new_subtotal = subtotal - discount_tax
        subtotal_tax = .06 * new_subtotal
        new_total = subtotal_tax + new_subtotal
        print(f"Dscount amount: {discount_tax: .2f}")
        print(f"Sales tax amount: {subtotal_tax: .2f}")
        print(f"Total: {new_total: .2f}")
else:
    subtotal_tax = .06 * subtotal
    new_total = subtotal_tax + subtotal
    print(f"Sales tax amount: {subtotal_tax: .2f}")
    print(f"Total: {new_total: .2f}")
