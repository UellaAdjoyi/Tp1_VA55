#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import sys
from RobotController import RobotController
from DistanceSensor import DistanceSensor
from ColorSensor import ColorSensor
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
# Write your program here.
#ev3.speaker.beep()

# print(sys.version)
# wait(5000)
robot_controller = RobotController()
# robot_controller.forward(100)
# wait(5000)
# robot_controller.stop()
# robot_controller.rotate(-180,1000)
# wait(5000)
# distance_sensor = DistanceSensor()
# print(distance_sensor.get_distance())
color_sensor = ColorSensor()
print(color_sensor.get_color())
