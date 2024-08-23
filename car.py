from player import Turtle
import random

# car colors
colors = ["red", "blue", "green", 'magenta', 'brown', 'yellow']


# car class
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.random_position = random.randrange(-250,250,2)
        self.penup()
        self.color(random.choice(colors))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.goto(x=400,y=self.random_position)

    # move cars forward
    def move_forward(self):
        self.forward(-10)