"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()
    blob = robot.camera.get_biggest_blob()
    while True:
        if (blob.height * blob.width) >= 600:
            ev3.Sound.beep().wait()


    """ Runs YOUR specific part of the project """


main()
