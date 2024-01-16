"""
Aaron Lopez
CSE 111 prove Milestone 1. Review python
"""

from datetime import datetime
import math

#settting up the date and time

current_date_time = datetime.now()


#gathering input from the users

width_tire = int(input("Enter the width of the tire in mm (ex 205): "))

aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))

diameter_tire = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#seperating equations into parts for my own understanding 

top_equation = (math.pi * (width_tire ** 2) * aspect_ratio) * (width_tire * aspect_ratio + (2540 * diameter_tire))

bottom_equation = 10000000000

v_liters = top_equation / bottom_equation

print(f"The approximate volume is {v_liters: .2f} liters")

#stretch for assignment. Does the user want to buy? if yes gather phone number. If no don't and print to txt file. 

user_choice = input("Do you want to buy the tires with the dimensions that were entered? (yes or no): ")

if user_choice.lower() == "yes":
    phone_number = input("Please enter your phone number: ")
    with open ("volumes.txt", "at") as volumes_file:
        print(f"{current_date_time:%y-%m-%d}, {width_tire}, {aspect_ratio}, {diameter_tire}, {v_liters: .2f}, {phone_number}", file = volumes_file)
else:
    with open ("volumes.txt", "at") as volumes_file:
        print(f"{current_date_time:%y-%m-%d}, {width_tire}, {aspect_ratio}, {diameter_tire}, {v_liters: .2f}", file = volumes_file)