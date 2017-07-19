import turtle
def loop(tr):
    x=0
    while (x<3):
        tr.forward(100)
        tr.left(120)
        x+=1
def flower():
    window= turtle.Screen()
    window.bgcolor("blue")
    
    triangle=turtle.Turtle()
    triangle.shape("arrow")
    triangle.color("yellow")
    triangle.speed(25)
    triangle.hideturtle()
    triangle.penup()
    triangle.goto(0,300)
    triangle.pendown()
    
    y=0
    while (y<=360):
        loop(triangle)
        triangle.right(20)
        y+=20
    triangle.goto(0,300)
    triangle.goto(0,0)
    triangle.circle(10)
    window.exitonclick()


    
flower()
