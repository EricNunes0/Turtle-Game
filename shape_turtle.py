from turtle import Shape

def shape_turtle(turtle, screen, name: str, colors: list):
    turtle.shape("turtle")
    polygon = turtle.get_shapepoly()
    turtle_color = Shape("compound")
    turtle_color.addcomponent(polygon, colors[0], colors[1])
    screen.register_shape(name, turtle_color)
    turtle.shape(name)
    return turtle