user_number = float(input("What is the first number? "))
user_number2 = float(input("What is the second number? "))

if user_number > user_number2:
    print("The first number is greater")
    print("The numbers are not equal")
    print("The second number is not greater")
elif user_number == user_number2:
    print("The first number is not greater")
    print("The numbers are equal")
    print("The second number is not greater")
else:
    print("The first number is not greater")
    print("The numbers are not equal")
    print("The second number is greater")
    
print()

animal = "Monkey"
user_animal = input("What is your favorite animal? ")
if animal== user_animal.capitalize():
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")