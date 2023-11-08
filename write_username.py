from delete_turtle import delete_turtle
from teleport_turtle import teleport_turtle
from settings import screen_width, screen_height

def write_username(turtle, name):
    turtle.speed(100)
    delete_turtle(turtle)
    x = int(screen_width / 2 * -1) + 10
    y = int(screen_height / 2) - 30
    teleport_turtle(turtle, x, y)
    turtle.color("#040")
    turtle.write(name, font=("Arial", 14, "bold"))