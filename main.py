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

import time
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
print(color_sensor.get_reflection())

# robot_controller.straight(-50)
# robot_controller.turn(360)


mid_val = 50
speed = 250

max_time = 15
delta = 10

# robot_controller.drive_base.settings(100,10,angle_speed,2)

start = time.time()

k_p = 0.8
tau = 0.1
k_i = 1.1
borne = 45
k_d = 0.001

sum_e = 0
e_t = 0
while(True):
    x_c = mid_val
    x_t = color_sensor.get_reflection()

    e_t_minus_1 = e_t  
    e_t = x_t - x_c
    print(e_t <= borne)
    sum_e += e_t

    # delta = k_p*e_t + k_i*tau*sum_e
    # delta = k_p*e_t + max(abs(k_i*tau*sum_e), borne)
    delta = k_p*e_t + k_i*tau*sum_e + k_d/tau*(e_t-e_t_minus_1)


    robot_controller.drive_base.drive(speed,delta)
    
    if time.time() - start > 15:
        break

    time.sleep(tau)

