from wpilib.command import Command
import robotsubsystems

class RetractCommand(Command):
  def __init__(self):
    super().__init__('RetractCommand')
    self.requires(robotsubsystems.hatch)
  
  
  def initialize(self):
    pass
  
  
  def execute(self):
    robotsubsystems.hatch.retract()
  
  
  def isFinished(self):
    return True
  
  
  def end(self):
    pass
  
  
  def interrupted(self):
    self.end()
