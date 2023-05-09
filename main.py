import turtle
import random
import time

score = 0
timelimit = 30
startTime = time.time()

# screen
screen = turtle.Screen()
screen.bgcolor("DarkTurquoise")
screen.tracer(0)
screen.register_shape("fox.gif")
screen.register_shape("coin.gif")

# score
scoreTurtle = turtle.Turtle()
scoreTurtle.hideturtle()
scoreTurtle.penup()
scoreTurtle.color("DeepPink")
scoreTurtle.goto(-130, 180)
scoreTurtle.write("Score: {}".format(score), align="center", font=("Courier", 20, "bold"))

# timer
timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.color("DeepPink")
timer.goto(130, 180)
timer.write("Timer: {}".format(timelimit), align="center", font=("Courier", 20, "bold"))

# game over
gameover = turtle.Turtle()
gameover.hideturtle()
gameover.penup()

# player fox
fox = turtle.Turtle()
fox.shape("fox.gif")
fox.penup()
fox.speed(0)
fox.setheading(90)


def moveRight():
    (x, y) = fox.pos()
    if x < 200:
        fox.setx(x + 5)


def moveLeft():
    (x, y) = fox.pos()
    if x > -200:
        fox.setx(x - 5)


def moveUp():
    if fox.ycor() < 200:
        fox.forward(5)


def moveDown():
    if fox.ycor() > -200:
        fox.backward(5)


# object coin
coin = turtle.Turtle()
coin.shape("coin.gif")
# coin.color("yellow")
coin.penup()
x = random.randint(-180, 180)
y = random.randint(-180, 180)
coin.goto(x, y)

# keyboard bindings
screen.listen()
screen.onkey(fun=moveRight, key="Right")
screen.onkey(fun=moveLeft, key="Left")
screen.onkey(fun=moveUp, key="Up")
screen.onkey(fun=moveDown, key="Down")

# main game loop
while True:
    screen.update()
    # fox coin collision
    if fox.distance(coin) < 30:
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)
        coin.goto(x, y)
        score = score + 10
        scoreTurtle.clear()
        scoreTurtle.write("Score: {}".format(score), align="center", font=("Courier", 20, "bold"))

    # countdown
    timeElapsed = int(time.time() - startTime)
    timer.clear()
    timer.write("Timer: {}".format(timelimit - timeElapsed), align="center", font=("Courier", 20, "bold"))

    # end game when time finishes
    if timeElapsed >= timelimit:
        break;


