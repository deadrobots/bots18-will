#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import actions as a
# all functions in use work, next time work on using the camera


# Again, great work Will. It's about time to start separating code out to separate files
# (so one file doesn't get too cumbersome)
# I would suggest the following format:
# constants.py (holds your constants!)
# actions.py  (contains collections of Motor and servo commands to perform an action. EX: grabCan() )
# servos.py (just holds servo related functions. Not Motor commands, generally)
# Motors.py (just holds your Motor commands. drive(), driveTimed(), driveUntilBlackLine(), stuff like that.)
# main.py (where everything starts!)

# Just the one comment, really. You should take a stab at the camera project. I think you'll do well at the software component -LMB

def main():

    print "Let's Get Going"
    enable_servos()
    a.randomBumpNavigate()

    #a.fullSequence()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();
