"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Dylan Verst.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this .
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TOD: 2. With your instructor, review the "big picture" of laptop-robot
# TOD:    communication, per the comment in mqtt_sender.py.
# TOD:    Once you understand the "big picture", delete this TOD.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # TOD: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TOO.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    # --------------------------------------------------------------------------
    # TOD: 4. Add code that constructs a   com.MqttClient   that will
    # TOD:    be used to receive commands sent by the laptop.
    # TOD:    Connect it to this robot.  Test.  When OK, delete this ODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TOD: 5. Add a class for your "delegate" object that will handle messages
    # TOD:    sent from the laptop.  Construct an instance of the class and
    # TOD:    pass it to the MqttClient constructor above.  Augment the class
    # TOD:    as needed for that, and also to handle the go_forward message.
    # TOD:    Test by PRINTING, then with robot.  When OK, delete this TOD
    #  --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # TOD: 6. With your instructor, discuss why the following WHILE loop,
    # TOD:    that appears to do nothing, is necessary.
    # TOD:    When you understand this, delete this TOD.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # TOD 7. Add code that makes the robot beep if the top-red button
        # TOD:    on the Beacon is pressed.  Add code that makes the robot
        # TOD:    speak "Hello. How are you?" if the top-blue button on the
        # TOD:    Beacon is pressed.  Test.  When done, delete this TDO.
        # --------------------------------------------------------------------
        #if robot.proximity_sensor.get_distance_to_nearest_object_in_inches() <= 2 and a == 0:
            #print('Picking up object')
            #robot.arm.move_arm_to_position(30)
            #a = 1
        #else:
        a = 0
        while robot.beacon_button_sensor.is_top_red_button_pressed() or robot.beacon_button_sensor.is_top_blue_button_pressed() or robot.beacon_button_sensor.is_bottom_red_button_pressed() or robot.beacon_button_sensor.is_bottom_blue_button_pressed():
            if robot.beacon_button_sensor.is_top_red_button_pressed() and robot.beacon_button_sensor.is_top_blue_button_pressed() and robot.beacon_button_sensor.is_bottom_red_button_pressed() and robot.beacon_button_sensor.is_bottom_blue_button_pressed():
                if a == 0:
                    robot.arm.raise_arm_and_close_claw()
                    a = 1
                else:
                    robot.arm.calibrate()
                    a = 0
            else:
                if robot.beacon_button_sensor.is_top_blue_button_pressed():
                    robot.drive_system.right_wheel.start_spinning()
                if robot.beacon_button_sensor.is_bottom_red_button_pressed():
                    robot.drive_system.left_wheel.start_spinning(-100)
                if robot.beacon_button_sensor.is_bottom_blue_button_pressed():
                    robot.drive_system.right_wheel.start_spinning(-100)
                if robot.beacon_button_sensor.is_top_red_button_pressed():
                    robot.drive_system.left_wheel.start_spinning()
        if not robot.beacon_button_sensor.is_top_blue_button_pressed():
            robot.drive_system.stop_moving()
        if not robot.beacon_button_sensor.is_bottom_red_button_pressed():
            robot.drive_system.stop_moving()
        if not robot.beacon_button_sensor.is_bottom_blue_button_pressed():
            robot.drive_system.stop_moving()
        if not robot.beacon_button_sensor.is_top_red_button_pressed():
            robot.drive_system.stop_moving()
        if robot.color_sensor.get_reflected_intensity() >= rc.intensity:
            ev3.Sound.beep()
            time.sleep(1)


class RemoteControlEtc(object):
    def __init__(self, robot):
        """"
        Stores the robot.
          :type   robot:  rb.Snatch3Robot
        """
        self.robot = robot
        self.intensity = 100

    def set_intensity(self, intensity):
        print('Setting intensity detector to', intensity)
        self.intensity = int(intensity)


main()
