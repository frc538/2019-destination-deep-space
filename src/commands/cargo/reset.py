from wpilib.command import Command
import robotsubsystems

class ResetCommand(Command):
    def __init__(self):
        super().__init__('ResetCommand')
        self.requires(robotsubsystems.cargo)


    def initialize(self):
        pass

    
    def execute(self):
        robotsubsystems.cargo.reset()


    def isFinished(self):
        return True


    def end(self):
        pass

    def interrupted(self):
        self.end()
