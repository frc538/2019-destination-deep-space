from wpilib.command import Command
import robotsubsystems
import math 
import oi
import robotmap

class MecanumDriveCommand(Command):
    def __init__(self):
        super().__init__('MecanumDriveCommand')
        self.requires(robotsubsystems.drive)
        

    def initialize(self):
        pass
        
    
    def execute(self):
        robotsubsystems.drive.drive(
            oi.driverOne.getRawAxis(robotmap.AXIS_LEFT_X), 
            -oi.driverOne.getRawAxis(robotmap.AXIS_LEFT_Y), 
            0)        
    

    def isFinished(self):
        return True
        
        
    def end(self):
        pass
        
        
    def interrupted(self):
        self.end()
