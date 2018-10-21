#!/usr/bin/python
import os, sys
from wallaby import *

#Grabs can successfully

# Great coding overall. Well done.
# Could use a few comments here and there, but you've stuck with the
# naming conventions and have used constants where appropriate.
# Excellent work for being newer to the coding side of things.
# Next up will be making separate files for constants and utility/action functions
# and importing them using the "import" statement. I'll walk you all through that
# -LMB

lMotor = 1
rMotor = 0
armServo = 0
clawServo = 1
clawOpen = 1850
clawClose = 1300
armDown = 1300
armUp = 0
topHat = 1

def freezeBoth():
    freeze(lMotor)
    msleep(55) #msleep is to balance difference between stop times of motors
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

def canGrab():
    set_servo_position(armServo, armDown)
    msleep(50)
    set_servo_position(clawServo, clawOpen)
    msleep(50)
    drive(90, 100, 3000)
    freezeBoth()
    set_servo_position(clawServo, clawClose)
    msleep(100)
    set_servo_position(armServo, armUp)
    msleep(1500)

def main():
    print "Let's Get Going"
    enable_servos()

    drive(95, 100, 1000)
    drive(-95, -100, 1000)
    for x in range(0, 4):
        print(x)
        drive(90, 100, 2000)
        drive(100, 0, 1175)
    freezeBoth()
    msleep(300)

    wait_for_button()

    canGrab()

    wait_for_button()

    startTime = seconds()

	# What does this block of code do? Comments would be helpful here.
	# If this code was in a function that was named well enough, I might not even need a comment
	# to understand what was going on -LMB
    while (seconds() - startTime) < 5:
        if analog(topHat) > 2000:
            drive(100, 20, 10)
        else:
            drive(20, 100, 10)
    freezeBoth()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();
