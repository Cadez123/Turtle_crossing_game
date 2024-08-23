from turtle import Turtle


# Player class
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(-30,-280)

    # move player up
    def move_up(self):
        self.forward(15)

    # move player down
    def move_down(self):
        self.forward(-15)