from wpilib.command import Subsystem
from wpilib.solenoid import Solenoid
from wpilib.digitalinput import DigitalInput
from commands.hatch.tilt import TiltHatchCommand
from rev import CANSparkMax, MotorType
import robotmap

class HatchSubsystem(Subsystem):
    def __init__(self):
        # Anything the subsystem has goes here
        super().__init__("HatchSubsystem")
        self.angleMotor = CANSparkMax(robotmap.CAN_REV_HATCH_ANGLE, MotorType.kBrushless)
        self.maxUpSwitch = DigitalInput(robotmap.DIO_PORT_HATCH_MAX_UP)
        self.minDownSwitch = DigitalInput(robotmap.DIO_PORT_HATCH_MIN_DOWN)
        self.hatchLauncher = Solenoid(robotmap.HATCH_LAUNCHER_PCM_PORT)
        self.hatchLauncher.set(False)


    def initDefaultCommand(self):
        # This is where the command to do if nothing else happens goes
        self.setDefaultCommand(TiltHatchCommand())

    
    def tilt(self, speed):
        # This function lets the mechanism tilt
        if speed > 0 and self.maxUpSwitch.get():
            self.angleMotor.set(0)
        elif speed < 0 and self.minDownSwitch.get():
            self.angleMotor.set(0)
        else:
            self.angleMotor.set(speed)


    def releaseHatch(self):
        # This function extends the poker
        self.hatchLauncher.set(True)


    def retract(self):
        # This function retracts the poker
        self.hatchLauncher.set(False)