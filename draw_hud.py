from create_turtle import create_turtle
from delete_turtle import delete_turtle
from draw_fruit import draw_fruit
from teleport_turtle import teleport_turtle
from settings import applesRequired, screen_width, screen_height

def draw_hud(screen):
    hud_turtle = create_turtle()
    hud_turtle.speed(100)
    x = int(screen_width / 2 * -1) + 15
    y = int(screen_height / 2) - 20
    teleport_turtle(hud_turtle, x, y - 20)
    draw_fruit(screen=screen, turtle=hud_turtle, image="images\\apple_hud.gif")