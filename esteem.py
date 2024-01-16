def main():

    print("This program is an implementation of the Rosenberg \n Self-Esteem Scale. This program will show you ten\n statements that you could possibly apply to yourself.\n Please rate how much you agree with each of the\n statements by responding with one of these four letters:")
    print("")
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")

    print("\n1. I feel that I am a person of worth, at leason an\n equal plane with others.")
    answer_one = input("Enter D, d, a, or A: ")
    print("2. I feel that I have a number of good qualities.")
    answer_two = input("Enter D, d, a, or A: ")
    print("3. All in all, I am inclined to feel that I am a failure")
    answer_three = input("Enter D, d, a, or A: ")
    print("4. I am able to do things as well as most other people.")
    answer_four = input("Enter D, d, a, or A: ")
    print("5. I feel I do not have much to be proud of.")
    answer_five = input("Enter D, d, a, or A: ")
    print("6. I take a positive attitude toward myself.")
    answer_six = input("Enter D, d, a, or A: ")
    print("7. On the whole, I am satisfied with myself.")
    answer_seven = input("Enter D, d, a, or A: ")
    print("8.I wish I could have more respect for myself.")
    answer_eight = input("Enter D, d, a, or A: ")
    print("9. I certainly feel useless at times.")
    answer_nine = input("Enter D, d, a, or A: ")
    print("10. At times I think I am no good at all.")
    answer_ten = input("Enter D, d, a, or A: ")

    one = compute_positive(answer_one)
    two = compute_positive(answer_two)
    three = compute_negative(answer_three)
    four = compute_positive(answer_four)
    five = compute_negative(answer_five)
    

    six = compute_positive(answer_six)
    seven = compute_positive(answer_seven)
    eight = compute_negative(answer_eight)
    nine = compute_negative(answer_nine)
    ten = compute_negative(answer_ten)

    total = one + two + three + four + five + six + seven + eight + nine + ten
    
    print(f"Your score is {total}")
    print("A score below 15 may indicate problematic low self-esteem.")
    
    

def compute_positive(answer):
    
    new_answer = 0

    if answer == "D":
        new_answer = new_answer + 0
    elif answer == "d":
        new_answer = new_answer + 1
    elif answer == "a":
        new_answer = new_answer + 2
    elif answer == "A":
        new_answer = new_answer + 3

    return new_answer



def compute_negative(answer):

    new_answer = 0

    if answer == "D":
        new_answer = new_answer + 3
    elif answer == "d":
        new_answer = new_answer + 2
    elif answer == "a":
        new_answer = new_answer + 1
    elif answer == "A":
        new_answer = new_answer + 0

    return new_answer



main()