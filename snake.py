from turtle import Turtle

S_POINT = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segements = []
        self.create_snake()
        self.head = self.segements[0]

    def create_snake(self):
        for i in S_POINT:
            self.add_segements(i)

    def add_segements(self, position):
        self.snake = Turtle()
        self.snake.shape("square")
        self.snake.color("white")
        self.snake.penup()
        self.snake.setposition(position)
        self.segements.append(self.snake)

    def extend_snake(self):
        self.add_segements(self.segements[-1].position())

    def move(self):
        for seg_num in range(len(self.segements) - 1, 0, -1):
            # get the last segement to take position a head of it
            new_x = self.segements[seg_num - 1].xcor()
            new_y = self.segements[seg_num - 1].ycor()
            self.segements[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            return self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            return self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            return self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            return self.segements[0].setheading(RIGHT)
