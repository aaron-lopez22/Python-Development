
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 225
youngest_name = ""

for person in people:
    clean_list = person.split(" ")
    name = clean_list[0]
    age = int(clean_list[1])

    print(person)
    #print(name)
    #print(age)

    if age < youngest_age:

        youngest_age = age

        youngest_name = name
        



print(f"The youngest age is {youngest_age}")
print(f"The name of the youngest person is {youngest_name}")