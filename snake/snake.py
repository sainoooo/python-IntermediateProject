import turtle
POSITION = [(0, 0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITION:
            self.add(position)

    def add(self,position):
        t = turtle.Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add(self.segments[-1].position())


    def move(self):
        # از دم به سر جابجا کن
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            position = self.segments[i].goto(x, y)
        # سر را جلو ببر
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.segments[0].setheading(0)
