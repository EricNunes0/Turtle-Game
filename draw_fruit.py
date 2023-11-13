from resource_path import resource_path

def draw_fruit(screen, turtle, image):
    screen.addshape(resource_path(image))
    turtle.shape(resource_path(image))