#!/usr/bin/env pybricks-micropython
import time
import csv
from pybricks.tools import DataLog


class Logger:
    def __init__(self, filename="robot_log.csv"):
        self.filename = filename
        # with open(self.filename, 'w') as file:
        #     file.write("Timestamp,Color,Distance (mm),State\n")
        self.data_log = DataLog("time", "error","delta", "speed", name=filename, timestamp=True, extension='csv', append=False)

    def log(self, time, error, delta, speed):
        
        self.data_log.log(time, error, delta, speed)