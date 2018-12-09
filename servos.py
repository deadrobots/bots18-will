from wallaby import *
import constants as c
import actions as a
import motors as m

def canGrab():
    set_servo_position(c.armServo, c.armDown)
    msleep(1000)  # Careful. 50 ms is not nearly enough time for the servo to fully move to its next position, BTW. -LMB
    set_servo_position(c.clawServo, c.clawOpen)
    msleep(1000)
    set_servo_position(c.clawServo, c.clawClose)
    msleep(1000)
    set_servo_position(c.armServo, c.armUpWithCan)
    msleep(1500)