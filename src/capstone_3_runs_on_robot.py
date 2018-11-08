"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Achintya Gupta.
"""
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot=rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    rc = Remote_control(robot)
    client=com.MqttClient(rc)
    client.connect_to_pc()
    # --------------------------------------------------------------------------
    #

    # --------------------------------------------------------------------------
    # T
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('Hello. How are you?')
        # ----------------------------------------------------------------------

        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work

class Remote_control(object):
    def __init__(self,robot):
        """
        :type robot: rb.Snatch3rRobot
        """
        self.robot=robot
    def go_forward(self,speedstr):
        print('test',speedstr)
        speed=int(speedstr)
        self.robot.drive_system.start_moving(speed,speed)


main()