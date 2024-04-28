from turtle import Turtle, Screen
import random
import turtle



tommy = Turtle()
tommy.shape("arrow")
tommy.color("red")
tommy.pensize(1)

tommy2 = Turtle()
tommy2.color("green")
tommy2.shape("arrow")
tommy2.pensize(1)

###############################
#######ukony tommyho krok po korku
###################################
""" tommy.forward(100)
tommy.right(90)
tommy.forward(100)
tommy.right(90)
tommy.forward(100)
tommy.right(90)
tommy.forward(100)
tommy.right(90) """

#ukony tommyho krok v cykle
""" for _ in range(4):
    tommy.right(90)
    tommy.forward(100) """


#######################################   
#######tommyho prerusovana ciara po kroku
###########################################
""" tommy.pendown()
tommy.forward(20)
tommy.penup()
tommy.forward(20)

tommy.pendown()
tommy.forward(20)
tommy.penup()
tommy.forward(20)

tommy.pendown()
tommy.forward(20)
tommy.penup()
tommy.forward(20) """

#tommyho prerusovana ciara po kroku

""" for _ in range(10):
    tommy.pendown()
    tommy.forward(20)
    tommy.penup()
    tommy.forward(20)
 """
##############################################
#####farebna kresba s nahodnymi farbami a vzdy o uhol viac
##############################################
""" farby = ["green", "red", "blue", "yellow", "black", "pink"] """

#krok po korku
""" for _ in range(3):
    tommy.forward(100)
    tommy.right(120) # 360 : 3

for _ in range(4):
    tommy.forward(100)
    tommy.right(90) # 360 : 4

for _ in range(5):
    tommy.forward(100)
    tommy.right(72) # 360 : 5 """

# v cykle s nahodnymi farbami
""" pohyb = 3

while pohyb != 9:
    random_color = random.choice(farby)
    tommy.pencolor(random_color)
    for _ in range(pohyb):
        tommy.forward(100)
        tommy.right(360/pohyb)
    pohyb += 1 """


#########################################
##### Random walk / nahodny pohyb tommyho
#########################################
#list farieb_toto som zrusil, lebo som pouzil tuple radnom color()
#farby = ["green", "red", "blue", "yellow", "black", "pink"]

#zmena farevneho modu
"""turtle.colormode(255)"""

""" def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

#list uhlov otacania tommyho
otacanie = [0, 45, 90, 135, 180, 270]

#pociatocna rychlost
speed = 1


for number in range (200):
    #Nahodna farba
    tommy.pencolor(random_color())
    #Hrubka ciary sa zvysuje
    if number <= 10:
        tommy.pensize(number)
    #Posun o 30
    tommy.forward(30)
    #Nahodne otocenie z listu otacanie
    tommy.right(random.choice(otacanie))
    #Zvysenie rychlosti
    tommy.speed(speed)
    speed += 1
 """


##########################################
#####SPIROMETER
##########################################

#Zmena farebneho modu
""" turtle.colormode(255)
tommy.speed(20)

#Funkcia na generovanie farby
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def  spirograf(gap):
    for number in range(int(360/gap)):
        tommy.pencolor(random_color())
        tommy.circle(80)
        tommy.left(gap)

spirograf(5) """

########################################
######DIAGRAM
########################################

""" colors = ["red","green","blue","yellow","pink","purple"]

arrow = Turtle("arrow")

for x in range(200):
    arrow.pencolor(colors[x%6])
    arrow.forward(x)
    arrow.left(60) """


################################
#####VYPLNENIE TVARU (FILL)
################################
""" tommy.pen(fillcolor="red")
tommy.begin_fill()

for _ in range(4):
    tommy.forward(80)
    tommy.left(90)

tommy.end_fill() """

################################
#####KURHY
################################

tommy.circle(20)

#range (od priemeru 30 do priemeru 80 po zvacseni o 10)
for n in range(30, 80, 10):
    tommy2.circle(n)


my_screen = Screen()
my_screen.exitonclick()