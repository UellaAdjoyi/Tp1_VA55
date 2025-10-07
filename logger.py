#!/usr/bin/env pybricks-micropython
import time
import csv
from pybricks import DataLog


class Logger:
    def __init__(self, filename="robot_log.csv"):
        self data_log = DataLog('Time', 'Distance (mm)', 'Error', 'Delta', 'Mode')
        

    def log_pid(self, error, delta, distance):
        t = round(time.time(), 3)
        DataLog('Time', t)
        DataLog('Error', error)
        DataLog('Delta', delta)
        DataLog('Color', color)
        DataLog('Distance (mm)', distance)
        with open(self.filename, 'a') as file:
            file.write(f"{t},{distance},{error},{delta},PID\n")