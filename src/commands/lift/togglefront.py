from wpilib.command import Command
import robotsubsystems

class ToggleFrontCommand(Command):
  def __init__(self):
    super().__init__('ToggleFrontCommand')
    self.requires(robotsubsystems.lift)
  
  
  def initialize(self):
    pass
  
  
  def execute(self):
    robotsubsystems.lift.toggleFront()
  
  
  def isFinished(self):
    return True
  
  
  def end(self):
    pass
  
  
  def interrupted(self):
    self.end()
