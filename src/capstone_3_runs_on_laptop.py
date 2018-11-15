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
    setup(root)


    root.mainloop()
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------


def setup(root_window):
    """ Constructs and sets up widgets on the given window. """
    frame1 = ttk.Frame(root_window, padding=10)
    frame2= ttk.Frame(root_window, padding=10)
    frame1.grid()

    speed_entry_box = ttk.Entry(frame1)
    textbox0=ttk.Label(frame2,text='Pick your Treasure')
    textbox= ttk.Label(frame1,text='Welcome to the underwater treasure hunter')
    textbox1=ttk.Label(frame1,text='Searching for Object')
    textbox2=ttk.Label(frame1,text='Object found, attempting retrieval')
    go_forward_button = ttk.Button(frame1, text="Go forward")
    go_backward_button = ttk.Button(frame1,text='Go backward')
    turn_right_button = ttk.Button(frame1,text='Turn right')
    turn_left_button = ttk.Button(frame1,text='Turn left')
    stop_button = ttk.Button(frame1,text='Stop moving')
    choose_color_button= ttk.Button(frame1,text='Choose color')
    fetch_button= ttk.Button(frame1,text='Hunt')
    yellow_button = ttk.Button(frame2,text='Gold')
    red_button = ttk.Button(frame2,text='Rubies')
    blue_button = ttk.Button(frame2,text='Sapphires')
    green_button = ttk.Button(frame2,text='Emeralds')

    textbox.grid(row=1,column=1, columnspan=3)
    speed_entry_box.grid(row=2,column=2)
    go_forward_button.grid(row=3, column=2)
    go_backward_button.grid(row=5, column=2)
    turn_left_button.grid(row=4,column=1)
    turn_right_button.grid(row=4,column=3)
    stop_button.grid(row=4,column=2)
    choose_color_button.grid(row=6,column=1)
    fetch_button.grid(row=6,column=3)
    textbox0.grid(row=1,column=1, columnspan=2)
    yellow_button.grid(row=2,column=1)
    red_button.grid(row=2,column=2)
    blue_button.grid(row=3,column=1)
    green_button.grid(row=3,column=2)

    gc=Gui_control(textbox1,textbox2)
    client=com.MqttClient(gc)
    client.connect_to_ev3()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box,client)
    go_backward_button['command'] = \
        lambda: handle_go_backward(speed_entry_box,client)
    turn_right_button['command']=lambda: handle_turn_right(speed_entry_box,client)
    turn_left_button['command']=lambda: handle_turn_left(speed_entry_box,client)
    choose_color_button['command']=lambda: handle_choose_color(frame1,frame2)
    yellow_button['command']=lambda: color_set('SIG1',client,frame1,frame2)
    red_button['command'] = lambda: color_set('SIG2', client, frame1, frame2)
    blue_button['command'] = lambda: color_set('SIG3', client, frame1, frame2)
    green_button['command'] = lambda: color_set('SIG4', client, frame1, frame2)
    stop_button['command']=lambda: handle_stop_moving(client)
    fetch_button['command']=lambda: handle_fetch(client,speed_entry_box)

class Gui_control(object):
    def __init__(self,textbox1,textbox2):
        self.text1=textbox1
        self.text2=textbox2
    def searching(self):
        print('search')
        self.text1.grid(row=7,column=1, columnspan=3)
    def found(self):
        print('found')
        self.text1.grid_remove()
        self.text2.grid(row=7,column=1, columnspan=3)

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

def handle_go_backward(speedbox, client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed = speedbox.get()
    client.send_message('go_backward', [speed])

def handle_turn_right(speedbox, client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed = speedbox.get()
    client.send_message('turn_right', [speed])

def handle_turn_left(speedbox, client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed = speedbox.get()
    client.send_message('turn_left', [speed])

def handle_stop_moving(client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    client.send_message('stop_moving')

def handle_fetch(client,speedbox):
    speed=speedbox.get()
    client.send_message('fetch',[speed])




    # --------------------------------------------------------------------------
    #-------


main()
