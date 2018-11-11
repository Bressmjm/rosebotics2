"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Joshua Bressman.
"""
# ------------------------------------------------------------------------------
# TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, review the "big picture" of laptop-robot
# TODO:    communication, per the comment in mqtt_sender.py.
# TODO:    Once you understand the "big picture", delete this TODO.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()
    rc = RemoteControlEtc(robot)
    client = com.MqttClient(rc)
    client.connect_to_pc()

# Individual Project- Joshua Bressman
# Dance Path
def dance_routine(n, robot, color):
    # Statement
    print('I am a dancing robot. Watch me dance!')
    # Sound
    ev3.Sound.speak("I am a dancing robot. Watch me dance!").wait()
    polygon_list = ['triangle', 'quadrilateral', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'enneagon',
                    'decagon', 'hendecagon', 'dodecagon', 'tridecagon', 'tetradecagon', 'pendedecagon',
                    'hexdecagon', 'heptdecagon', 'octdecagon', 'enneadecagon', 'icosagon']
    deg_total = 180 * (n - 2)
    deg_turn = deg_total / n
    totalspins = n
    while True:
        robot.drive_system.go_straight_inches(24)
        time.sleep(2)
        robot.drive_system.spin_in_place_degrees(180 - deg_turn)
        time.sleep(2)
        # Moving A Blocking Object
        if robot.InfraredAsProximitySensor.get_distance_to_nearest_object() <= 10:
            robot.ArmAndClaw.raise_arm_and_close_claw()
        # Statement
        print('Get out of my way I am trying to make art!')
        # Sounds
        ev3.Sound.speak("Get out of my way I am trying to make art!").wait()
        # Spin When Encounters A Color
        if robot.color_sensor.get_color == color:
            robot.drive_system.spin_in_place_degrees(360)
            totalspins = totalspins - 1
            # Statement
            print('I am spinning at the color', color)
            # Sounds
            ev3.Sound.speak("I am spinning at the color", color).wait()
        if totalspins == 0:
            break
    # Statement
    print("I danced in the shape of an", polygon_list[n - 3])
    # Sounds
    ev3.Sound.speak("I danced in the shape of an", polygon_list[n - 3]).wait()

    # --------------------------------------------------------------------------
    # TODO: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 5. Add a class for your "delegate" object that will handle messages
    # TODO:    sent from the laptop.  Construct an instance of the class and
    # TODO:    pass it to the MqttClient constructor above.  Augment the class
    # TODO:    as needed for that, and also to handle the go_forward message.
    # TODO:    Test by PRINTING, then with robot.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------
    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed() == True:
            ev3.Sound.beep()
        if robot.beacon_button_sensor.is_top_blue_button_pressed() == True:
            speech = ev3.Sound.speak("Hello, How are you?")
            speech.play()
        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work

class RemoteControlEtc(object):
    def __init__(self, robot):
        '''
        Stores the robot.
        :type robot: rb.Snatch3rRobot
        '''
        self.robot = robot

# Individual Project- Joshua Bressman
    # Dance Path
    def dance_routine(self, n, color):
        # Statement
        print('I am a dancing robot. Watch me dance!')
        # Sound
        ev3.Sound.speak("I am a dancing robot. Watch me dance!").wait()
        polygon_list = ['triangle', 'quadrilateral', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'enneagon',
                        'decagon', 'hendecagon', 'dodecagon', 'tridecagon', 'tetradecagon', 'pendedecagon',
                        'hexdecagon', 'heptdecagon', 'octdecagon', 'enneadecagon', 'icosagon']
        deg_total = 180 * (n - 2)
        deg_turn = deg_total / n
        totalspins = n
        while True:
            self.robot.drive_system.go_straight_inches(24)
            time.sleep(2)
            self.robot.drive_system.spin_in_place_degrees(180 - deg_turn)
            time.sleep(2)
            # Moving A Blocking Object
            if self.robot.proximity_sensor.get_distance_to_nearest_object() <= 10:
                self.robot.arm.raise_arm_and_close_claw()
            # Statement
            print('Get out of my way I am trying to make art!')
            # Sounds
            ev3.Sound.speak("Get out of my way I am trying to make art!").wait()
            # Spin When Encounters A Color
            if self.robot.color_sensor.get_color == color:
                self.robot.drive_system.spin_in_place_degrees(360)
                totalspins = totalspins - 1
                # Statement
                print('I am spinning at the color', color)
                # Sounds
                ev3.Sound.speak("I am spinning at the color", color).wait()
            if totalspins == 0:
                break
        # Statement
        print("I danced in the shape of an", polygon_list[n - 3])
        # Sounds
        ev3.Sound.speak("I danced in the shape of an", polygon_list[n - 3]).wait()
    '''
    def go_foward(self, speedstring):
        print("tells the robot to go forward")
        speed = int(speedstring)
        self.robot.drive_system.start_moving(speed, speed)
    '''

main()