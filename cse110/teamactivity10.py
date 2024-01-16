

accoount_names = []
balances = []

name = ""
balance = 0

while name != 'quit':
    name = input("What is the name of this account? ")
    
    

    if name != 'quit':
        balance = float(input("What is the balance? "))
        accoount_names.append(name)
        balances.append(balance)

print("Account Information:")

total = 0
average = 0

for i in range(len(accoount_names)):
    inames = accoount_names[i]
    ibalance = balances[i]
    print (f"{inames} - ${ibalance}")

    total += balances[i]
    average = total / len(balances)

    

print(F"Total: ${total: .2f}")
print(f"AVerage: {average:.2f}")