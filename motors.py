from wallaby import *
import constants as c
import actions as a
import servos as s

def drive(lPer, rPer, dTime):
    motor(c.lMotor, lPer)
    motor(c.rMotor, rPer)
    msleep(dTime)
    ao()

def freezeBoth(): # Careful when using this function in a loop, as we saw. That last msleep() causes some confusion. -LMB
    freeze(c.lMotor)
    msleep(55)
    # msleep is to balance difference between stop times of Motors
    freeze(c.rMotor)
    
def backUpRight():
    freezeBoth()
    drive(-90, -95, 1000)
    drive(0, 100, 1000)
    msleep(200)
    
def backUpLeft():
    freezeBoth()
    drive(-90, -95, 1000)
    drive(100, 0, 1000)
    msleep(200)