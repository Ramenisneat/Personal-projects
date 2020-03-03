import math
import time
import turtle
#rule1 ={"a":"F", "b":"F+F-F-FF+F+F-F"}#FF+[+F-F-F]-[-F+F+F]}
rules = [{"a":"F", "b": "FF+[+F-F-F]-[-F+F+F]"}]
Sentence = " F"
screen = turtle.Screen()
turt = turtle.Turtle()
turt.penup()
turt.setpos(0, -300)
turt.pendown()
turt.left(90)
len= 150
angle =22.5
states= []

def generate(Sentence):
    global len
    len *= .5
    shift = ""
    for i in Sentence:
        check = False
        for r in rules:
            if i == r.get("a"):
                shift += r.get("b")
                check = True
        if not check: shift += i
    return shift

def update(Sentence):
    global states
    global len
    for i in Sentence:
        if i == "F":
            turt.fd(len)
        elif i == "+":
            turt.right(angle)
        elif i == "-":
            turt.left(angle)
        elif i == "[":
            states.append((turt.heading(),turt.pos()))
        elif i == "]":
            turt.penup()
            turt.setheading(states[-1][0])
            turt.setposition(states[-1][1][0], states[-1][1][1])
            turt.pendown()
            states.pop()

turt.speed("fastest")
while True:
    #print(Sentence)
    update(Sentence)
    Sentence = generate(Sentence)
    turt.penup()
    turt.setpos(0, -300)
    turt.setheading(90)
    turt.pendown()

