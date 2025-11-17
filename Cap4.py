import turtle
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

def circle():
    

bob = turtle.Turtle()
polygon(bob,100,7)