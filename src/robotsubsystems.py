from subsystems.drive import DriveSubsystem
from subsystems.cargo import CargoSubsystem
from subsystems.lift import LiftSubsystem

drive = None
cargo = None
lift = None

def init():
  global drive
  global cargo
  global lift

  drive = DriveSubsystem()
  cargo = CargoSubsystem()
  lift = LiftSubsystem()