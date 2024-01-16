'''
Aaron Lopez
milestone 09 and 10
cse 110
'''


print("Welcome to the Shopping Cart Program!")


print()
print("Please select one of the following:")
print("1. Add item")
print("2. View cart")
print("3. Remove item")
print("4. Compute total")
print("5. Quit")


userinput = 0

items = []
prices = []

total = 0


while userinput != 5:
    userinput = int(input("Please enter an action: "))
    if userinput == 1:
        item = input("What item would you like to add? ")
        items.append(item)
        price = float(input(f"what is the price of '{item}'? "))
        prices.append(price)
        print(f"'{item}' has been added to the cart.")
    elif userinput == 2:
        print("The contents of the shopping care are: ")
        for i in range(len(items)):
            i_items = items[i]
            i_prices = prices[i]
            i += 1
            print(f" {i}. {i_items} - ${i_prices: .2f}")
    elif userinput == 3:
        remove_item = int(input("Which item would like to remove? "))
        remove_item -= 1
        for i in range(len(items)):
            if remove_item <= i:
                items.pop(remove_item)
                prices.pop(remove_item)
                print("Item removed.")
            else:
                print("You have made an invalid choice")
    elif userinput == 4:
        for i in range(len(items)):
            total += prices[i]
        print(f"The total price of the items in the shopping car is ${total: .2f}")
    else:
         print("Thank you. Goodbye.")          
