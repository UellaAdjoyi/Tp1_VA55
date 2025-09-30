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
distance_sensor = DistanceSensor()
# print(distance_sensor.get_distance())
color_sensor = ColorSensor()

# --- Logging setup ---
# import logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s [%(levelname)s] %(message)s',
#     datefmt='%H:%M:%S'
# )

# --- Logging setup ---
# import logging
# import csv

# class CsvFormatter(logging.Formatter):
#     def __init__(self):
#         super().__init__()
#     def format(self, record):
#         # CSV: time,level,message
#         return f'{self.formatTime(record, "%H:%M:%S")},{record.levelname},{record.getMessage()}'

# csv_handler = logging.FileHandler('robot_logs.csv', mode='a')
# csv_handler.setFormatter(CsvFormatter())

# logging.basicConfig(
#     level=logging.INFO,
#     handlers=[csv_handler],
# )

# Log color sensor readings
# logging.info(f"Color detected: {color_sensor.get_color()}")
# logging.info(f"Reflection value: {color_sensor.get_reflection()}")

# robot_controller.straight(-50)
# robot_controller.turn(360)


mid_val = 40


max_time = 15
delta = 10

start = time.time()

k_p = 1.3
tau = 0.1
k_i = 1.75
borne = 45
k_d = 0.12

val_e = []
sum_e = 0
e_t = 0
while(True):

    speed = 220

    x_c = mid_val
    x_t = color_sensor.get_reflection()

    e_t_minus_1 = e_t  
    e_t = x_t - x_c
    # print(e_t <= borne)
    sum_e += e_t
    val_e.append(e_t)

    # delta = k_p*e_t + k_i*tau*sum_e
    # delta = k_p*e_t + max(abs(k_i*tau*sum_e), borne)
    # sum_e = sum(val_e)
    delta = k_p*e_t + k_i*tau*sum_e + k_d/tau*(e_t-e_t_minus_1)

    if distance_sensor.get_distance() < 50:
        delta = 0
        speed = 0
        sum_e = 0

    robot_controller.drive_base.drive(speed,delta)
    
    # if time.time() - start > 15:
    #     break

    if len(val_e) > 320:
        val_e.pop(0)

    time.sleep(tau)

