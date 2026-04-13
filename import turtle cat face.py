import turtle


t = turtle.Turtle()
t.speed(5)
t.pensize(3)
turtle.bgcolor("white")

 
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


move_to(0, -100)
t.color("black", "#FFD700") 
t.begin_fill()
t.circle(100)
t.end_fill()

move_to(60, 80)
t.begin_fill()
for i in range(3):
    t.forward(50)
    t.left(120)
t.end_fill()

move_to(-110, 80)
t.begin_fill()
for i in range(3):
    t.forward(50)
    t.left(120)
t.end_fill()

move_to(40, 30)
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

move_to(-40, 30)
t.begin_fill()
t.circle(10)
t.end_fill()

move_to(0, 10)
t.color("pink")
t.begin_fill()
for i in range(3):
    t.forward(20)
    t.right(120)
t.end_fill()

t.color("black")
move_to(20, 0)
t.goto(80, 10)
move_to(20, 0)
t.goto(80, -10)
move_to(-20, 0)
t.goto(-80, 10)
move_to(-20, 0)
t.goto(-80, -10)

t.hideturtle()
turtle.exitonclick()
