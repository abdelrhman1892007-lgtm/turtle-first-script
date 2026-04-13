import turtle

# إعدادات الشاشة
t = turtle.Turtle()
t.speed(5)
t.pensize(3)
turtle.bgcolor("white")

# دالة لتحريك القلم بدون رسم
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# 1. رسم الرأس (دائرة)
move_to(0, -100)
t.color("black", "#FFD700") # لون ذهبي للقطة
t.begin_fill()
t.circle(100)
t.end_fill()

# 2. رسم الأذن اليمنى (مثلث)
move_to(60, 80)
t.begin_fill()
for i in range(3):
    t.forward(50)
    t.left(120)
t.end_fill()

# 3. رسم الأذن اليسرى (مثلث)
move_to(-110, 80)
t.begin_fill()
for i in range(3):
    t.forward(50)
    t.left(120)
t.end_fill()

# 4. رسم العينين
# العين اليمنى
move_to(40, 30)
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

# العين اليسرى
move_to(-40, 30)
t.begin_fill()
t.circle(10)
t.end_fill()

# 5. رسم الأنف (مثلث صغير مقلوب)
move_to(0, 10)
t.color("pink")
t.begin_fill()
for i in range(3):
    t.forward(20)
    t.right(120)
t.end_fill()

# 6. رسم الشوارب
t.color("black")
# شوارب يمين
move_to(20, 0)
t.goto(80, 10)
move_to(20, 0)
t.goto(80, -10)
# شوارب شمال
move_to(-20, 0)
t.goto(-80, 10)
move_to(-20, 0)
t.goto(-80, -10)

t.hideturtle()
turtle.exitonclick()