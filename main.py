from tkinter import *
from turtle import *
from time import sleep
from random import random
from create_turtle import create_turtle
from delete_turtle import delete_turtle
from edit_turtle import edit_turtle
from move_turtle import move_turtle
from play_final import play_final
from resource_path import resource_path
from screen_background_random import screen_background_random
from screen_background_set import screen_background_set
from screen_icon_set import screen_icon_set
from settings import screen_width, screen_height, screen_background_color, screen_background_image, screen_title, button_width, button_height, turtle_speed, turtle_width
from shape_turtle import shape_turtle

# Configurações da tela
screen = Screen()
screen.setup(width = screen_width, height = screen_height)
screen.title(screen_title)
screen.bgcolor(screen_background_color)
screen.cv._rootwindow.resizable(False, False)
screen_background_set(screen, "images/title.png")
screen_icon_set(screen=screen, icon_path="images/icon.png")
canvas = screen.getcanvas()

button_width = button_width
button_height = button_height

username = screen.textinput("Bem-vindo(a)!", f"Controles:\nCima: ⬆ ou W\nEsquerda: ⬅ ou A\nDireita: ➡ ou D\nBaixo: ⬇ ou S\n\nObjetivo: obter 2000 pontos\n\nMas antes de começar, me conte:\nQual é o seu nome?")
print(username)

if username is None or len(username) <= 0:
    screen.clear()
    screen.bye()
else:
    username = username[:30]
    screen_background_random(screen)

    global turtle
    turtle = create_turtle()
    shape_turtle(screen = screen, turtle=turtle, name = "player1", colors = ["#080", "#040"])
    edit_turtle(turtle).speed(turtle_speed)
    edit_turtle(turtle).width(turtle_width)

    moviment = move_turtle(screen, turtle, username=username)
    moviment.start()
    screen.listen()
    screen.onkey(moviment.top, "Up")
    screen.onkey(moviment.left, "Left")
    screen.onkey(moviment.right, "Right")
    screen.onkey(moviment.bottom, "Down")
    screen.onkey(moviment.top, "w")
    screen.onkey(moviment.left, "a")
    screen.onkey(moviment.right, "d")
    screen.onkey(moviment.bottom, "s")
    running = True
    while running == True:
        running = moviment.move(username)
    play_final(screen, turtle)
    #done()