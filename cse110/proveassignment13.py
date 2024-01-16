'''
Prove assignment 13
Aaron Lopez
'''
# Gathering user info for temperature and what measurement farenheit or celsius

user_temperature = float(input("What is the temperature? "))
measurement = input("Fahrenheit or Celsius (F/C)? ")

# defining wind mph

wind = 0

#Creating functions to convert to celsius and for wind chill

def celsius_conversion(user_info):
   return user_info * (9/5) + 32

def wind_chill_conversion(user_info, wind):
   return (35.74 + 0.6215 * user_info) - (35.75 * (wind ** .16)) + ((0.4275 * user_info) * (wind ** .16))



# if user is using celsius this will use the function to convert celsius to Farenheit 

if measurement.lower() == 'c':
    user_temperature = celsius_conversion(user_temperature)


# Keeps the loop going to display until 60 wind speed

while wind != 60:
    wind += 5
    wind_chill = wind_chill_conversion(user_temperature, wind)

    print(f"At temperature {user_temperature}F, and wind speed {wind} mph, the windchill is: {wind_chill: .2f}F")