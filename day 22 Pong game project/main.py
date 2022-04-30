from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width = 800,height = 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Arun pong game")



player1_paddle = Paddle()
player2_paddle = Paddle()
player1_paddle.set_player1_position()
player2_paddle.set_player2_position()


ball = Ball()
screen.listen()
screen.onkey(player2_paddle.up,"Up")
screen.onkey(player2_paddle.down,"Down")
screen.onkey(player1_paddle.up,"w")
screen.onkey(player1_paddle.down,"s")

score = ScoreBoard()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player2_paddle) < 70 and ball.xcor() > 350 or ball.distance(player1_paddle) < 70 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        score.increase_player1_score()
        

    if ball.xcor() < -380:
        ball.reset_ball()
        score.increase_player2_score()
    
    if score.l_score >= 5:
        score.player1_wins()
        is_game_on = False
    elif score.r_score >= 5:
        score.player2_wins()
        is_game_on = False
    else:
        continue

screen.exitonclick()
