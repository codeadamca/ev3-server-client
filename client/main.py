#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# This is the name of the remote EV3 or PC we are connecting to.
SERVER = 'mike'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)
newMessage = ""

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize EV3 touch sensor and motors
motor = Motor(Port.A)

print('Establishing connection...')
client.connect(SERVER)
print('Connected!')

# Initialize a loop taht waits for instructions from the server
while True:

    mbox.wait()

    newMessage = mbox.read()

    if newMessage == "MOTORON":

        motor.dc(50)
        print("ON")

    elif newMessage == "MOTOROFF":

        motor.stop()
        print("OFF")

    elif newMessage == "COMPLETE":

        motor.stop()
        break

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
