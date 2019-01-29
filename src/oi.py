from wpilib.xboxcontroller import XboxController
import robotmap

driverOne = None

def init():
  global driverOne
  driverOne = XboxController(robotmap.USB_PORT_DRIVER_ONE)
    