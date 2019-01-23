from subsystems.lift import LiftSubsystem
from subsystems.drive import DriveSubsystem

lift = None
drive = None

def init():
  global lift
  lift = LiftSubsystem()
  
  global drive
  drive = DriveSubsystem()