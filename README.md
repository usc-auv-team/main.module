# USC AUV Main Module
the USC AUV team's logic for path following and task execution; can run in Python 2 or 3
  
build/install instructions:  
1) Make sure you're in the root directory (the one with setup.py)  
2) python3 setup.py sdist bdist_wheel  
3) cd dist
4) pip3 install main_module-0.0.1-py3-none-any.whl  
  
You can also download the wheel here: https://drive.google.com/open?id=1oR2eWiqXUZFfTDjLt5Ceivy69kb98u4P  
  
  
  
primary code outline:  
_gyro_  
**_abstract:** requirements of a gyro class  
**ros_gyro:** an implementation with callback methods for use with ROS  
**simulation:** an implementation that requires no external inputs and allows for quick debugging  
  
_odometer_  
**_abstract:** definition and explanation of what a gyro class does  
**disconnected:** an implementation that yields no data (if we need to "fly blind")  
**ros_odometer:** an implementation with callback methods for use with ROS  
**simulation:** an implementation that requires no external inputs and allows for quick debugging  
  
_paths_  
**_abstract:** requirements for creating Leash-compatible lines and curves  
**cubic_spline:** an implementation allowing us to swim along cubic splines  
**curve:** an implementation allowing us to swim along a curve defined by a parametric equation  
**point_list:** an implementation allowing us to swim from point to point in a list  
  
    
_planning_  
**events:** logic for executing arbitrary commands at specified points on a path  
**leash:** logic for autonomously following paths with propulsion  
**strategy:** abstract class for combining and following a set of events and a leash  
_s2018_  
**coach:** a class that lists possible strategies and initializes whichever one gets chosen  
**test:** contains 2 strategy implementations for debugging purposes  
  
_propulsion_  
**_abstract:** requirements for creating an autonomous-capable propulsion class  
**robot2018:** an implementation to be used with ROS this year  
**simulation:** an implementation that requires no external inputs and allows for quick debugging  
  
_subsystems_  
**_abstract:** requirements for creating an autonomous-capable subsystem  
  

  
Please contact hshively@usc.edu if you have questions.  
