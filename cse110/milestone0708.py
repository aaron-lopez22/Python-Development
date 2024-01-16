'''
Aaron lopez 
cse 110
Milestone 07
'''



print("Welcome to the word guessing game!")

secret_word = "Burrito"

print("Your hint is: _ _ _ _ _ _ _")

guess = input("what is you guess? ")


guess_count = 1

while secret_word.lower() != guess.lower():
   print("Your guess was not correct")
   guess_count = guess_count + 1
   guess = input("what is you guess? ")


print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")


'''''
index = 0
while index < len(secret_word):
    for guesses in guess:
        for word in secret_word:
            if word.lower() == guesses.lower():
                print(word.upper(), end="")
                index = index + 1
            else:
                print("_", end="")
                index = index + 1
'''