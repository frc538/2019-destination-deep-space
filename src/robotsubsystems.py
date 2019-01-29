from subsystems.drive import DriveSubsystem
from subsystems.cargo import CargoSubsystem

drive = None
cargo = None

def init():
  global drive
  global cargo
  drive = DriveSubsystem()
  cargo = CargoSubsystem()