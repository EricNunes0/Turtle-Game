from create_turtle import create_turtle
from delete_turtle import delete_turtle
from resource_path import resource_path
from teleport_turtle import teleport_turtle
import time

def draw_controls(screen):
    controls_turtle = create_turtle()
    teleport_turtle(controls_turtle, 0, 100)
    image = "images\\controls.gif"
    screen.addshape(resource_path(image))
    controls_turtle.shape(resource_path(image))
    time.sleep(3)
    delete_turtle(controls_turtle)