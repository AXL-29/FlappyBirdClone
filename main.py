import time
from turtle import Screen
from bird import Bird
from pipe_manager import PipeManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("skyblue")
screen.title("Flappy Bird - Turtle")
screen.tracer(0)

bird = Bird()
pipes = PipeManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(bird.flap, "space")

# Countdown before starting
scoreboard.countdown(screen)

game_is_on = True
frame_count = 0

def check_collision(bird, pipes):
    bird_x = bird.xcor()
    bird_y = bird.ycor()
    bird_size = 10  # radius of bird

    for pipe in pipes.pipes:
        pipe_x = pipe.xcor()
        pipe_y = pipe.ycor()
        pipe_width = pipe.shapesize()[1] * 10  # stretch_len * 20 / 2
        pipe_height = pipe.shapesize()[0] * 10 # stretch_wid * 20 / 2

        left = pipe_x - pipe_width
        right = pipe_x + pipe_width
        top = pipe_y + pipe_height
        bottom = pipe_y - pipe_height

        if (left <= bird_x <= right) and (bottom <= bird_y <= top):
            return True
    return False

while game_is_on:
    time.sleep(0.02)
    screen.update()

    bird.move()
    pipes.move_pipes()
    pipes.remove_offscreen()

    # Spawn pipes every 100 frames
    frame_count += 1
    if frame_count % 100 == 0:
        pipes.create_pipes()

    # Check collisions
    if check_collision(bird, pipes):
        game_is_on = False
        scoreboard.game_over()

    # Check if bird passed pipes (score)
    scoreboard.check_passed_pipe(bird, pipes)

    # Hit ground or ceiling
    if bird.ycor() > 280 or bird.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
