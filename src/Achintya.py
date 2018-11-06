"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""
print('test')
import rosebotics_new as rb
print('test')
import time
print('test')
import ev3dev.ev3 as ev3
print('test')


def main():
    """ Runs YOUR specific part of the project """
    #robot=rb.Snatch3rRobot()
    #Test 1 (wait until pressed):
    #while True:
        #robot.touch_sensor.wait_until_pressed()
        #robot.drive_system.move_for_seconds(5)
    #Test 2 (wait until released):
    #robot=rb.Snatch3rRobot()
    #while True:
        #robot.touch_sensor.wait_until_released()
        #robot.drive_system.move_for_seconds(2)
    #Test 3 (go straight inches):
    #robot = rb.Snatch3rRobot()
    #robot.touch_sensor.wait_until_pressed()
    #robot.drive_system.go_straight_inches(5)
    #robot.touch_sensor.wait_until_pressed()
    #robot.drive_system.go_straight_inches(20)
    #Test 4 (wait until color is):
    #robot= rb.Snatch3rRobot()
    #robot.color_sensor.wait_until_color_is(rb.Color.BLACK.value)
    #robot.drive_system.move_for_seconds(1)
    #robot.color_sensor.wait_until_color_is(rb.Color.YELLOW.value)
    #robot.drive_system.move_for_seconds(1)
    #robot.color_sensor.wait_until_color_is(rb.Color.BLUE.value)
    #robot.drive_system.move_for_seconds(1)
    #Test 5 (wait until color is one of):
    #robot = rb.Snatch3rRobot()
    #colors = [rb.Color.BLUE.value, rb.Color.BROWN.value, rb.Color.RED.value]
    #while True:
        #robot.color_sensor.wait_until_color_is_one_of(colors)
        #robot.drive_system.move_for_seconds(1)
    #Test 6 (spin in place degrees):
    #robot = rb.Snatch3rRobot()
    #while True:
        #robot.touch_sensor.wait_until_pressed()
        #robot.drive_system.spin_in_place_degrees(90)
    #Test 7 (turn degrees):
    #robot = rb.Snatch3rRobot()
    #while True:
        #robot.touch_sensor.wait_until_pressed()
        #robot.drive_system.turn_degrees(90)
    #Test 8:
    #robot=rb.Snatch3rRobot()
    #robot.touch_sensor.wait_until_pressed()
    #m2.polygon(3,robot)
    #print('test1')
    #robot=rb.Snatch3rRobot()
    #print('test2')
    #while True:
        #if robot.proximity_sensor.get_distance_to_nearest_object_in_inches()>9 and robot.proximity_sensor.get_distance_to_nearest_object_in_inches()<15:
            #print('test3')
            #ev3.Sound.beep().wait()
        #if robot.touch_sensor.is_pressed():
            #print('test4')
            #break
    robot=rb.Snatch3rRobot()
    robot.drive_system.start_moving()
    robot.drive_system.left_wheel.reset_degrees_spun()
    list=[]
    while True:
        blob=robot.camera.get_biggest_blob()
        if blob.get_area()<=50:
            list=list+[robot.drive_system.left_wheel.get_degrees_spun()]
            robot.drive_system.left_wheel.reset_degrees_spun()
            robot.drive_system.stop_moving()
            robot.drive_system.start_moving(-100, 100)
            while True:
                blob=robot.camera.get_biggest_blob()
                if blob.get_area()>=50:
                    list = list + [robot.drive_system.left_wheel.get_degrees_spun()]
                    robot.drive_system.left_wheel.reset_degrees_spun()
                    robot.drive_system.stop_moving()
                    break
            robot.drive_system.start_moving()
        if robot.proximity_sensor.get_distance_to_nearest_object_in_inches()<=1:
            list = list + [robot.drive_system.left_wheel.get_degrees_spun()]
            robot.drive_system.left_wheel.reset_degrees_spun()
            robot.drive_system.stop_moving()
            break
    robot.arm.raise_arm_and_close_claw()
    for k in range(0,len(list),2):
        robot.drive_system.left_wheel.reset_degrees_spun()
        robot.drive_system.start_moving(-100,-100)
        while True:
            if robot.drive_system.left_wheel.get_degrees_spun()>=list[k]:
                robot.drive_system.stop_moving()
                break
        robot.drive_system.left_wheel.reset_degrees_spun()
        robot.drive_system.start_moving(100,-100)
        while True:
            if robot.drive_system.left_wheel.get_degrees_spun()>=list[k+1]:
                robot.drive_system.stop_moving()
                break
    robot.drive_system.left_wheel.reset_degrees_spun()
    robot.drive_system.start_moving(-100, -100)
    while True:
        if robot.drive_system.left_wheel.get_degrees_spun() >= list[len(list)-1]:
            robot.drive_system.stop_moving()
            break













main()