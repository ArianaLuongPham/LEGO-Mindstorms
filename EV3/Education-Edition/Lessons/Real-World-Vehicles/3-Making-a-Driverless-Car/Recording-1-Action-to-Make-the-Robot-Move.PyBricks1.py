#!/usr/bin/env pybricks-micropython


from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Button, SoundFile
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# The Left, Right, Up, and Down Buttons are used to command the robot.
COMMAND_BUTTONS = (Button.LEFT, Button.RIGHT, Button.UP, Button.DOWN)

# Configure 2 motors with default settings on Ports B and C.  These
# will be the left and right motors of the Driving Base.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# The wheel diameter of the Robot Educator Driving Base is 56 mm.
wheel_diameter = 56

# The axle track is the distance between the centers of each of the
# wheels.  This is 118 mm for the Robot Educator Driving Base.
axle_track = 118

# The Driving Base is comprised of 2 motors.  There is a wheel on each
# motor.  The wheel diameter and axle track values are used to make the
# motors move at the correct speed when you give a drive command.
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Wait until one of the command buttons is pressed.
while not any(b in brick.buttons() for b in COMMAND_BUTTONS):
    wait(10)

# Store the pressed button as the drive command.
drive_command = brick.buttons()[0]
brick.sound.file(SoundFile.CLICK)

# Wait 2 seconds and then play a sound to indicate that the robot is
# about to drive.
wait(2000)
brick.sound.file(SoundFile.GO)
wait(1000)

# Now drive the robot using the drive command.  Depending on which
# button was pressed, drive in a different way.

# The robot turns 90 degrees to the left.
if drive_command == Button.LEFT:
    robot.drive_time(100, -90, 1000)

# The robot turns 90 degrees to the right.
elif drive_command == Button.RIGHT:
    robot.drive_time(100, 90, 1000)

# The robot drives straight forward 30 cm.
elif drive_command == Button.UP:
    robot.drive_time(100, 0, 3000)

# The robot drives straight backward 30 cm.
elif drive_command == Button.DOWN:
    robot.drive_time(-100, 0, 3000)

# Play a sound to indicate that it is finished.
brick.sound.file(SoundFile.GAME_OVER)
wait(2000)
