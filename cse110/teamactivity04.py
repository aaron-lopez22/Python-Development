print("Welcome to the velocity calculator. PLease enter the following:")
print()

#  m = mass
m = float(input("Mass (in kg): "))

# g = gravity
g = float(input("Gravity (in m/s^2, 9.8 Earth, 24 for Jupiter): "))

#  t = time in seconds
t = float(input("Time (in seconds): "))

#  p = density fluid
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))

# A = cross sectional
A = float(input("Cross sectional area (in m^2): "))

# C = drag constant
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# c = 1/2 p A C or in othe words 1/2 density fluid * cross sectional * drag constant

c = (1/2) * p * A * C

import math

velocity = math.sqrt(m * g / c ) * (1 - math.exp((- math.sqrt(m * g *c) / m) * t)) 

print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {velocity:.3f} m/s")
