# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from tkinter import Y
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_rectangle(canvas, scene_width, scene_height / 1, 1, 280, fill = "blue4")
    draw_rectangle(canvas, scene_width, scene_height / 700, 0, 280, fill= "aliceBlue")
    draw_oval(canvas, 300, 200, 60, 30, fill = "royalBlue3")
    draw_oval(canvas, 340, 200, 410, 275, fill = "white")
    draw_oval(canvas, 345, 270, 405, 330, fill = "white")
    draw_oval(canvas, 353, 320, 393, 365, fill = "white")
    draw_oval(canvas, 365, 335, 381, 345, fill = "black")
    draw_oval(canvas, 365, 350, 367, 355, fill = "black")
    draw_oval(canvas, 379, 350, 381, 355, fill = "black")
    draw_oval(canvas, 70, 400, 150, 470, fill = "gold1")
    draw_oval(canvas, 150, 370, 225, 438, outline = "bisque1", fill = "bisque1")
    draw_oval(canvas, 120, 380, 250, 430, outline = "bisque1", fill = "bisque1")
    draw_pine_tree(canvas, 625, 180, 280)
    draw_pine_tree(canvas, 550, 150, 250)
    draw_pine_tree(canvas, 700, 150, 250)
    draw_grid(canvas, scene_width, scene_height, 50)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_pine_tree(canvas, center_x, bottom, height):
    #Draw the trunk of the tree.
    trunk_width = height / 8
    trunk_height = height / 4
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk,
    trunk_top, fill ="tan4")

    #Draw the skirt of the tree.
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2

    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x,
    peak_y, skirt_right, skirt_bottom, fill = "white")


def draw_grid(canvas, width, height, interval):
    #Draw vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")
    
    #Draw horizontal lines
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")


# Call the main function so that
# this program will start executing.
main()