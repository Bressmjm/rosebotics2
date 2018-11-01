"""
  Capstone Project.  Code written by Dylan Verst.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    def polygon(n, robot):
        deg_total = 180 * (n - 2)
        deg_turn = deg_total / n
        for k in range(n):
            robot.drive_system.go_straight_inches(24)
            time.sleep(2)
            robot.drive_system.spin_in_place_degrees(180 - deg_turn)
            time.sleep(2)

    def follow_line(robot):
        start_time = time.time()
        while True:
            robot.drive_system.start_moving()
            robot.color_sensor.wait_until_intensity_is_greater_than(20)
            robot.drive_system.stop_moving()
            robot.drive_system.turn_degrees(3)
            if time.time() - 60 >= start_time:
                break

    def go_until(color, robot):
        robot.drive_system.start_moving()
        robot.color_sensor.wait_until_color_is(color)
        robot.drive_system.stop_moving()

    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    polygon(3, robot)
    polygon(4, robot)
    polygon(5, robot)
    polygon(6, robot)
    time.sleep(30)
    follow_line(robot)
    time.sleep(30)
    go_until(rb.Color.RED.value, robot)
    time.sleep(5)
    go_until(rb.Color.BLUE.value, robot)
    time.sleep(5)
    go_until(rb.Color.BLACK.value, robot)
    time.sleep(5)
    go_until(rb.Color.BROWN.value, robot)
    time.sleep(5)
    go_until(rb.Color.GREEN.value, robot)
    time.sleep(5)
    go_until(rb.Color.YELLOW.value, robot)
    time.sleep(5)
    go_until(rb.Color.WHITE.value, robot)


def polygon(n, robot):
    deg_total = 180 * (n - 2)
    deg_turn = deg_total / n
    for k in range(n):
        robot.drive_system.go_straight_inches(24)
        robot.drive_system.spin_in_place_degrees(deg_turn)


def follow_line(robot):
    start_time = time.time()
    while True:
        robot.drive_system.start_moving()
        robot.color_sensor.wait_until_intensity_is_greater_than(0)
        robot.drive_system.stop_moving()
        robot.drive_system.turn_degrees(3)
        if time.time() - 60 >= start_time:
            break


def go_until(color, robot):
    robot.drive_system.start_moving()
    while True:
        if robot.color_sensor.get_value() == color:
            robot.drive_system.stop_moving()
            break


main()
