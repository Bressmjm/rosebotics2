"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Achintya Gupta.
"""
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, discuss the "big picture" of laptop-robot
# TODO:    communication:
# TODO:      - One program runs on your LAPTOP.  It displays a GUI.  When the
# TODO:        user presses a button intended to make something happen on the
# TODO:        ROBOT, the LAPTOP program sends a message to its MQTT client
# TODO:        indicating what it wants the ROBOT to do, and the MQTT client
# TODO:        SENDS that message TO a program running on the ROBOT.
# TODO:
# TODO:      - Another program runs on the ROBOT. It stays in a loop, responding
# TODO:        to events on the ROBOT (like pressing buttons on the IR Beacon).
# TODO:        It also, in the background, listens for messages TO the ROBOT
# TODO:        FROM the program running on the LAPTOP.  When it hears such a
# TODO:        message, it calls the method in the DELAGATE object's class
# TODO:        that the message indicates, sending arguments per the message.
# TODO:
# TODO:  Once you understand the "big picture", delete this TODO (if you wish).
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    client=com.MqttClient()
    client.connect_to_ev3()
    setup_gui(root,client)
    root.mainloop()
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------


def setup_gui(root_window,client):
    """ Constructs and sets up widgets on the given window. """
    frame1 = ttk.Frame(root_window, padding=10)
    frame2= ttk.Frame(root_window, padding=10)
    frame1.grid()

    speed_entry_box = ttk.Entry(frame1)
    go_forward_button = ttk.Button(frame1, text="Go forward")
    go_backward_button = ttk.Button(frame1,text='Go backward')
    turn_right_button = ttk.Button(frame1,text='Turn right')
    turn_left_button = ttk.Button(frame1,text='Turn left')
    stop_button = ttk.Button(frame1,text='Stop moving')
    choose_color_button= ttk.Button(frame1,text='Choose color')
    yellow_button = ttk.Button(frame2,text='Yellow')

    speed_entry_box.grid()
    go_forward_button.grid(row=1, column=1)
    go_backward_button.grid(row=1, column=2)
    turn_left_button.grid()
    turn_right_button.grid()
    stop_button.grid()
    choose_color_button.grid()
    yellow_button.grid()



    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box,client)
    choose_color_button['command']=lambda: handle_choose_color(frame1,frame2)
    yellow_button['command']=lambda: color_set('SIG1',client,frame1,frame2)

def handle_choose_color(frame1,frame2):
    frame1.grid_remove()
    frame2.grid()

def color_set(color,client,frame1,frame2):
    client.send_message('choose_color',[color])
    frame2.grid_remove()
    frame1.grid()


def handle_go_forward(speedbox,client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed = speedbox.get()
    client.send_message('go_forward',[speed])
    # --------------------------------------------------------------------------
    #-------


main()
