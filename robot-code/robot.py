from wpilib import TimedRobot
from wpilib import run
from wpilib.command import Scheduler

class Robot(TimedRobot):
  """
  Command-based robots inherit from the TimedRobot class.
  """
  
  def robotInit(self):
    """
    This function is run when the robot is first started up and should be 
    used for any initialization code.
    """
    
  
  def robotPeriodic(self):
    """
    This function is called every robot packet, no matter the mode. Use
    this for items like diagnostics that you want ran during disabled,
    autonomous, teleoperated and test.
   
    This runs after the mode specific periodic functions, but before
    LiveWindow and SmartDashboard integrated updating.
    """
    pass

  
  def disabledInit(self):
    """
    This function is called once each time the robot enters Disabled mode.
    You can use it to reset any subsystem information you want to clear when 
    the robot is disabled.
    """
    pass


  def disabledPeriodic(self):
    """
    This function is repeatedly while the robot is in Disabled mode. 
    You generally will not need to alter this method.
    """
    Scheduler.getInstance().run()


  def autonomousInit(self):
    """
    This method is called once at the start of autonomous.
    Put anything in this method that needs to happen when autonomous starts.
    """
    pass


  def autonomousPeriodic(self):
    """
    This function is called periodically during autonomous.
    You generally will not need to alter this method.
    """
    Scheduler.getInstance().run()


  def teleopInit(self):
    """
    This method is called once at the start of teleop.
    Put anything in this method that needs to happen when teleop starts.
    """
    pass


  def teleopPeriodic(self):
    """
    This function is called periodically during teleop.
    You generally will not need to alter this method.
    """
    Scheduler.getInstance().run()


  def testPeriodic(self):
    """
    This method is not called during competition.
    You can put test code in here that is tested from driver station.
    """
    pass

   

if __name__ == "__main__":
    run(Robot)
