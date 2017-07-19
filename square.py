import turtle
def loop(obj):
    for i in range (1,5):
        obj.forward(100)
        obj.right(90)
#def lp(ct):
    #for i in range (1,4):
        #ct.forward(100)
        #ct.right(120)
def square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(10)
    for i in range (1,361):
        loop(brad)
        brad.right(1)
    #angie= turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("yellow")
    #angie.circle(100)
    #triangle= turtle.Turtle()
    #triangle.speed(1)
    #lp(triangle)

    window.exitonclick()

square()
