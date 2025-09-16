#!/usr/bin/env pybricks-micropython
from  pybricks.hubs import EV3Brick
from  pybricks.ev3devices import ColorSensor as color
from pybricks.parameters import Port

class ColorSensor:
    def __init__(self):
        self.color_sensor = color(Port.S3)

    def get_color(self):
        return self.color_sensor.color()