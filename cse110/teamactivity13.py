
import math



def compute_area_square():
    square_side = float(input("what is the length of the side? "))
    return square_side * square_side


def compute_area_rectangle():
    length_input = float(input("What is the length of the rectangle? "))
    width_input = float(input("What is the width of the rectangle? "))
    return length_input * width_input


def compute_area_circle():
    radius = float(input("what is the radius of the circle? "))
    return radius * radius * math.pi
    

shape = ""

while shape != "quit":
    shape = input("What shape do you have? ")

    shape = shape.lower()

    if shape == "square":
        area_square = compute_area_square()
        print(area_square)
    elif shape == "rectangle":
        area_rectangle = compute_area_rectangle()
        print(area_rectangle)
    elif shape == "circle":
        area_circle = compute_area_circle()
        print(f"{area_circle: .2f}")
