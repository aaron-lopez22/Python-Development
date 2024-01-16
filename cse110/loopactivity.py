'''
number = float(input("Please type in a positive number: "))


while number <= 0:
    print("Sorry, that is a negative number. Please try again.")
    number = float(input("Please type in a positive number: "))


print(f"The number is {number}")
'''

answer = input("May I have a piece of candy? ")

while answer.lower() != "yes":
    answer = input("May I have a piece of candy? ")



print("Thank you")