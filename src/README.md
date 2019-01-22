# FRC Robot Code

To run robot code, you'll need the robotpy libraries (and any required third party libraries) installed.

The robot code is organized in the following manner.

- robot.py
  - Contains the main, top level robot code.
  - Includes very little of the robot's actual code.
- robotmap.py
  - Only contains constants.
  - Constant values that are accessible to avoid magic numbers.
  - Include things like button maps and CAN/PWM IDs here.
- robotsubsystems.py
  - Handles creating the subsystems that have been defined.
  - Gives commands and the robot access to the subsystems.
- oi.py
  - Handles creating the operator interface (OI).
  - Things like controllers, joysticks, and buttons go here.
- subsystems
  - Contains subsystem files.
  - Each file defines a subsystem of the robot.
- commands
  - Contains command files.
  - Each file defines a command.
