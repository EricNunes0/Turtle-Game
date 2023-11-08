from tkinter import Image
from resource_path import resource_path

def screen_icon_set(screen, icon_path):
    icon = Image("photo", file = resource_path(icon_path))
    screen._root.iconphoto(False, icon)