from wpilib.command import Command
from robotcode.robotsubsystems import lift

class ToggleRearCommand(Command):
    def __init__(self):
        super().__init__('ToggleRearCommmand')
        self.requires(lift)

    
    def initialize(self):
        pass


    def execute(self):
        lift.toggleRear()


    def isFinished(self):
        return True


    def end(self):
        pass


    def interrupted(self):
        self.end()