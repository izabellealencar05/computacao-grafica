import turtle as tr

tr.speed(50)
tr.color(30/255,70/255,60/255)
tr.pensize(5)
tr.penup()
tr.goto(-100,-100)
tr.pendown()
tr.begin_fill()


for i in range(4):
    tr.forward(200)
    tr.left(90)
tr.end_fill()

tr.color(100/255,60/255,100/255)
tr.begin_fill()
tr.penup()
tr.fd(50)
tr.pendown()
tr.fd(50)
tr.left(90)
tr.fd(100)
tr.left(90)
tr.fd(50)
tr.left(90)
tr.fd(100)
tr.left(90)
tr.end_fill()

tr.begin_fill()
tr.penup()
tr.fd(150)
tr.left(90)
tr.fd(202)

tr.right(90)
tr.pendown()
tr.fd(30)
tr.left(135)
tr.fd(180)
tr.left(90)
tr.fd(180)
tr.left(135)
tr.fd(200)



