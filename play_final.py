from create_popup import create_popup
from play_audio import play_audio
from resource_path import resource_path
from time import sleep

def play_final(screen, turtle):
    screen.clearscreen()
    screen.bgpic(resource_path("images/final.png"))
    turtle.clear()
    play_audio("audios/final.mp3")
    create_popup(screen, "Parabéns por terminar o jogo!\nSua senha é:\nXr6nfG1K3j4P")