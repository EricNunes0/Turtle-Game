class edit_turtle:
    def __init__(self, turtle):
        self.turtle = turtle
    
    def speed(self, speed: int):
        self.turtle.width(speed)
    
    def width(self, width: int):
        self.turtle.width(width)