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


main()
