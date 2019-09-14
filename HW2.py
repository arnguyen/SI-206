# import the turtle functions for use in this program
# don't need to use the module name
from turtle import *


def draw_rectangle(turtle, xpos, ypos, length, width, color):
    """
    Write a function to draw a rectangle on the screen
    with the specified parameters.

    :param turtle: An instance of the Turtle class
    :param xpos: The X-axis coordinate for a corner of the rectangle
    :param ypos: The Y-axis coordinate for a corner of the rectangle
    :param length: The length of the rectangle
    :param width: The width of the rectangle
    :param color: The line color and fill color to use for the rectangle
    """

    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.end_fill()


def draw_background(turtle, coords, colors, length, width):
    """
    Write a function to draw four rectangles by calling draw_rectangle().
    This function should call draw_rectangle() in a loop.

    :param turtle: An instance of the Turtle class
    :param coords: A list of (X,Y) coordinates to cycle through
    :param colors: A list of colors to cycle through
    :param length: The length of the rectangles
    :param width: The width of the rectangles
    """

    i = 0

    while i < 4:
        draw_rectangle(turtle, coords[i][0], coords[i][1], length, width, colors[i])
        i += 1
        draw_rectangle(turtle, coords[i][0], coords[i][1], width, length, colors[i])
        i += 1


def draw_spiral(turtle, xpos, ypos, color, width):
    """
    Write a function to draw a spiral on top of your 4 rectangles.
    The function should contain the following parameters at a minimum,
    but feel free to add additional ones like "size" or "direction",
    if you'll be calling this function more than once.

    :param turtle: An instance of the Turtle class
    :param xpos: The X-axis coordinate where the spiral should begin.
    :param ypos: The Y-axis coordinate where the spiral should begin.
    :param color: The color of the line.
    :param width: The width of the line.
    """
    length = 1
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(width)
    for i in range(100):
        turtle.forward(length)
        turtle.left(95)
        length += 2

def draw_pentagram(turtle, xpos, ypos, length, color):
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)


def draw_art(turtle):
    """
    Write a function to create your abstract art by calling draw_background and
    draw_spiral (at least once). Feel free to modify the arguments of this
    function as you like. But you should pass in the turtle object at the very
    least.

    Extra credit for using additional functions to draw shapes other than
    a square/rectangle, triangle, or spiral. And for signing your art
    with your initials in block letters.
    """
    coordinates = [(5, 5), (5, 5), (5, 5), (5, 5)]
    colors = ["Dark Turquoise", "Grey", "Violet", "Dark Orange"]

    draw_background(turtle, coordinates, colors, 250, 250)
    draw_spiral(turtle, 5, -30, "Red", 3)
    turtle.forward(50)
    turtle.setheading(0)
    draw_pentagram(turtle, -245, 50, 500, "Black")
    turtle.penup()
    turtle.goto(5, -70)
    turtle.pendown()
    turtle.circle(50)


def main():
    """
    Write a main function that will be called when you run this program
    from the terminal.

    Make sure to create a Screen object, a Turtle object,
    and call draw_background and draw_spiral (at least once).
    You'll also want to create your lists of coordinates and colors here.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting untill you close the drawing window.
    """
    space = Screen()

    bob = Turtle()
    bob.speed(8)

    draw_art(bob)

    space.exitonclick()


# Only run the main method if this file is executed (not imported)
if __name__ == '__main__':
    main()
