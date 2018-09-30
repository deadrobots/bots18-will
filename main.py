#!/usr/bin/python
import os, sys
from wallaby import *

#Test wait_for_button function
# this is a new comment

lMotor = 1
rMotor = 0
armServo = 0
clawServo = 1
clawOpen = 1850
clawClose = 1135
armDown = 1300
armUp = 0

def freezeBoth():
    freeze(lMotor)
    msleep(55)
    freeze(rMotor)
    msleep(225)

def drive(lPer, rPer, dTime):
    motor(lMotor, lPer)
    motor(rMotor, rPer)
    msleep(dTime)

def wait_for_button():
    print "Waiting for Button Press"
    while right_button() == 0:
        pass
    while right_button() == 1:
        print "Press Success"

def main():
    print "Let's Get Going"
    drive(95, 100, 1000)
    drive(-95, -100, 1000)
    for x in range(0, 4):
        print(x)
        drive(95, 100, 2000)
        drive(100, 0, 1175)
    freezeBoth()
    msleep(300)
    wait_for_button()
    enable_servos()
    set_servo_position(armServo, armDown)
    msleep(50)
    set_servo_position(clawServo, clawOpen)
    msleep(50)
    drive(95, 100, 3000)
    freezeBoth()
    set_servo_position(clawServo, clawClose)
    msleep(100)
    set_servo_position(armServo, armUp)
    msleep(1500)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();
