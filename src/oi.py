from wpilib.xboxcontroller import XboxController
from wpilib.buttons import JoystickButton
from commands.hatch.launchhatch import LaunchHatchCommand
from commands.hatch.retract import RetractCommand
import robotmap

driverOne = None
driverTwo = None

def init():
  global driverOne
  global driverTwo
  driverOne = XboxController(robotmap.USB_PORT_DRIVER_ONE)
  driverTwo = XboxController(robotmap.USB_PORT_DRIVER_TWO)

  toggleLauncher = JoystickButton(driverTwo, robotmap.BUTTON_A)
  toggleLauncher.whenPressed(LaunchHatchCommand())
  toggleLauncher.whenReleased(RetractCommand())
    