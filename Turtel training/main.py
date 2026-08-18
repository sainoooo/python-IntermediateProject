import turtle
from turtle import Turtle, Screen
import random
import data

timmy = Turtle()
timmy.color("#000080")

#draw a squer
'''for _ in range(4):
    timmy.forward(100)
    timmy.right(90)'''

#draw dashedline 1
'''for _ in range(20):
    timmy.forward(10)
    timmy.color("white")
    timmy.forward(10)
    timmy.color("black")'''

#draw dashedline 2
'''for _ in range(20):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)'''

#draw shape in shape

'''for i in range(3,11):
    for _ in range(i):
        timmy.color(data.colors[i-3])
        timmy.forward(100)
        timmy.right(360/i)'''

#random art
'''turtle.colormode(255)
timmy.speed("fastest")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb'''

'''
timmy.pensize(15)'''
#color 1
'''for _ in range(200):
    dir = random.choice(data.direction)
    timmy.right(dir)
    timmy.forward(30)
    color = random.choice(data.colors)
    timmy.color(color)'''

#color 2
'''for _ in range(200):
    way = random.choice(data.direction)
    timmy.right(way)
    timmy.forward(30)
    timmy.color(random_color())
'''

#cricle
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

timmy.speed("fastest")
for _ in range(180):
    timmy.circle(100)
    timmy.right(2)
    timmy.color(random_color())



screen = Screen()
screen.exitonclick()