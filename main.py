from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SPEED = 0.2
display = Screen()
tim = Snake()
food = Food()
scoreboard = Scoreboard()


display.bgcolor("black")
display.title("snake game")
display.tracer(0)

display.onkey(tim.up, "Up")
display.onkey(tim.down, "Down")
display.onkey(tim.left, "Left")
display.onkey(tim.right, "Right")

display.listen()
display.setup(width=600, height=600)

game_state = True


while game_state:
    display.update()
    time.sleep(SPEED)
    scoreboard.display_score()
    tim.move()

    # Detect collision with food.
    if tim.head.distance(food) < 15:
        food.refresh()
        tim.extend_snake()
        scoreboard.update_score()

    # Detect wall collision
    if tim.head.xcor() > 280 or tim.head.xcor() < -280 or tim.head.ycor() > 280 or tim.head.ycor() < -280:
        scoreboard.game_over()
        game_state = False

    # Detect tail collision
    for i in tim.segements[1:]:
        # in python you can compare object 👀
        # if i == tim.head:
        #     print(i)
        #     pass

        if tim.head.distance(i) < 10:
            scoreboard.game_over()
            game_state = False


display.exitonclick()
