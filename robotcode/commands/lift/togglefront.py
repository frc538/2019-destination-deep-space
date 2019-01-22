from wpilib.command import Command
from robotcode.robotsubsystems import lift

class ToggleFrontCommand(Command):
    def __init__(self):
        super().__init__('ToggleFrontCommand')
        self.requires(lift)


    def initialize(self):
        pass


    def execute(self):
        lift.toggleFront()

    
    def isFinished(self):
        return True


    def end(self):
        pass

    
    def interrupted(self):
        self.end()