"""
Aaron Lopez
CSE 110
April 2022

"""

while True:

    print("Please enter the following: ")

# next lines will ask user for madlib words

    adjective = input("Adjective: ")
    animal = input("Animal: ")
    verb = input("Verb: ")
    exclamation = input("Exclamation: ")
    verb_two = input("Verb: ")
    verb_three = input("Verb: ")

# Story code

    print()
    print("Your story is: ")
    print()

    print(f"The other day, I was really in trouble. It all started when I saw a very")
    print(f"{adjective} {animal} {verb} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all")
    print(f"I could think to do was to {verb_two} over and over. Miraculously,")
    print(f"that caused it to stop, but not before it tried to {verb_three}")
    print(f"right in front of my family.")
    print()
    while True:
        answer = input("Run again and try differnet words?  (y/n): ")
        if answer in ('y', 'n'):
            break
        print("Invalid input.")
    if answer == 'y':
            continue
    else:
            print("Good bye")
            break
