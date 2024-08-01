#function to move the ball
def ball_movement():
    y=ball.ycor()
    x=ball.xcor()
    ball.setx(x+ball.dx)
    ball.sety(y+ball.dy)

#score
score_1=0
score_2=0
# bouncing the ball against the wall  
def ball_bouncing():
    global score_1,score_2
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:  
        ball.goto(0,0)
        ball.dx *= -1
        score_1+=1
        pen.clear()
        pen.write(f"You: {score_1}  Computer: {score_2}".format(score_1,score_2),align='center',font=('courier',23,'normal'))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2+=1
        pen.clear()
        pen.write("You: {}  Computer: {}".format(score_1,score_2),align='center',font=('courier',23,'normal'))
        
#function to bounce the ball against the paddle:
def ball_and_paddle():
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
    
#function to move padel_a up
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
    
#function to move padel_a down
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
    
    
import turtle
import time

# Background screen set up
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("PONG GAME")
wn.setup(width=800, height=600)
wn.tracer(0)



# paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(5,1)
paddle_a.color("blue")
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(5,1)
paddle_b.color("green")
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx=2
ball.dy=2

#scoring system function
pen=turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("You: 0  Computer: 0",align='center',font=('courier',24,'normal'))
    
#press Up to move padel_a up
wn.listen()
wn.onkeypress(paddle_a_up,"Up")

#press Down to move padel_a down
wn.listen()
wn.onkeypress(paddle_a_down,"Down")

# Main game loop
while True:
    ball_movement()
    ball_bouncing()
    ball_and_paddle()
    wn.update()  
    time.sleep(0.01)  
    
