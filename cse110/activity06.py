
rideable = False

age_rider1 = int(input("What is the age of the first rider? "))
height_rider1 = int(input("What is the height of the first rider? "))
rider2 = input("Is there a second rider (yes/no)? ")



if rider2.lower() == "yes":
    age_rider2 = int(input("what is the age of the second rider? "))
    height_rider2 = int(input("What is the height of the second rider? "))






if age_rider1 >= 18:
    if height_rider1 >= 62:
            rideable = True
    elif height_rider1 >= 36:
        if rider2.lower() == "yes" and age_rider2 >= 18:
            rideable = True
        else:
            rideable = False
else:
    if rider2.lower() == "yes" and age_rider2 >= 18:
        rideable = True
    else:
        rideable = False

if rideable:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")

          

