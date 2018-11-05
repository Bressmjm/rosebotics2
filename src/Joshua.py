"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""
import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()
    while True:
        blob = robot.camera.get_biggest_blob()
        if (blob.height * blob.width) >= 50:
            print('test')
            ev3.Sound.beep().wait()
        if robot.touch_sensor.is_pressed() == True:
            break



    """ Runs YOUR specific part of the project """


main()
