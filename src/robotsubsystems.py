
from subsystems.drive import DriveSubsystem
from subsystems.cargo import CargoSubsystem
from subsystems.lift import LiftSubsystem
from subsystems.hatch import HatchSubsystem

drive = None
cargo = None
lift = None
hatch = None

def init():
  global drive
  global cargo
  global lift
  global hatch

  drive = DriveSubsystem()
  cargo = CargoSubsystem()
  lift = LiftSubsystem()
  hatch = HatchSubsystem()