import math

items = int(input("Enter the number of items: "))
item_box = int(input("Enter the number of items per box: "))

box = items / item_box

boxes = math.ceil(box)

print(boxes)