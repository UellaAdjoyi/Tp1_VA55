#!/usr/bin/env pybricks-micropython
from  pybricks.hubs import EV3Brick
from  pybricks.ev3devices import ColorSensor as color
from pybricks.parameters import Port
from ColorSensor import ColorSensor
from DistanceSensor import DistanceSensor

class RobotState:
    def __init__(self):
        self.color_sensor = ColorSensor()
        self.distance_sensor = DistanceSensor()
        self.current_color = None
        self.current_distance = None
        self.update_state()
    
    def update_state(self):
        self.current_color = self.color_sensor.get_color()
        self.current_distance = self.distance_sensor.get_distance()
        return self.current_color, self.current_distance
    
    