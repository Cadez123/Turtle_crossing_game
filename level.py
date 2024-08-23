from turtle import Turtle


# level class
class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-300, 200)
        self.hideturtle()
        self.level = 0
        self.level_up()

    # level up function
    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f'LEVEL - {self.level}', align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=('Arial', 25, 'normal'))