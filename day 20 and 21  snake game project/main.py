from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My python snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

food = Food()
score = ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.increase_score()
        snake.extend_segment()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
        # score.reset_score()
        # snake.reset_snake()

    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
            # score.reset_score()
            # snake.reset_snake()

screen.exitonclick()