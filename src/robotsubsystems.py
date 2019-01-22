from subsystems.lift import LiftSubsystem

lift = None

def init():
  global lift
  lift = LiftSubsystem()
