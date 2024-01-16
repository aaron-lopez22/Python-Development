import random


keep_playing = "yes"
while keep_playing.lower() == "yes":

    number = random.randint(1, 100)


    guess = int(input("What is your guess? "))

    count = 1

    while guess != number:
        if guess > number:
            print("Lower")
            guess = int(input("What is your guess? "))
            count = count + 1

        else: 
            print("Higher")
            guess = int(input("What is your guess? "))
            count = count + 1


    print("You guessed it!")
    print(f"It took you this man guesses {count}.")
    keep_playing = input("Do you want to keep playing? (yes/no)")

print("The game is over.")
