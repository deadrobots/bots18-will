from wallaby import *
import constants as c
import motors as m
import servos as s
import math
import random

def wait_for_button():
    print "Waiting for Button Press"
    while right_button() == 0:
        pass
    while right_button() == 1:
        print "Press Success"

def forwardBackLine():
    m.drive(95, 100, 1000)
    m.drive(-95, -100, 1000)

def square():

    for x in range(0, 4):
        print(x)
        m.drive(90, 100, 2000)
        m.drive(100, 0, 1175)


def lineFollowIntoGrab():
    while analog(c.et) < 2200: # checks ET sensor for distance from can
        if analog(c.topHat) > 2000: # Reads top hat sensor, >2000 is black
            m.drive(90, 0, 10)
        else:
            m.drive(0, 90, 10)

def clawDropPreperation():
    set_servo_position(c.armServo, c.armDown)
    msleep(1000)
    set_servo_position(c.clawServo, c.clawOpen)
    msleep(1000)

def bumpNavigate():

    set_servo_position(c.armServo, c.armUp)

    startTime = seconds()
    while (seconds() - startTime) < 60:
        dirX = gyro_x()
        dirY = gyro_y()
        dirZ = gyro_z()
        resultantDirection = math.sqrt(math.pow(dirX, 2) + math.pow(dirY, 2) + math.pow(dirZ, 2))
        # finds resultant gyro vector
        if resultantDirection <= 400:
            m.drive(90, 95, 100)
        else:
            m.freezeBoth()              # stops motors, then backs up and turns right
            m.drive(-90, -95, 1000)
            m.drive(0, 100, 1000)
            msleep(200)

def randomBumpNavigate():
    set_servo_position(c.armServo, c.armUp)

    startTime = seconds()
    while (seconds() - startTime) < 60:
        dirX = gyro_x()
        dirY = gyro_y()
        dirZ = gyro_z()
        resultantDirection = math.sqrt(math.pow(dirX, 2) + math.pow(dirY, 2) + math.pow(dirZ, 2))
        # finds resultant gyro vector
        if resultantDirection <= 400:
            m.drive(90, 95, 100)
        else:
            output = random.randint(0,1)

            if output == 0:
                m.backUpRight()
            else:
                m.backUpLeft()

def canSeeker():
    camera_open_black()
    msleep(5000)
    while True:
        camera_update()
        objectCount = get_object_count(c.can)
        if objectCount > 1:
            m.freezeBoth() #input code that would travel to and grab can
            clawDropPreperation()
            m.drive(95, 100, 1000)
            s.canGrab()
        else:
            motor(c.rMotor, 100)


def testConfidence():
    while not left_button():
        camera_update()
        objectCount = get_object_count(c.can)
        if objectCount > 0:
            objectConfidence = get_object_confidence(c.can, 0)
            print objectConfidence
        msleep(50)


def fullSequence():
    forwardBackLine()       # moves forward one second, backward one second
    wait_for_button()
    square()                # drives a square shape
    wait_for_button()
    clawDropPreperation()   # lowers arm and opens claw
    lineFollowIntoGrab()    # will line follow until spots a can
    s.canGrab()             # following can sight, will pick up can and lift up
    print "Full Sequence Complete!"