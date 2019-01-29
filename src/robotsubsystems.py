from subsystems.hatch import HatchSubsystem

hatch = None

def init():
  global hatch
  hatch = HatchSubsystem()
