'''
Aaron Lopez
Milestone 11 and 12
'''
print()

chosen_year = int(input("Enter the year of interest: "))
chosen_country = input("Enter the country of intrest: ")

overall_lowest_life = 9999
overall_lowest_country = ""
overall_lowest_year = -1

overall_max_life = -1
overall_max_country = ""
overall_max_year = -1

ch_lowest_life = 9999
ch_lowest_country = ""
ch_lowest_year = -1

ch_max_life = -1
ch_max_country = ""
ch_max_year = -1

row_count = 0
average_life = 0
sum = 0


new_row_count = 0
new_average_life = 0
new_sum = 0

co_lowest_life = 9999
co_lowest_country = ""
co_lowest_year = -1

co_max_life = -1
co_max_country = ""
co_max_year = -1


with open("life-expectancy.csv") as life_date:
    next(life_date, None)
    for date in life_date:
        clean = date.strip()
        parts = clean.split(",")


        name = parts[0]
        suffix = parts[1]
        year = int(parts[2])
        expectancy = float(parts[3])

        
        if expectancy < overall_lowest_life:

                overall_lowest_life = expectancy
                overall_lowest_country = name
                overall_lowest_year = year

        elif expectancy > overall_max_life:
            
            overall_max_life = expectancy
            overall_max_country = name
            overall_max_year = year

        if year == chosen_year:
            
            row_count += 1
            sum += expectancy

            average_life = sum / row_count

            if expectancy < ch_lowest_life:


                ch_lowest_life = expectancy
                ch_lowest_country = name
                ch_lowest_year = year

            elif expectancy > ch_max_life:
            
                ch_max_life = expectancy
                ch_max_country = name
                ch_max_year = year

        if name.lower() == chosen_country.lower():
            
            new_row_count += 1
            new_sum += expectancy

            new_average_life = sum / row_count

            if expectancy < co_lowest_life:


                co_lowest_life = expectancy
                co_lowest_country = name
                co_lowest_year = year

            elif expectancy > co_max_life:
            
                co_max_life = expectancy
                co_max_country = name
                co_max_year = year

            

print()        
print(f"The overall max life Expectancy is: {overall_max_life} from {overall_max_country} in {overall_max_year}")        
print(f"The overall min life exectancy is: {overall_lowest_life} from {overall_lowest_country} in {overall_lowest_year} ")
print()
print(f"For the year {chosen_year}:")
print(f"The average life expectancy across all countries was {average_life: .2f}")
print(f"The max life expectancy was in {ch_max_country} with {ch_max_life}")
print(f"The min life expectancy was in {ch_lowest_country} with {ch_lowest_life}")
print()
print(f"For the country {chosen_country}:")
print(f"The average life expectancy across the years in {chosen_country} was {new_average_life: .2f}")
print(f"The highest life expectancy in {co_max_country} was {co_max_life}")
print(f"The lowest life expectancy in {co_lowest_country} was {co_lowest_life}")
print()