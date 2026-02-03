import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# import random


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("red")
screen.title("My Snake Game")
screen.tracer(10)

starting_positions=[(0,0),(-20,0),(-40,0)]
segments= []

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        Scoreboard.increase_score(scoreboard)
        food.refresh()

#   Detect collision with walls

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game_is_on = False
        Scoreboard.game_over(scoreboard)

#         if head collides with any segment in the tail :


    for segment in snake.segments[1:]:
        if  snake.head.distance(segment) < 15:
            game_is_on = False
            Scoreboard.game_over(scoreboard)



screen.exitonclick()
















