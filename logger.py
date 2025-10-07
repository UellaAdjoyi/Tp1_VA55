#!/usr/bin/env pybricks-micropython
import time
import csv


class Logger:

    def __init__(self, filename="robot_log.csv"):
        self.filename = filename
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Color", "Distance (mm)", "State"])

    def log(self, state):
        with open(self.filename, 'a', newline='') as file:
            file.write("{}, {}, {}, {}\n".format(
                time.time(), state.current_color, state.current_distance, state.state
            ))