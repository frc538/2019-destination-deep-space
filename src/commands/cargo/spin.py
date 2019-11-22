from wpilib.command import Command
import robotsubsystems
import robotmap
import oi

class SpinCommand(Command):
    def __init__(self):
        super().__init__('SpinCommand')
        self.requires(robotsubsystems.cargo)


    def initialize(self):
        pass

    
    def execute(self):
        robotsubsystems.cargo.spin(oi.driverTwo.getRawButton(robotmap.BUTTON_Y))


    def isFinished(self):
        return True


    def end(self):
        pass

    def interrupted(self):
        self.end()
