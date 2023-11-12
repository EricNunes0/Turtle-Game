from resource_path import resource_path

def screen_background_set(screen, image):
    screen.bgpic(resource_path(image))
