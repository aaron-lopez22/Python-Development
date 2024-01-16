from random import randint
import string
import random
#program will be a random password generator with custom inputs from the user.

#calling in the main function
def main():
    #try is to make sure that a yes or no is entered into the program other wise an error will appear.
    try:
        print("This is a random passord generator.")
        print("This password generator will allow you customize your password so that you can meet the password requirements set by a website.")
        print("If you do not want to create your own password you can type in 'no'. This will create a random password made out of 9 characters.")
        print()
    
    #letting the user decide whether they want to make a password or just have one created for them
        user_decision = input("Would you like to customize your password? ")
        print()

    #if statement to let the user choose the amount of characters or no to assign a preset amount
        if user_decision.lower() == "yes":

            lower_amount = int(input("How many lower case Letters will your password need? "))
            upper_amount = int(input("How many upper case letters will your password need? "))
            symbol_amount = int(input("How many symbols will your password need? "))
            number_amount = int(input("How many numbers will your password need? "))
    
        elif user_decision.lower() == "no":

            lower_amount = 5
            upper_amount = 2
            symbol_amount = 1
            number_amount = 1

   


        lower = lower_character_generator(lower_amount)
        upper = upper_case_generator(upper_amount)
        symbol = symbol_generator(symbol_amount)
        number = number_generator(number_amount)

    #combining the amount of integers entered
        length = lower_amount + upper_amount + symbol_amount + number_amount

    #combining the random characters into one word
        pss_all = lower + upper + symbol + number

    #using the function to scramble the word that was created from the random characters
        password = generate_password(length, pss_all)

 
    
    #printing out the new funtion
        print()
     
        print (f"Here is your new password {password}")

    except UnboundLocalError as trace_err:
        print(trace_err)
        print("please enter either 'yes' or 'no' when asked whether you want to customize your password")

def lower_character_generator(lower_case):
    """ Using the chr funtion and random I can find all of the lower case letters in the alphabet
    then assign the function to return a random one.
    """

    password = ""
    for i in range(lower_case):
        i = chr(randint(97, 122))
        password = str(password) + i

    return password

#next three funtion will be similar to lower_character_generator what changes with these will be the number range from ascII table
def upper_case_generator(upper_case):
    password = ""
    for i in range(upper_case):
        i = chr(randint(65, 90))
        password = str(password) + i

    return password


def symbol_generator(symbol):
    password = ""
    for i in range(symbol):
        i = chr(randint(33, 47))
        password = str(password) + i

    return password

def number_generator(number):
    password = ""
    for i in range(number):
        i = chr(randint(48, 57))
        password = str(password) + i

    return password

def generate_password(length, password):
    """ This funtion will allow me to take the length of the function and the password then shoot it back out
    in a random order instead of just the order the user answer the questions """

    new_password = ""
    new_password = random.sample(password, length)
    random_password = "".join(new_password)

    return random_password



    

if __name__ == "__main__":
    main()