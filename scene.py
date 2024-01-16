# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():



    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_sun(canvas, scene_width, scene_height)
    draw_cloud(canvas)
    draw_ground(canvas, scene_width, scene_height)
    draw_grass(canvas, 32, 0)
    draw_grass(canvas, 50, 0)
    draw_grass(canvas, 100, 0)
    draw_grass(canvas, 150, 0)
    draw_grass(canvas, 200, 0)
    draw_grass(canvas, 225, 0)

    draw_grid(canvas, scene_width, scene_height, 50)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_grid(canvas, width, height, interval):
    #draw vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")
    #draw horizontal
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}") 


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="midnightblue")

def draw_sun(canvas, scene_width, scene_height):
    #first oval
    draw_oval(canvas, scene_width, scene_height, 350, 50, fill="darkorange1")

def draw_cloud(canvas):
    
    draw_oval(canvas, 250, 450, 50, 350, width= 0, fill="mediumPurple1")

    draw_oval(canvas, 325, 400, 100, 350, width= 0, fill="mediumPurple1")

    draw_oval(canvas, 300, 275, 150, 375, width= 0, fill="mediumPurple1")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 2.5, width=0, fill="sienna3")

def draw_grass(canvas, corner_x, corner_y):

    corner_x_two = corner_x + 13
    corner_y_two = corner_y + 35

    draw_rectangle(canvas, corner_x, corner_y, corner_x_two, corner_y_two, width=1, fill="sandyBrown")

    corner_x = corner_x + 3
    corner_x_two = corner_x + 15
    corner_y_two = corner_y + 60

    draw_rectangle(canvas, corner_x, corner_y, corner_x_two, corner_y_two, width=1, fill="sandyBrown")

    corner_x = corner_x + 15
    corner_x_two = corner_x + 10
    corner_y_two = corner_y + 45

    draw_rectangle(canvas, corner_x, corner_y, corner_x_two, corner_y_two, width=1, fill="sandyBrown")

    
    corner_x_two = corner_x + 10
    corner_y_two = corner_y + 80

    draw_rectangle(canvas, corner_x, corner_y, corner_x_two, corner_y_two, width=1, fill="sandyBrown")

    corner_x = corner_x + 10
    corner_x_two = corner_x + 5
    corner_y_two = corner_y + 50

    draw_rectangle(canvas, corner_x, corner_y, corner_x_two, corner_y_two, width=1, fill="sandyBrown")
    







# Call the main function so that
# this program will start executing.
main()