#!/usr/bin/env pybricks-micropython
from  pybricks.hubs import EV3Brick
from  pybricks.ev3devices import ColorSensor as color
from pybricks.parameters import Port

class DisplayLcd:
    def __init__(self):
        self.ev3 = EV3Brick()

    def display_text(self, text, x=0, y=0):
        self.ev3.screen.clear()
        self.ev3.screen.draw_text(x, y, text)

    def clear_screen(self):
        self.ev3.screen.clear()