import turtle
import os

wn = turtle.Screen()
wn.title("Pong")    # Giving the title for the game window
wn.bgcolor("black")     # Setting the background colour to black with the theme of early 90's retro games in mind
wn.setup(width=800, height=600)     # Setting the initial size of the game window
wn.tracer(0)    # Here we turn off the tracer animation by passing '0' as the parameter to the tracer() function

# The next two lines are the two variables which are created to store the scores of the two players
score_a = 0
score_b = 0


''' 
The next block of code creates the paddle on the left side of the screen which is controlled by the first player.
The paddle was initially created as a square after which a shapesize() function was used to make it into a 
traditional rectangle used in pong games. We also use the penup() function, basically makes sure that the moving
object that you've created does not draw anything on the window.
'''
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


''' 
The next block of code creates the paddle on the right side of the screen which is controlled by the second player.
The paddle was initially created as a square after which a shapesize() function was used to make it into a 
traditional rectangle used in pong games. We also use the penup() function, basically makes sure that the moving
object that you've created does not draw anything on the window.
'''
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


'''
The next block of code creates the ball on the dead centre of the game window. As the game represents the retro age,
the ball itself is not a circle but rather a single pixel square. The dx and dy functions used together initially move 
the ball towards the top right of the game window and towards the second player to start the round.
'''
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1


'''
The next block of code creates a scoreline to dynamically keep track of the scores of both the players.
'''
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


'''
The following functions below are created as part of control of the paddeles to the two players
'''
def paddle_a_up(): # function for moving the left paddle above it's current position
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down(): # function for moving the left paddle below it's current position
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up(): # function for moving the right paddle above it's current posistion
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down(): # function for moving the right paddle below it's current position
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# The next four lines of code bind the functions defined above to a keyboard key
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

'''
This is the main loop of the code where the game window is updated and clear instructions are written about the
collisions and the point system.
'''
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
