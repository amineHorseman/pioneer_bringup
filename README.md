Pionner_bringup
===============

A ROS package providing roslaunch scripts for starting the Adept MobileRobots Pioneer and Pioneer-compatible robots (Including Pioneer 2, Pioneer 3, Pioneer LX, AmigoBot, PeopleBot, PatrolBot, PowerBot, Seekur and Seekur Jr.)

Note: This package have not yet been tested on ROS Kinetic Kame

# Installation

### 1. Dependencies

Enter in your catkin workspace directory

	$ cd ~/catkin_ws/src


Get RosAria stack that allows to communicate with Pioneer robots hardware

	$ git clone https://github.com/amor-ros-pkg/rosaria.git (master branch)
	$ source ~/catkin_ws/devel/setup.bash
	$ rosdep install rosaria

Get and Install LMS1xx Package that allows to communicate with Sick LMS1xx Laser Range Finders

- For ROS Kinetic Kame:
	$ sudo apt-get install ros-kinetic-lms1xx

- For ROS Jade:
	$ sudo apt-get install ros-jade-lms1xx
	
- For ROS Indigo:
	$ sudo apt-get install ros-indigo-lms1xx

- For ROS Hydro:
	$ sudo apt-get install ros-hydro-lms1xx


Get and Install usb_cam Package that allows to communicate with usb cameras and webcams

- For ROS Jade:
	$ sudo apt-get install ros-jade-usb-cam
	
- For ROS Indigo:
	$ sudo apt-get install ros-indigo-usb-cam

- For ROS Hydro:
	$ sudo apt-get install ros-hydro-usb-cam


Get pioneer_bringup package that allows to launch base functionalities of Pioneer robots

	$ git clone https://github.com/amineHorseman/pioneer_bringup.git

## 2. Build the catkin workspace

	$ cd ~/catkin_ws
	$ catkin_make


# Usage

There actually 3 bringup modes: 

### 1. Minimal mode

Starts up the robot with a single master ROS environment and ROSARIA:

		$ roslaunch pioneer_bringup minimal.launch

### 2. Camera mode

Can do everything minimal mode does, but also launches the usb cam node

		$ roslaunch pioneer_bringup camera.launch

### 3. Laser mode

Can do everything minimal mode does, but also launches the Sick LMS1xx laser node:

		$ roslaunch pioneer_bringup laser_lms1xx.launch

If you want to bringup both the laser and camera together use the following command:

		$ roslaunch pionner_bringup laser_lms1xx.launch _camera:=1

# Known issues

### Use USB port in RosAria instead of Serial

All the bringup modes call first RosAria package which is responsible to link ROS with the robot hardware.

Generally, the pioneer robots come with an onboard computer which communicate with the hardware throught Serial port, that's why, in the minimal.launch file we specify the port value as "/dev/ttyS0" (default value).

Sometimes however, RosAria need to communicate throught USB port, and then, you need to replace the followin line in the minimal.launch file:

	$ <param name="port" value="/dev/ttyS0" />

with this one:

	$ <param name="port" value="/dev/ttyUSB0" />

For more information about this modification, please refer to [RosAria documentation](http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA):
	
### Other issues

Please report any problem in the [issues panel](https://github.com/amineHorseman/pioneer_bringup/issues)

# TODO

Feel free to contribute to this repository:
- Test the package on ROS Kinetic Kame
- Add argument to choose between Serial and USB port
- Add Hokuyo Laser bringup mode
- Add Rviz launcher?
