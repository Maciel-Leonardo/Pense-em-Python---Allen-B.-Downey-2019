import turtle
import math

# 1
def square(t: turtle.Turtle, length: float):
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    turtle.mainloop()

def polygon(t: turtle.Turtle, length: float, n: int):
    Si=180*(n-2)
    Ae=180-(Si/n)
    for i in range(n):
        t.fd(length)
        t.lt(Ae)
    turtle.mainloop()

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = int(circumference / n)
    polygon(t, n, length)
    

def arc(t, r, angle):
    Si = angle * 2 * math.pi * r/360
    n = 20
    length = int(Si/n) 
    Ae=angle/n
    for i in range(n):
            t.fd(length)
            t.lt(Ae)
    turtle.mainloop()

def flower(t, r, angle):
    Si = 2 * math.pi * r
    n = 20
    length = int(Si/n) 
    Ae=angle/n
    for i in range(n):
            t.fd(length)
            t.lt(190)
            t.fd(length)
    turtle.mainloop()
   

bob = turtle.Turtle()
flower(bob,100,360)