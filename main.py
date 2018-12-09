#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import actions as a
# started work on using the camera, next time work with expanding the code used on the canSeeker function

def main():

    print "Let's Get Going"
    enable_servos()

    #a.randomBumpNavigate()

    #a.fullSequence()

    camera_open_black()
    msleep(1000)
    a.testConfidence()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();
