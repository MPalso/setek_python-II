from turtle import Turtle, Screen
import time
import random

#premenne
score = 0
highest_score = 0

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

#####score
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write("Skore: 0 Najvacsie skore: 0", align="center", font=("Arial", 18))

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
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

# kliknutie na klavesy
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

#hlavny cyklus 
while True:

    screen.update()

    #kontrola kolizie s hranou platna
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"

        #skryt casti tela
        for one_body_part in body_parts:
            one_body_part.goto(1500, 1500)

        #po kolizii vyprazdnime  list s castami tela
        body_parts.clear()

        #vynulovanie score
        score = 0

        score_sign.clear()
        score_sign.write(f"Skore: {score} Najvacsie skore: {highest_score}", align="center", font=("Arial", 18))


    #kolizia hlavy z jablkom / had zje jedlo
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

        # zvysenie score
        # score = score + 10
        score += 10

        if score > highest_score:
            highest_score = score
        score_sign.clear()
        score_sign.write(f"Skore: {score} Najvacsie skore: {highest_score}", align="center", font=("Arial", 18))
        

    for index in range(len(body_parts) - 1, 0, - 1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x,y)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)

    move()

    #kolizia do tela samotneho hada
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"
            #skryt casti tela
            for one_body_part in body_parts:
                one_body_part.goto(1500, 1500)

        #po kolizii vyprazdnime  list s castami tela
            body_parts.clear()

            score = 0
            score_sign.clear()
            score_sign.write(f"Skore: {score} Najvacsie skore: {highest_score}", align="center", font=("Arial", 18))

    time.sleep(0.1)
    

screen.exitonclick()