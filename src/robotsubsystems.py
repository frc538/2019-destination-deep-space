from subsystems.lift import LiftSubsystem
from subsystems.hatch import HatchSubsystem

lift = None
hatch = None

def init():
  global lift
  lift = LiftSubsystem()

  global hatch
  hatch = HatchSubsystem()
