import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.title("Ping - Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((382, 0))
l_paddle = Paddle((-388, 0))
score = Score()

screen.listen()

"""Key strokes for Right paddle"""
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

"""Key strokes for Left paddle"""
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_move_speed)
    screen.update()
    ball.move()

    """collision with wall"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    """collision with paddle"""
    if (ball.distance(r_paddle) < 40 and ball.xcor() > 350) or (ball.distance(l_paddle) < 40 and ball.xcor() < -360):
        ball.bounce_paddle()

    """ball missed right paddle"""
    if ball.xcor() > 360:
        ball.reset_position()
        score.increase_left_score()

    """ball missed left paddle"""
    if ball.xcor() < -375:
        ball.reset_position()
        score.increase_right_score()

screen.exitonclick()