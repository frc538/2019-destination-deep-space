from wpilib.xboxcontroller import XboxController
from wpilib.buttons import JoystickButton
from robotcode.commands.lift.togglefront import ToggleFrontCommand
from robotcode.commands.lift.togglerear import ToggleRearCommand
from robotcode import robotmap

driverOne = None
driverTwo = None

def init():
  global driverOne
  global driverTwo
  driverOne = XboxController(robotmap.USB_PORT_DRIVER_ONE)
  driverTwo = XboxController(robotmap.USB_PORT_DRIVER_TWO)

  toggleFront = JoystickButton(driverTwo, robotmap.BUTTON_RIGHT_BUMPER)
  toggleFront.whenReleased(ToggleFrontCommand())

  toggleRear = JoystickButton(driverTwo, robotmap.BUTTON_LEFT_BUMPER)
  toggleRear.whenReleased(ToggleRearCommand())
    