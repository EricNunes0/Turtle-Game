from time import sleep
from add_points import add_points
from clear_turtle import clear_turtle
from create_turtle import create_turtle
from delete_turtle import delete_turtle
from settings import screen_background_color, screen_width, screen_height, turtle_left, turtle_speed, walk
from random import randint
from write_points import write_points
from write_username import write_username

class move_turtle:
    def __init__(self, screen, turtle, username):
        self.screen = screen
        self.turtle_left = turtle_left
        self.turtle = turtle
        self.check = False
        self.color_index = 0
        
        self.turtle.left(90)
        self.turtle.tiltangle(0)

        self.fruit_x = 0
        self.fruit_y = 0
        self.fruit_width = walk / 2
        self.fruit_turtle = create_turtle()
        self.move_fruit()

        self.points = 0
        self.points_turtle = create_turtle()
        write_points(self.points_turtle, self.points)

        self.username = username
        self.username_turtle = create_turtle()
        write_username(self.username_turtle, self.username)
    
    def move(self, name):
        colors = ["#20a020"]
        if self.check == True:
            self.turtle.speed(turtle_speed)
            self.turtle.color(colors[self.color_index])
            x = int(self.turtle.xcor())
            y = int(self.turtle.ycor())
            halfWidth = int(screen_width / 2)
            halfHeight = int(screen_height / 2)
            if self.fruit_colision(x=x, y=y) == True:
                self.stop()
                self.move_fruit()
                self.points += 100
                add_points(self.points_turtle, name, self.points)
                if self.points >= 2000:
                    self.stop()
                    return False
            self.start()

            if x > halfWidth - walk:
                self.teleport((halfWidth * -1) + walk, y)
            elif x < (halfWidth * -1) + walk:
                self.teleport(halfWidth - walk, y)
            elif y > halfHeight - walk:
                self.teleport(x, (halfHeight * -1) + walk)
            elif y < (halfHeight * -1) + walk:
                self.teleport(x, halfHeight - walk)
            
            self.turtle.up()
            self.turtle.forward(walk / 2)
            self.color_index += 1
            if self.color_index >= len(colors):
                self.color_index = 0
            return True
    
    def start(self):
        self.check = True    
    def stop(self):
        self.check = False
    
    def turn(self, value):
        if self.check == True:
            if self.turtle_left != value:
                self.stop()
                self.turtle.speed(100)
                self.turtle.left(-self.turtle_left)
                self.turtle.left(value)
                self.turtle.tiltangle(0)
                self.turtle_left = value
                self.start()
    
    def top(self):
        newLeft = 0
        self.turn(newLeft)
         
    def left(self):
        newLeft = 90
        self.turn(newLeft)
    
    def right(self):
        newLeft = -90
        self.turn(newLeft)
    
    def bottom(self):
        newLeft = 180
        self.turn(newLeft)
    
    def teleport(self, x, y):
        self.turtle.up()
        self.turtle.speed(0)
        self.turtle.goto(x = x, y = y)
        self.turtle.down()
    
    def get_fruit_position(self):
        return {
            "x": int(randint(2, (screen_width / walk) - 2) * walk) - (screen_width / 2) - (walk / 2),
            "y": int(randint(2, (screen_height / walk) - 2) * walk) - (screen_height / 2) - (walk / 2)
        }
    
    def fruit_colision(self, x, y):
        if x >= self.fruit_x and x < self.fruit_x + self.fruit_width:
            if y >= self.fruit_y and y < self.fruit_y + self.fruit_width:
                return True
        return False
    
    def move_fruit(self):
        clear_turtle(turtle=self.fruit_turtle)
        fruit_pos = self.get_fruit_position()
        x = fruit_pos["x"]
        y = fruit_pos["y"]
        turtle = self.fruit_turtle
        turtle.speed(100)
        turtle.up()
        turtle.setx(x)
        turtle.sety(y)
        turtle.down()
        turtle.dot(self.fruit_width, "#d02020")
        delete_turtle(turtle=turtle)
        self.fruit_x = x
        self.fruit_y = y