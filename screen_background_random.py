from screen_background_set import screen_background_set
import random

def screen_background_random(screen):
    backgrounds = [
        'images/background(0).png',
        'images/background(1).png',
        'images/background(2).png',
        'images/background(3).png',
        'images/background(4).png'
    ]
    image = random.choice(backgrounds)
    image = str(image)
    screen_background_set(screen, image)