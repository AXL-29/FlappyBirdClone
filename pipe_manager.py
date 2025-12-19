import random
from turtle import Turtle

PIPE_SPEED = 3
SCREEN_HEIGHT = 600
PIPE_WIDTH = 60  # 🔹 made wider
PIPE_GAP = 150   # vertical space for the bird

class Pipe(Turtle):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=height/20, stretch_len=width/20)  # Turtle units
        self.goto(x, y)

    def move(self):
        self.setx(self.xcor() - PIPE_SPEED)


class PipeManager:
    def __init__(self):
        self.pipes = []

    def create_pipes(self):
        # Choose center of gap
        gap_center = random.randint(-SCREEN_HEIGHT//2 + PIPE_GAP, SCREEN_HEIGHT//2 - PIPE_GAP)

        # Bottom pipe: from bottom of screen to bottom of gap
        bottom_height = gap_center - PIPE_GAP/2 + SCREEN_HEIGHT/2
        bottom_y = -SCREEN_HEIGHT/2 + bottom_height/2
        bottom_pipe = Pipe(300, bottom_y, PIPE_WIDTH, bottom_height)

        # Top pipe: from top of screen to top of gap
        top_height = SCREEN_HEIGHT/2 - (gap_center + PIPE_GAP/2)
        top_y = SCREEN_HEIGHT/2 - top_height/2
        top_pipe = Pipe(300, top_y, PIPE_WIDTH, top_height)

        self.pipes.extend([bottom_pipe, top_pipe])

    def move_pipes(self):
        for pipe in self.pipes:
            pipe.move()

    def remove_offscreen(self):
        for pipe in self.pipes:
            if pipe.xcor() < -350:
                pipe.hideturtle()
                self.pipes.remove(pipe)
