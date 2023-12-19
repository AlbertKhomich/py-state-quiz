import turtle


class StateLocation(turtle.Turtle):

    def __init__(self, name, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(name)
