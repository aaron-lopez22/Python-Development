
import csv


def main():
    try:

        PRODUCT_INDEX = 0
        number_of_items = 0
        sub_total = 0
        sales_tax = 0
        total = 0

                          # Import the datetime class from the datetime
# module so that it can be used in this program.
        from datetime import datetime

        week_day = datetime.now()
        x = week_day.weekday()
# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
        current_date_and_time = datetime.now()
        

        products_dict = read_dict("products.csv", PRODUCT_INDEX)

        print("Inkom Emporium")
        print()

        with open ("request.csv", "rt") as request_file:

            reader = csv.reader(request_file)

            next(reader)

            for row in reader:

                if len(row) != 0:
                    if x == 2:

                        product = row[0]
                        quantity = int(row[1])
                        number_of_items += quantity

                        products = products_dict[product]
                        product_name = products[1]
                        product_price = float(products[2]) *.9
                        sub_total += product_price * quantity
                        sales_tax = sub_total * 0.06
                        total = sales_tax + sub_total

                        

                        print(f"{product_name}: {quantity} @ discount {product_price}")
                    else:
                        product = row[0]
                        quantity = int(row[1])
                        number_of_items += quantity

                        products = products_dict[product]
                        product_name = products[1]
                        product_price = float(products[2])
                        sub_total += product_price * quantity
                        sales_tax = sub_total * 0.06
                        total = sales_tax + sub_total

                        

                        print(f"{product_name}: {quantity} @ {product_price}")
        print()
        print(f"Number of Items: {number_of_items}")
        print(f"Subtotal: {sub_total: .2f}")
        print(f"Sales Tax: {sales_tax: .2f}")
        print(f"Total: {total: .2f}")
        print()
        print("Thank you for shopping at the Inkom Emporium")
  

# Use an f-string to print the current
# day of the week and the current time.
        print(f"{current_date_and_time:%A %I:%M %p}")
        


        

    except FileNotFoundError as error:
        print("Error: missing file")
        print(error)
        

    except KeyError as key_err:
        print("Error: uknown product ID in the request.csv file")
        print(key_err)    
    
    except PermissionError as perm_err:
        print(perm_err)
    
    

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

    dictionary = {}

    with open (filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            if len(row_list) != 0:

                key = row_list[key_column_index]

                dictionary[key] = row_list
    
    return dictionary



if __name__ == "__main__":
    main()