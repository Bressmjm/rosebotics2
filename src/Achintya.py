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
    #robot.drive_system.go_straight_inches(20,-100)
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
        #robot.drive_system.spin_in_place_degrees(-90)
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
    #fetch()
    #robot=rb.Snatch3rRobot()
    #while True:
        #blob = robot.camera.get_biggest_blob()
        #if (blob.height * blob.width) >= 600:
            #print('test')
            #ev3.Sound.beep().wait()
        #if robot.touch_sensor.is_pressed() == True:
            #break





def fetch(speed):
    #goes up to an object of a specified color and brings it back to its initial position
    robot=rb.Snatch3rRobot()
    robot.drive_system.start_moving(speed,speed)
    robot.drive_system.left_wheel.reset_degrees_spun()
    list=[] #list records motion
    while True:
        blob=robot.camera.get_biggest_blob()
        if blob.get_area()<=10: #if off screen
            print('test1')
            list=list+[robot.drive_system.left_wheel.get_degrees_spun()]
            robot.drive_system.left_wheel.reset_degrees_spun()
            robot.drive_system.stop_moving()
            robot.drive_system.start_moving(-speed, speed)
            while True:
                # Turns until it sees object
                blob=robot.camera.get_biggest_blob()
                if blob.get_area()>=10:
                    print('test2')
                    robot.drive_system.stop_moving()
                    robot.drive_system.spin_in_place_degrees(-15,speed)
                    list = list + [robot.drive_system.left_wheel.get_degrees_spun()]
                    robot.drive_system.left_wheel.reset_degrees_spun()
                    break
            robot.drive_system.start_moving(speed,speed)
        blob=robot.camera.get_biggest_blob()
        if blob.get_area()>5000: #stops when the object is close enough to grab
            list = list + [robot.drive_system.left_wheel.get_degrees_spun()]
            robot.drive_system.left_wheel.reset_degrees_spun()
            robot.drive_system.stop_moving()
            break
    list.reverse()
    print(list)

#def retrace(robot,list,speed):
    #retraces the steps it took to get to the object
    robot.arm.raise_arm_and_close_claw() #grabs object
    for k in range(0,len(list)-1,2): #every other number in the list is a turn while the rest are the degrees moved forward
        robot.drive_system.left_wheel.reset_degrees_spun()
        robot.drive_system.start_moving(-speed,-speed)
        while True:
            if abs(robot.drive_system.left_wheel.get_degrees_spun())>=abs(list[k]):
                robot.drive_system.stop_moving()
                break
        robot.drive_system.left_wheel.reset_degrees_spun()
        robot.drive_system.start_moving(speed,-speed)
        while True:
            if abs(robot.drive_system.left_wheel.get_degrees_spun())>=abs(list[k+1]):
                robot.drive_system.stop_moving()
                break
    print('test')
    robot.drive_system.left_wheel.reset_degrees_spun()
    robot.drive_system.start_moving(-speed, -speed)
    while True: #it has an odd number of items, thus the last one is done separately
        if abs(robot.drive_system.left_wheel.get_degrees_spun()) >= abs(list[len(list)-1]):
            robot.drive_system.stop_moving()
            break
    print('test')
    robot.drive_system.spin_in_place_degrees(180) #spins to face you
    robot.arm.calibrate() #drops object at your feet


main()