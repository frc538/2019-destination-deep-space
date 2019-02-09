from wpilib.command import Command
import robotsubsystems

class ToggleRearCommand(Command):
  def __init__(self):
    super().__init__('ToggleRearCommmand')
    self.requires(robotsubsystems.lift)
  
  
  def initialize(self):
    pass
  
  
  def execute(self):
    robotsubsystems.lift.toggleRear()
    
    
  def isFinished(self):
    return True
  
  
  def end(self):
    pass
  
  
  def interrupted(self):
    self.end()
