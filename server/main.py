#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

# Initialize server
server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Initialize EV3 touch sensor and motors
touch = TouchSensor(Port.S1)
touchButton = "Off"

# The server must be started before the client!
print('Waiting for connection...')
server.wait_for_connection()
print('Connected!')

# Create a loop to react to buttons
while True:

    # Check for center button events
    if Button.CENTER in ev3.buttons.pressed():
        break

    # If the touch sensor is pressed
    if touch.pressed() is True and touchButton == "Off":

        # Send message to client that touch is on
        mbox.send('MOTORON')
        touchButton = "On"

    # If the touch sensor is released
    elif touch.pressed() is False and touchButton == "On":

        # Send message to client that touch is off
        mbox.send('MOTOROFF')
        touchButton = "Off"

    wait(20)

# Send message to client to stop
mbox.send('COMPLETE')

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
