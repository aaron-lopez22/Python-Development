import random

def main():

    numbers = [16.2, 75.1, 52.3]
    #list_of_words = ['join', 'love', 'smile', 'love', 'cloud', 'head']
    words = ['happy', 'hand', "joy"]

    print(f"numbers {numbers}")

    append_random_numbers(numbers)

    print(f"numbers {numbers}")

    append_random_numbers(numbers, 3)

    print(f"numbers {numbers}")

    append_random_words(words, 3)

    print(f"words {words}")

def append_random_numbers(numbers_list, quantity=1):

    for i in range(0, quantity):
        new_number = random.uniform(10, 100)

        rounded = round(new_number, 1)

        numbers_list.append(rounded)

def append_random_words(words_list, quantity=1):

    random_words = ["dog", "cat", "lion", "tiger", "seal", "dragon", "monkey"]

    for i in range(quantity):
        new_words = random.choice(random_words)

        words_list.append(new_words)

if __name__ == "__main__":
    main()
