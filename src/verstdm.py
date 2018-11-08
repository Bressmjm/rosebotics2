"""
  Capstone Project.  Code written by Dylan Verst.
  Fall term, 2018-2019.
"""

import ev3dev.ev3 as ev3
import time as t
import rosebotics_new as rb1


def main():
    robot = rb1.Snatch3rRobot()
    t.sleep(1)
    robot.touch_sensor.wait_until_pressed()
    # test_drive_system(robot)
    # t.sleep(1)
    # robot.touch_sensor.wait_until_pressed()
    test_color_sensor(robot)
    # t.sleep(1)
    # robot.touch_sensor.wait_until_pressed()
    # test_polygon(robot)
    # t.sleep(1)
    # robot.touch_sensor.wait_until_pressed()
    # test_follow_track(robot)
    # t.sleep(1)
    # robot.touch_sensor.wait_until_pressed()
    # test_arm_and_claw(robot)
    # t.sleep(1)
    # robot.touch_sensor.wait_until_pressed()
    # test_beeps(robot)


def test_drive_system(robot):
    robot.drive_system.go_straight_inches(10)
    t.sleep(1)
    robot.touch_sensor.wait_until_pressed()
    robot.drive_system.spin_in_place_degrees(180)
    t.sleep(1)
    robot.touch_sensor.wait_until_pressed()
    robot.drive_system.turn_degrees(-180)


def test_color_sensor(robot):
    color_sensor(rb1.Color.RED.value, robot)
    robot.touch_sensor.wait_until_pressed()
    color_sensor(rb1.Color.BLUE.value, robot)
    robot.touch_sensor.wait_until_pressed()
    color_sensor(rb1.Color.GREEN.value, robot)


def color_sensor(color, robot):
    robot.drive_system.start_moving()
    while True:
        if robot.color_sensor.get_color() == color:
            robot.drive_system.stop_moving()
            break


def test_polygon(robot):
    polygon(3, robot)
    t.sleep(.5)
    polygon(4, robot)
    t.sleep(.5)
    polygon(5, robot)


def polygon(sides, robot):
    for i in range(sides):
        robot.drive_system.go_straight_inches(12)
        t.sleep(.5)
        robot.drive_system.spin_in_place_degrees(180 - 180 * (sides - 2) / sides)


def test_follow_track(robot):
    while True:
        robot.drive_system.start_moving(30, 30)
        if robot.color_sensor.get_reflected_intensity() > 30:
            robot.drive_system.turn_degrees(5)


def test_arm_and_claw(robot):
    touch_sensor = robot.touch_sensor
    arm = rb1.ArmAndClaw(touch_sensor)
    arm.move_arm_to_position(60)
    robot.touch_sensor.wait_until_pressed()
    arm.move_arm_to_position(30)
    robot.touch_sensor.wait_until_pressed()
    arm.move_arm_to_position(90)
    robot.touch_sensor.wait_until_pressed()
    arm.move_arm_to_position(0)


def test_beeps(robot):
    while True:
        if 15 >= robot.proximity_sensor.get_distance_to_nearest_object_in_inches() >= 9:
            ev3.Sound.beep()
        if robot.touch_sensor.get_value() == 1:
            break
    robot.touch_sensor.wait_until_released()
    while True:
        blob = robot.camera.get_biggest_blob()
        if blob.get_area() >= 1000:
            ev3.Sound.beep().wait()
        if robot.touch_sensor.get_value() == 1:
            break


main()
