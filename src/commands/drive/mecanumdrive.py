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
        speed = math.sqrt(oi.driverOne.getRawAxis(robotmap.AXIS_LEFT_X)**2 + oi.driverOne.getRawAxis(robotmap.AXIS_LEFT_Y)**2)
        robotsubsystems.drive.drive()        
    
    def isFinished(self):
        return True
        
        
    def end(self):
        robotsubsystems.drive.drive(0, 0, 0)
        
        
    def interrupted(self):
        self.end()
