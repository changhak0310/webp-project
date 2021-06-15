import turtle

sc = turtle.Screen()
sc.title("Game_Web")
sc.bgcolor("white")
sc.setup(width=1000, height=700)

#왼쪽 플레이어
leftPlayer = turtle.Turtle()
leftPlayer.speed(0)
leftPlayer.shape("square")
leftPlayer.color("black")
leftPlayer.shapesize(stretch_wid=6, stretch_len=1)
leftPlayer.penup()
leftPlayer.goto(-400, 0)

#오른쪽 플레이어
rightPlayer = turtle.Turtle()
rightPlayer.speed(0)
rightPlayer.shape("square")
rightPlayer.color("black")
rightPlayer.shapesize(stretch_wid=6, stretch_len=1)
rightPlayer.penup()
rightPlayer.goto(400, 0)

#공
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 5 #공 방향
ball.dy = -5

#점수 
leftScore = 0
rightScore = 0

score = turtle.Turtle()
score.speed(0)
score.color("Black")
score.penup()
score.ht()
score.goto(0, 260)
score.write("Left_player : "+str(leftScore)+" / Right_player: "+str(rightScore),align="center",font=("Arial", 24, "normal"))

def LmoveUp(): #왼쪽 위 움직임
	leftPlayer.sety(leftPlayer.ycor()+20)
	if leftPlayer.ycor()>=280: #벽
		leftPlayer.setpos(-400,280)

def LmoveDown(): #왼쪽 아래 움직임
	leftPlayer.sety(leftPlayer.ycor()-20)
	if leftPlayer.ycor()<=-280: #벽
		leftPlayer.setpos(-400,-280)

def RmoveUp(): #오른쪽 위 움직임
	rightPlayer.sety(rightPlayer.ycor()+20)
	if rightPlayer.ycor()>=280: #벽
		rightPlayer.setpos(400,280)

def RmoveDown(): #오른쪽 아래 움직임
	rightPlayer.sety(rightPlayer.ycor()-20)
	if rightPlayer.ycor()<=-280: #벽
		rightPlayer.setpos(400,-280)

#'w','s' '↑','↓' 움직임
sc.onkeypress(LmoveUp, "w")
sc.onkeypress(LmoveDown, "s")
sc.onkeypress(RmoveUp, "Up")
sc.onkeypress(RmoveDown, "Down")
sc.listen()

#프레임
while True:
	sc.update()
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)
      #벽 감지
	if ball.ycor() > 280:
		ball.sety(280)
		ball.dy *= -1

	if ball.ycor() < -280:
		ball.sety(-280)
		ball.dy *= -1
      #공 골인시 점수
	if ball.xcor() > 500:
		ball.goto(0, 0)
		ball.dy *= -1
		leftScore += 1
		score.clear()
		score.write("Left_player : "+str(leftScore)+" / Right_player: "+str(rightScore),align="center",font=("Arial", 24, "normal"))

	if ball.xcor() < -500:
		ball.goto(0, 0)
		ball.dy *= -1
		rightScore += 1
		score.clear()
		score.write("Left_player : "+str(leftScore)+" / Right_player: "+str(rightScore),align="center",font=("Arial", 24, "normal"))

      #공 플레이어와 튕김
	if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < rightPlayer.ycor()+62 and ball.ycor() > rightPlayer.ycor()-62):
		ball.setx(360)
		ball.dx*=-1
		
	if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<leftPlayer.ycor()+62 and ball.ycor()>leftPlayer.ycor()-62):
		ball.setx(-360)
		ball.dx*=-1
