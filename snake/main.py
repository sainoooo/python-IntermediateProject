from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up ,"w")
screen.onkey(snake.down ,"s")
screen.onkey(snake.right ,"d")
screen.onkey(snake.left ,"a")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.new_food()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        screen.update();
        game_is_on = False
        score.game_over()
        screen.update()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            score.game_over()
            screen.update()

screen.exitonclick()