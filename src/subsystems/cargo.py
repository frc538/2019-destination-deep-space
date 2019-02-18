from wpilib.command import Subsystem
from commands.cargo.spin import SpinCommand
from ctre.wpi_victorspx import WPI_VictorSPX
import robotmap


class CargoSubsystem(Subsystem):
    def __init__(self):
        super().__init__('CargoSubsystem')
        self.bandSpinner = WPI_VictorSPX(robotmap.CAN_ID_VICTOR_BAND_SPINNER)
        
    def initDefaultCommand(self):
        # This is where the command to do if nothing else happens goes
        self.setDefaultCommand(SpinCommand())
        

    def spin(self, speed):
        self.bandSpinner.set(speed)


    def reset(self):
        pass


    def stop(self):
        pass
