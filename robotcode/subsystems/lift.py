from wpilib.command import Subsystem
from wpilib.solenoid import Solenoid
from robotcode import robotmap

class LiftSubsystem(Subsystem):
    def __init__(self):
        super().__init__('LiftSubsystem')
        self.frontLift = Solenoid(robotmap.FRONT_LIFT_SOLENOID_PCM_PORT)
        self.rearLift = Solenoid(robotmap.BACK_LIFT_SOLENOID_PCM_PORT)

    
    def toggleFront(self):
        self.frontLift.set(not self.frontLift.get())
    