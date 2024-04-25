from turtle import Turtle, Screen
import random

tommy = Turtle()
tommy.shape("turtle")
tommy.color("green")
tommy.pensize(2)

#######ukony tommyho krok po korku
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
    
#######tommyho prerusovana ciara po kroku
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
#####farebna kresba s nahodnymi farbami a vzdy o uhol viac
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

##### Random walk / nahodny pohyb tommyho

#list farieb
farby = ["green", "red", "blue", "yellow", "black", "pink"]

#list uhlov otacania tommyho
otacanie = [0, 45, 90, 135, 180, 270]

#pociatocna rychlost
speed = 1


for number in range (200):
    #Nahodna farba
    random_farba = random.choice(farby)
    tommy.pencolor(random_farba)
    #Hrubka ciary sa zvysuje
    if number <= 15:
        tommy.pensize(number)
    #Posun o 30
    tommy.forward(30)
    #Nahodne otocenie z listu otacanie
    tommy.right(random.choice(otacanie))
    #Zvysenie rychlosti
    tommy.speed(speed)
    speed += 1



my_screen = Screen()
my_screen.exitonclick()