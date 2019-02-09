from wpilib.command import Subsystem
from ctre.wpi_victorspx import WPI_VictorSPX
import robotmap


class CargoSubsystem(Subsystem):
    def __init__(self):
        super().__init__('CargoSubsystem')
        self.bandSpinner = WPI_VictorSPX(robotmap.CAN_ID_VICTOR_BAND_SPINNER)
        

    def spin(self):
        self.bandSpinner.set(1)


    def reset(self):
        self.stop()


    def stop(self):
        self.bandSpinner.set(0)