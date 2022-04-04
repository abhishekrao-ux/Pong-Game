from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=500)
screen.title("PonG")
screen.tracer(0)

r_Paddle = Paddle((220, 0))
l_Paddle = Paddle((-220, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_Paddle.go_up, "Up")
screen.onkey(r_Paddle.go_down, "Down")
screen.onkey(l_Paddle.go_up, "w")
screen.onkey(l_Paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 220 or ball.ycor() < -220:
        ball.bounce_y()

    if ball.distance(r_Paddle) < 50 and ball.xcor() > 200 or ball.distance(l_Paddle) < 50 and ball.xcor() < -200:
        ball.bounce_x()

    if ball.xcor() > 230:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -230:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
