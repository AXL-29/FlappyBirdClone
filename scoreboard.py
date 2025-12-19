from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()
        self.passed_pipes = set()  # track pipes already counted

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "bold"))

    def increase(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    def countdown(self, screen):
        self.goto(0, 0)
        for i in range(3, 0, -1):
            self.clear()
            self.write(i, align="center", font=("Arial", 48, "bold"))
            screen.update()  # force update
            time.sleep(1)
        self.clear()
        self.goto(0, 260)
        self.update_score()

    # 👇 New method to check if bird passed a pipe
    def check_passed_pipe(self, bird, pipes):
        for pipe in pipes.pipes:
            if pipe not in self.passed_pipes and pipe.xcor() < bird.xcor():
                # Only count bottom pipe to avoid double count
                if pipe.ycor() < 0:
                    self.increase()
                self.passed_pipes.add(pipe)
