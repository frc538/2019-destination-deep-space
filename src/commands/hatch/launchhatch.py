from wpilib.command import Command
import robotsubsystems

class LaunchHatchCommand(Command):
  def __init__(self):
    super().__init__('LaunchHatchCommand')
    self.requires(robotsubsystems.hatch)
  
  
  def initialize(self):
    pass
  
  
  def execute(self):
    robotsubsystems.hatch.releaseHatch()
  
  
  def isFinished(self):
    return True
  
  
  def end(self):
    pass
  
  
  def interrupted(self):
    self.end()
