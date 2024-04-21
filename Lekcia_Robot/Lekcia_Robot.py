class Robot():

#construktor

    def __init__(self, bateria, dlzka_ruky):
        self.bat = bateria
        self.dl_ruk = dlzka_ruky
        self.ukony_do_opravy = 1000

    def krok_vpred(self):
        print("Robot urobil krok vpred")
        self.ukony_do_opravy -= 1

    def krok_vzad(self):
        print("Robot urobil krok vzad")
        self.ukony_do_opravy -= 1

#objekty

robot_1 = Robot(24, 0.6)
robot_2 = Robot(48, 0.5)
robot_3 = Robot(62, 0.4)
robot_4 = Robot(74, 0.3)

print(robot_1.bat)
print(robot_1.dl_ruk)
print(robot_1.ukony_do_opravy)
robot_1.krok_vpred()
robot_1.krok_vzad()
print(robot_1.ukony_do_opravy)

print(robot_2.bat)
print(robot_2.dl_ruk)
print(robot_2.ukony_do_opravy)

print(robot_3.bat)
print(robot_3.dl_ruk)
print(robot_3.ukony_do_opravy)

print(robot_4.bat)
print(robot_4.dl_ruk)
print(robot_4.ukony_do_opravy)
