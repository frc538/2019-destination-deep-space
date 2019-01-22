from wpilib.xboxcontroller import XboxController
from robotcode import robotmap

driverOne = None
driverTwo = None

def init():
  global driverOne
  global driverTwo
  driverOne = XboxController(robotmap.USB_PORT_DRIVER_ONE)
  driverTwo = XboxController(robotmap.USB_PORT_DRIVER_TWO)