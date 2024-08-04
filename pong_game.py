import turtle
import time

# Background screen set up
wn = turtle.Screen()#creating screen
wn.bgcolor("light blue")#set the background color
wn.title("PONG GAME")#set title of the window
wn.setup(width=800, height=600)#set dimensions of window
wn.tracer(0)#prevents the window from updating automatically

#function to move padel_a up
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

#press Up to move padel_a up
wn.listen()#expecting an input
wn.onkeypress(paddle_a_up,"Up")#to make paddle move down when 'up' pressed
    
#function to move padel_a down
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

#press Down to move padel_a down
wn.listen()#expecting an input
wn.onkeypress(paddle_a_down,"Down")#to make paddle move down when 'down' pressed



#function to move padel_b up
def paddle_b_up():
    y=paddle_b.ycor()
    y+=8
    paddle_b.sety(y)
#function to move padel_b down
def paddle_b_down():
    y=paddle_b.ycor()
    y-=8
    paddle_b.sety(y)




# paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)#setting speed
paddle_a.shape("square")#change shape
paddle_a.shapesize(stretch_wid=5, stretch_len=1)#set up the shape's dimensions
paddle_a.color("blue")#change color
paddle_a.penup()#prevents objects from drawing any lines during run
paddle_a.goto(-350, 0)#setting position

# paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)#setting speed
paddle_b.shape("square")#change shape
paddle_b.shapesize(stretch_wid=5, stretch_len=1)#set up the shape's dimensions
paddle_b.color("green")#change color
paddle_b.penup()#prevents objects from drawing any lines during run
paddle_b.goto(350, 0)#setting position

# ball
ball= turtle.Turtle()
ball.speed(0)#setting speed
ball.shape("circle")#changes shape
ball.color("red")#change color of ball
ball.penup()#prevents objects from drawing any lines during run
ball.goto(0, 0)#setting position
ball.dx=2.5
ball.dy=2.5
    


#function to move the ball
def ball_movement():
    y=ball.ycor()
    x=ball.xcor()
    ball.setx(x+ball.dx)
    ball.sety(y+ball.dy)






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
        pen.write(f"YOU: {score_1}  COMPUTER: {score_2}".format(score_1,score_2),align='center',font=('courier',23,'normal'))
    if ball.xcor() < -350:
        ball.goto(0,0)
        ball.dx *= -1
        score_2+=1
        pen.clear()
        pen.write("YOU: {}  COMPUTER: {}".format(score_1,score_2),align='center',font=('courier',23,'normal'))
        
#function to bounce the ball against the paddle:
def ball_and_paddle():
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
def move_ball():
    ball.forward(10)
    


#score
score_1=0
score_2=0
#scoring system function
pen=turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("YOU: 0  COMPUTER: 0",align='center',font=('courier',24,'normal'))

#ai implementation
def calculate_ball_trajectory():
    width=800
    initial_ball_pos=ball.pos()
    initial_ball_angle=ball.heading()
    ball.setheading(ball.heading()%360)
    if ball.heading()<90 or ball.heading>270:
        while ball.xcor()<width//2-75:
            ball_movement()
            move_ball()
            ball_bouncing()
    x,y=ball.pos()
    ball.setpos(initial_ball_pos)
    ball.setheading(initial_ball_angle)
    return x,y





#ai movement
def ai_movement():
    offset=10
    if ball.heading()<90 or ball.heading()>270:
        target_y=calculate_ball_trajectory()[-1]
        if target_y>paddle_b.ycor()+offset:
            paddle_b.sety(paddle_b.ycor()+5)
        elif target_y<paddle_b.ycor()+offset:
            paddle_b.sety(paddle_b.ycor()-5)

# Main game loop
while True:
    calculate_ball_trajectory()
    ai_movement()
    ball_movement()
    ball_bouncing()
    ball_and_paddle()
    wn.update()  
    time.sleep(0.01)