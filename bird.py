from turtle import Turtle

GRAVITY = -0.5
FLAP_STRENGTH = 8

class Bird(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(-100, 0)
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def move(self):
        self.velocity += GRAVITY
        self.sety(self.ycor() + self.velocity)
