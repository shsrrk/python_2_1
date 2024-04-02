import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
move = 10
for i in range(36):
    t.penup()
    t.forward(0)
    t.pendown()
    t.forward(25)
    t.penup()
    t.forward(15)
    t.stamp()
    t.home()
    t.right(move)
    move += 10  #30도씩 움직여라 
