#!/usr/bin/env pybricks-micropython
from  pybricks.hubs import EV3Brick
from  pybricks.ev3devices import Motor
from pybricks.parameters import Port


class RobotController:
    
    def __init__(self):
        print("lezgo")
        self.left_motor=Motor(Port.B)
        self.right_motor=Motor(Port.C)
        # moteur.run_target(500,90)
    
    def forward(self,speed):
        self.left_motor.run(speed)
        self.right_motor.run(speed)
    
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        
    def rotate(self,angle,aSpeed):
        if(angle>0):
            self.left_motor.run_angle(aSpeed,angle)
        else:
            self.right_motor.run_angle(aSpeed,-angle)
        
    
    
