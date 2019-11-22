from wpilib.command import Subsystem
from wpilib.solenoid import Solenoid
from commands.hatch.tilt import TiltHatchCommand
from rev import CANSparkMax, MotorType
import robotmap

class HatchSubsystem(Subsystem):
    def __init__(self):
        # Anything the subsystem has goes here
        super().__init__("HatchSubsystem")
        self.angleMotor = CANSparkMax(robotmap.CAN_REV_HATCH_ANGLE, MotorType.kBrushed)
        self.hatchLauncher = Solenoid(robotmap.HATCH_LAUNCHER_PCM_PORT)
        self.hatchLauncher.set(False)


    def initDefaultCommand(self):
        # This is where the command to do if nothing else happens goes
        self.setDefaultCommand(TiltHatchCommand())

    
    def tilt(self, speed):
        # This function lets the mechanism tilt
        self.angleMotor.set(robotmap.HATCH_ARM_SPEED_REDUCTION * speed)


    def releaseHatch(self):
        # This function extends the poker
        self.hatchLauncher.set(True)


    def retract(self):
        # This function retracts the poker
        self.hatchLauncher.set(False)