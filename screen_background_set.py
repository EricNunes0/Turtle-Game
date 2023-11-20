from resource_path import resource_path

def screen_background_set(screen, image):
    try:
        screen.bgpic(resource_path(image))
    except Exception as e:
        print(e)