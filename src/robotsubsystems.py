from subsystems.drive import DriveSubsystem

drive = None

def init():
  global drive
  drive = DriveSubsystem()