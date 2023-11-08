from clear_turtle import clear_turtle
from create_turtle import create_turtle
from delete_turtle import delete_turtle
from settings import screen_width, screen_height
from write_points import write_points
from write_username import write_username

def add_points(turtle, name, value):
    clear_turtle(turtle)
    delete_turtle(turtle)
    turtle.speed(100)
    x = int(screen_width / 2 * -1) + 10
    y = int(screen_height / 2) - 30
    write_points(turtle, value)