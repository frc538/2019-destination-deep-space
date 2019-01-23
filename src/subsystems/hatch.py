from wpilib.command import Subsystem
from ctre.wpi_victorspx import WPI_VictorSPX
from wpilib.doublesolenoid import DoubleSolenoid
from wpilib.digitalinput import DigitalInput
import robotmap

class HatchSubsystem(Subsystem):
    def __init__(self):
        # Anything the subsystem has goes here
        self.angleMotor = WPI_VictorSPX(robotmap.CAN_VICTOR_HATCH_ANGLE)
        self.hatchLauncher = DoubleSolenoid(robotmap.HATCH_LAUNCHER_OPEN_PCM_PORT, robotmap.HATCH_LAUNCHER_CLOSE_PCM_PORT)
        self.hatchLauncher.set(DoubleSolenoid.Value.kReverse)
        self.maxUpSwitch = DigitalInput(robotmap.DIO_PORT_HATCH_MAX_UP)
        self.minDownSwitch = DigitalInput(robotmap.DIO_PORT_HATCH_MIN_DOWN)

    
    def initDefaultCommand(self):
        # This is where the command to do if nothing else happens goes
        pass

    
    def tilt(self, speed):
        # This function lets the mechanism tilt
        if speed > 0 and self.maxUpSwitch.get():
            self.angleMotor.set(0)
        elif speed < 0 and self.minDownSwitch.get():
            self.angleMotor.set(0)
        else:
            self.angleMotor.set(speed)


        self.angleMotor.set(speed)


    def toggleLauncher(self):
        # This function extends/retracts the poker
        if self.hatchLauncher.get() is DoubleSolenoid.Value.kForward:
            self.hatchLauncher.set(DoubleSolenoid.Value.kReverse)
        else:
            self.hatchLauncher.set(DoubleSolenoid.Value.kForward)