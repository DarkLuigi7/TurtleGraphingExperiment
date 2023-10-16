from turtle import*
from os import system
import math
screensize(1000,1000)
setworldcoordinates(-100,-100,100,100)


def drawaxes():
    tracer(0)
    goto(-100, 0)
    fd(200)
    write("x",font=("Verdana", 12, "bold"))
    penup()
    goto(0, -100)
    pendown()
    seth(90)
    fd(200)
    write("y",font=("Verdana", 12, "bold"))
    penup()
    goto(-3,-5)
    write(0,font=("Verdana", 12, "bold"))
    update()
    tracer(1)

def plotter(expr):
    color("blue")
    penup()
    for x in range(-100, 100):
        try:
            y = eval(expr)
            #eval() function converts user input into a working python function
        except ZeroDivisionError or ValueError:
            continue
        except ValueError:
            continue
        if y > 100 or y < -100:
            continue
        goto(x, y)
        pendown()


while True:
    drawaxes()
    expr = input("Enter a function in terms of x:")
    #allow user to input a mathematical function
    plotter(expr)
