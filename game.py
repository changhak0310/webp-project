import turtle
p1 = turtle.Turtle()
p2 = turtle.Turtle()
ball = turtle.Turtle()
screen1 = p1.getscreen()
screen2 = p2.getscreen()
movespeed = 30
def init_setting():
    turtle.setup(width=1000,height=700)
    p1.speed(0)
    p2.speed(0)
    ball.ht()
    p1.ht()
    p2.ht()
    p1.lt(90)
    p2.lt(90)
    p1.shape('square')
    p1.shapesize(stretch_wid=0.5, stretch_len=6, outline=None)
    p2.shape('square')
    p2.shapesize(stretch_wid=0.5, stretch_len=6, outline=None)
    ball.shape('circle')
    ball.shapesize(stretch_wid=2, stretch_len=2, outline=None)
    ball.color('blue')
    p1.penup()
    p2.penup()
    p1.goto(-450,0)
    p2.goto(450,0)
    ball.st()
    p1.st()
    p2.st()

def player_moveUp_1():
    p1.fd(movespeed)
    if(p1.ycor()>=270.0):
        p1.setpos(-450,270)

def player_moveDown_1(): 
    p1.back(movespeed)
    if(p1.ycor()<=-270.0):
        p1.setpos(-450,-270)

def player_moveUp_2():
    p2.fd(movespeed)
    if(p2.ycor()>=270.0):
        p2.setpos(450,270)

def player_moveDown_2(): 
    p2.back(movespeed)
    if(p2.ycor()<=-270.0):
        p2.setpos(450,-270)





        

init_setting()
#dsad
screen1.onkeypress(player_moveUp_1,'w')
screen1.onkeypress(player_moveDown_1,'s')
screen2.onkeypress(player_moveUp_2,'Up')
screen2.onkeypress(player_moveDown_2,'Down')

screen1.listen()
screen2.listen()
screen1.mainloop()
screen2.mainloop()







