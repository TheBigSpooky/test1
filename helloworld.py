
import turtle
import random
wn = turtle.Screen()

#  set window colors
wn.bgcolor("lightgreen")

#  get a turtle
tess = turtle.Turtle()
tess.color("blue")              # make tess blue
tess.pensize(3)                 # set the width of her pen
tess.speed(0)

#  do stuff
for i in range(0,1000):
    tess.forward(4)
    tess.left(random.randint(1,10))

wn.exitonclick()                # wait for a user click on the canvas

