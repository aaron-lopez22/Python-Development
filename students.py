import csv

NUMBER_INDEX = 0
NAME_INDEX = 1

def main():

    number = input("Enter the I-Number: ")

    student_dict = read_dict("students.csv", NUMBER_INDEX )

    name = student_dict[number]
    
    print(name[NAME_INDEX])


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    student_dict = {}

    

    with open(filename, "rt") as text_file:

        read_file = csv.reader(text_file)

        next(read_file)

        for line in read_file:
            key = line[NUMBER_INDEX]
            student_dict[key] = line

    return student_dict





# Call main to start this program.
if __name__ == "__main__":
    main()
