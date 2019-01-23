from wpilib.command import Command
import robotsubsystems

class ToggleLauncherCommand(Command):
  def __init__(self):
    super().__init__('ToggleLauncherCommand')
    self.requires(robotsubsystems.hatch)
  
  
  def initialize(self):
    pass
  
  
  def execute(self):
    robotsubsystems.hatch.toggleLauncher()
  
  
  def isFinished(self):
    return True
  
  
  def end(self):
    pass
  
  
  def interrupted(self):
    self.end()
