from wpilib.xboxcontroller import XboxController
from wpilib.buttons import JoystickButton
from commands.cargo.spin import SpinCommand
from commands.cargo.reset import ResetCommand
import robotmap

driverOne = None

def init():
  global driverOne
  driverOne = XboxController(robotmap.USB_PORT_DRIVER_ONE)
  
  cargoButton = JoystickButton(driverOne, robotmap.BUTTON_A)
  cargoButton.whileHeld(SpinCommand())
  cargoButton.whenReleased(ResetCommand())