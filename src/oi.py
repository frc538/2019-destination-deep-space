from wpilib.xboxcontroller import XboxController
from wpilib.buttons import JoystickButton
from commands.hatch.retract import RetractCommand
from commands.cargo.spin import SpinCommand
from commands.cargo.reset import ResetCommand
import robotmap

driverTwo = None

def init():
  global driverOne
  global driverTwo

  driverOne = XboxController(robotmap.USB_PORT_DRIVER_ONE)
  driverTwo = XboxController(robotmap.USB_PORT_DRIVER_TWO)

  toggleFront = JoystickButton(driverTwo, robotmap.BUTTON_RIGHT_BUMPER)

  toggleRear = JoystickButton(driverTwo, robotmap.BUTTON_LEFT_BUMPER)
  
  cargoButton = JoystickButton(driverOne, robotmap.BUTTON_A)
  cargoButton.whileHeld(SpinCommand())
  cargoButton.whenReleased(ResetCommand())
