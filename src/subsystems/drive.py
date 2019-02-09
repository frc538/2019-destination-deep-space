from wpilib.command import Subsystem
from ctre.wpi_victorspx import WPI_VictorSPX
from wpilib.drive import MecanumDrive
from commands.drive.mecanumdrive import MecanumDriveCommand
import robotmap

class DriveSubsystem(Subsystem):
    def __init__(self):
        super().__init__('DriveSubsystem')
        self.frontRight = WPI_VictorSPX(robotmap.CAN_ID_VICTOR_FRONT_RIGHT)
        self.rearRight = WPI_VictorSPX(robotmap.CAN_ID_VICTOR_REAR_RIGHT)        
        self.frontLeft = WPI_VictorSPX(robotmap.CAN_ID_VICTOR_FRONT_LEFT)
        self.rearLeft = WPI_VictorSPX(robotmap.CAN_ID_VICTOR_REAR_LEFT)

        self.mecanum = MecanumDrive(self.frontLeft, self.rearLeft, self.frontRight, self.rearRight)


    def initDefaultCommand(self):
        self.setDefaultCommand(MecanumDriveCommand())


    def drive(self, robotRightSpeed, robotForwardSpeed, robotClockwiseSpeed):
        self.mecanum.driveCartesian(robotRightSpeed, robotForwardSpeed, robotClockwiseSpeed)
