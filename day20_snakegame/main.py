import time
from turtle import Screen
from snake import Snake
from snake_food import Food
from score import Score
screen = Screen()
snake = Snake()
food = Food()
score = Score()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snake Game')
screen.tracer(0)



screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.generateFood()
        score.updateScore()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    list = snake.segments[1:]
    for segment in list:
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()