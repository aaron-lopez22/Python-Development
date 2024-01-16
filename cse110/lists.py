


numbers = []
new_number = -1

sum_numbers = 0

while new_number != 0:

    new_number = int(input("Enter a list of number, type 0 when finished. "))
    numbers.append(new_number)


count = len(numbers)


for number in numbers:
    if number != 0:
        sum_numbers = sum_numbers + number
        average = sum_numbers / count


print(f"The sum is: {sum_numbers}")
print(f"the average is: {average}")
print({number})

