from wpilib.xboxcontroller import XboxController
from wpilib.buttons import JoystickButton
from commands.cargo.spin import SpinCommand
from commands.cargo.reset import ResetCommand
from commands.hatch.retract import RetractCommand
from commands.hatch.launchhatch import LaunchHatchCommand
from commands.lift.togglefront import ToggleFrontCommand
from commands.lift.togglerear import ToggleRearCommand
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

  toggleFront = JoystickButton(driverTwo, robotmap.BUTTON_RIGHT_BUMPER)
  toggleFront.whenReleased(ToggleFrontCommand())

  toggleRear = JoystickButton(driverTwo, robotmap.BUTTON_LEFT_BUMPER)
  toggleRear.whenReleased(ToggleRearCommand())    
  
  cargoButton = JoystickButton(driverOne, robotmap.BUTTON_A)
  cargoButton.whileHeld(SpinCommand())
  cargoButton.whenReleased(ResetCommand())
