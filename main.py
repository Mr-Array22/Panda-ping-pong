# Author mostafa gamal

# imported turtle module
import turtle
import datetime

now = datetime.datetime.now()
print("Created by Mostafa gamal at " + str(now))

# inti screen of the game
wind = turtle.Screen()
# window title
wind.title('Panda-Ping-Pong')
# window color
wind.bgcolor("black")
# set the height and width of the screen
wind.setup(width=800, height=600)
# prevent window from automatic refresh
wind.tracer(0)

# madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape('square')
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.color('blue')
madrab1.penup()
madrab1.goto(-350, 0)

# madrab2
madrab2 = turtle.Turtle()  # init object
madrab2.speed(0)  # set speed of animation
madrab2.shape('square')  # set the shape
madrab2.shapesize(stretch_wid=5, stretch_len=1)  # stretch the shape
madrab2.color('red')  # set the color of the object
madrab2.penup()  # prevent draw while moving
madrab2.goto(350, 0)  # position the object in the screen

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player1:0 Player2:0", align="center", font=("courier", 24, "normal"))


# functions
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)


def madrab1_down():
    y = madrab1.ycor()
    y += -20
    madrab1.sety(y)


def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)


def madrab2_down():
    y = madrab2.ycor()
    y += -20
    madrab2.sety(y)


# keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

# update the window
# main game loop
while True:
    wind.update()
    # move ball
    ball.setx(ball.xcor() + ball.dx)  # ball starts at 0 -->>>+2 axis
    ball.sety(ball.ycor() + ball.dy)  # ball starts at 0 -->>>+2 yxis

    # border check
    if ball.ycor() > 290:  # if ball is at top border
        ball.sety(290)  # set y coordinate +290
        ball.dy *= -1  # reverse the direction

    if ball.ycor() < -290:  # if ball is at bottom border
        ball.sety(-290)  # set y coordinate -290
        ball.dy *= -1  # reverse the direction

    if ball.xcor() > 390:  # if ball is at right border
        ball.goto(0, 0)  # return ball to the center
        ball.dx *= -1  # reverse the x
        score1 += 1
        score.clear()
        score.write("Player1:{} Player2:{}".format(score1, score2), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:  # if ball is at left border
        ball.goto(0, 0)  # return ball to the center
        ball.dx *= -1  # reverse the x
        score2 += 1
        score.clear()
        score.write("Player1:{} Player2:{}".format(score1, score2), align="center", font=("courier", 24, "normal"))

    # ball collision
    if (340 < ball.xcor() < 350) and (madrab2.ycor() + 40 > ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (madrab1.ycor() + 40 > ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
