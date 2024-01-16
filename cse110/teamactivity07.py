'''
Assignment
date
teamactivity 07
Aaron Lopez
'''
'''
from turtle import end_fill


words = "commitment"
user_letter = input("What is your favorite letter? ")

for word in words:
    if word == user_letter:
        word = "_"
        print(word, end="")
    else:
       print(f'{word}', end="")

'''


words_pres = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
user_number = int(input("Please enter a number: "))

for i, words in enumerate(words_pres):
    if i % user_number == 0:
        print(words.capitalize(), end="")
    else:
            print(words, end="")