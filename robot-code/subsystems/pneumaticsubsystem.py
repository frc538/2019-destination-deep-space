from wpilib.command import Subsystem

class PneumaticSubsystem(Subsystem):

  def __init__(self):
    super().__init__("PneumaticSubsystem")
    # Create pieces of the subsystem in this function
    
  
  def initDefaultCommand(self):
    # Create the default command
    self.setDefaultCommand(None)

  # Create any other functions here.
  # For example, a drive train subsystem would need a method for how to drive.
