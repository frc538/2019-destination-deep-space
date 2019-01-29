from wpilib.command import Command
import robotsubsystems

class SpinCommand(Command):
    def __init__(self):
        super().__init__('SpinCommand')
        self.requires(robotsubsystems.cargo)


    def initialize(self):
        pass

    
    def execute(self):
        robotsubsystems.cargo.spin()


    def isFinished(self):
        return True


    def end(self):
        pass

    def interrupted(self):
        self.end()
