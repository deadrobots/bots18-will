#!/usr/bin/python
import os, sys
from wallaby import *

# line follows till detecting can CHANGE VALES IN CAN GRAB FOR CAMERA MOUNT

lMotor = 1
rMotor = 0
armServo = 0
clawServo = 1
clawOpen = 1850
clawClose = 1300
armDown = 1300
armUp = 0
topHat = 1
et = 0

# Again, great work Will. It's about time to start separating code out to separate files
# (so one file doesn't get too cumbersome)
# I would suggest the following format:
# constants.py (holds your constants!)
# actions.py  (contains collections of motor and servo commands to perform an action. EX: grabCan() )
# servo.py (just holds servo related functions. Not motor commands, generally)
# motors.py (just holds your motor commands. drive(), driveTimed(), driveUntilBlackLine(), stuff like that.)
# main.py (where everything starts!)

def freezeBoth(): # Careful when using this function in a loop, as we saw. That last msleep() causes some confusion. -LMB
    freeze(lMotor)
    msleep(55)
    # msleep is to balance difference between stop times of motors
    freeze(rMotor)
    msleep(1000)

def drive(lPer, rPer, dTime):
    motor(lMotor, lPer)
    motor(rMotor, rPer)
    msleep(dTime)
    ao()

def wait_for_button():
    print "Waiting for Button Press"
    while right_button() == 0:
        pass
    while right_button() == 1:
        print "Press Success"

def canGrab():
    set_servo_position(armServo, armDown)
    msleep(50) # Careful. 50 ms is not nearly enough time for the servo to fully move to its next position, BTW. -LMB
    set_servo_position(clawServo, clawOpen)
    msleep(50)
    set_servo_position(clawServo, clawClose)
    msleep(100)
    set_servo_position(armServo, armUp)
    msleep(1500)

def main():
    print "Let's Get Going"
    enable_servos()

    drive(95, 100, 1000)
    drive(-95, -100, 1000)
    #for x in range(0, 4):
    #    print(x)
    #    drive(90, 100, 2000)
    #    drive(100, 0, 1175)
    # drives a square

    wait_for_button()

    set_servo_position(armServo, armDown)
    msleep(50)
    set_servo_position(clawServo, clawOpen)
    msleep(50)
    # sets arm down and claw open

    while analog(et) < 2200: # checks ET sensor for distance from can
        if analog(topHat) > 2000: # Reads Tophat sensor, >2000 is black
            drive(90, 0, 10)
        else:
            drive(0, 90, 10)

    canGrab()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();
