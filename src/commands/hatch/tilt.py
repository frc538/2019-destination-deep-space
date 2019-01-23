from wpilib.command import Command
import robotsubsystems
import robotmap
import oi

class TiltHatchCommand(Command):
    def __init__(self):
        super().__init__("TitleHatchCommand")
        self.requires(robotsubsystems.hatch)
  
  
    def initialize(self):
        pass


    def execute(self):
        robotsubsystems.hatch.tilt(-oi.driverTwo.getRawAxis(robotmap.AXIS_LEFT_Y))


    def isFinished(self):
        return False


    def end(self):
        robotsubsystems.hatch.tilt(0)


    def interrupted(self):
        self.end()