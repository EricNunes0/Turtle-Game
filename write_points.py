from delete_turtle import delete_turtle
from teleport_turtle import teleport_turtle
from settings import applesRequired, screen_width, screen_height

def write_points(turtle, value):
    turtle.speed(100)
    delete_turtle(turtle)
    x = int(screen_width / 2 * -1) + 30
    y = int(screen_height / 2) - 30
    teleport_turtle(turtle, x, y - 20)
    turtle.color("#fff")
    turtle.write(f"{value}/{applesRequired}", font=("Arial", 12, "bold"))