"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""
import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()
   # while True:
        #blob = robot.camera.get_biggest_blob()
        #if (blob.height * blob.width) >= 600:
            #print('test')
            #ev3.Sound.beep().wait()
        #if robot.touch_sensor.is_pressed() == True:
            #break


########################################################################

# Individual Project- Joshua Bressman
    # Dance Path
    def dance_routine(n, robot, color):
        polygon_list = ['triangle','quadrilateral','pentagon','hexagon','heptagon','octagon','enneagon','decagon','hendecagon','dodecagon','tridecagon','tetradecagon','pendedecagon','hexdecagon','heptdecagon','octdecagon','enneadecagon','icosagon']
        deg_total = 180 * (n - 2)
        deg_turn = deg_total / n
        totalspins = n
        while True:
            robot.drive_system.go_straight_inches(24)
            time.sleep(2)
            robot.drive_system.spin_in_place_degrees(180 - deg_turn)
            time.sleep(2)
            # Spin When Encounters A Color
            if robot.color_sensor.get_color == color:
                robot.drive_system.spin_in_place_degrees(360)
                totalspins = totalspins - 1
                # Statement
                print('I am spinning at the color',color)
                # Sounds
            if totalspins == 0:
                break
        # Statement
        print("I danced in the shape of an",polygon_list[n-3])
        # Sounds
    # Moving A Blocking Object
        # Sounds
        print('Get out of my way I am trying to make art!')
        # Statement




    """ Runs YOUR specific part of the project """


main()
