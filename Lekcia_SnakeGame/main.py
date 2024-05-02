from turtle import Turtle, Screen
import time
import random

screen = Screen()

#nastavenie pozadia obrazovky
screen.bgcolor("green")

#text alebo teda TITLE obrazovky
screen.title("SNAKE GAME by MP")

#nastavenie width a height okna
screen.setup(width=600, height=600)

#vypnutie automatickeho refreshu stranky
screen.tracer(False)

#####hlava hada
#tvar hlavy hada
head = Turtle("square")
#farba hlavy hada
head.color("black")
#rychlost hlavy hada
head.speed(0)
#nekreslit ciaru pera pri pohybe hada
head.penup()
#pociatocna pozicia hlavy hada
head.goto(0, 0)
#....
head.direction = "stop"

####potrava
# bude v tvare kruhu
apple = Turtle("circle")
# kruh bude cervenej farby
apple.color("red")
# pri presune nebude robit ciaru za svojim pohybom, t.j. PRERO HORE // penup
apple.penup()
#pociatocny bod
apple.goto(100, 100)

#casti tela, zatial prazny zoznam
body_parts = []


#vytvorenie funkcie na pohyb
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


#vytvorenie funkcie na konkrety pohyb t.j. na zmenu
def move_up():
    head.direction = "up"

def move_down():
    head.direction = "down"

def move_left():
    head.direction = "left"

def move_right():
    head.direction = "right"

# kliknutie na klavesy
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

#hlavny cyklus pohybu
while True:
    
    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)

        #pridanie casti tela
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)

    move()
    time.sleep(0.1)
    screen.update()

    #pokracujem na videu 38

screen.exitonclick()