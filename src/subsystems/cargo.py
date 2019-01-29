from wpilib.command import Subsystem
from ctre.wpi_victorspx import WPI_VictorSPX
from wpilib.digitalinput import DigitalInput
import robotmap


class CargoSubsystem(Subsystem):
    def __init__(self):
        super().__init__('CargoSubsystem')
        self.bandSpinner = WPI_VictorSPX(robotmap.CAN_ID_VICTOR_BAND_SPINNER)
        self.motorStopper = DigitalInput(robotmap.DIO_PORT_CARGO_MOTOR_STOPPER)
        self.canSpin = True


    def spin(self):
        if self.canSpin:
            self.bandSpinner.set(0.5)
        else:
            self.stop()

        if self.motorStopper.get():
            self.canSpin = False


    def reset(self):
        self.canSpin = True
        self.stop()


    def stop(self):
        self.bandSpinner.set(0)