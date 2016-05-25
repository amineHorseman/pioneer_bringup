Pionner_bringup
===============

A ROS package providing roslaunch scripts for starting the Adept MobileRobots Pioneer and Pioneer-compatible robots (Including Pioneer 2, Pioneer 3, Pioneer LX, AmigoBot, PeopleBot, PatrolBot, PowerBot, Seekur and Seekur Jr.)

Note: This package have not yet been tested on ROS Kinetic Kame

# Installation

## Get the source

	Enter in your catkin workspace directory

	$ cd ~/catkin_ws/src


Get RosAria stack that allows to communicate with Pioneer robots hardware

	$ git clone https://github.com/amor-ros-pkg/rosaria.git (master branch)
	$ source ~/catkin_ws/devel/setup.bash
	$ rosdep install rosaria

**Important: actually we get an error message while trying to install rosaria in Ubuntu 16.04, that's because rosdep try to locate the binaries for this OS version (which was not released yet)**

Get and Install LMS1xx Package that allows to communicate with Sick LMS1xx Laser Range Finders

	For ROS Kinetic Kame:
	$ sudo apt-get install ros-kinetic-lms1xx

	For ROS Jade:
	$ sudo apt-get install ros-jade-lms1xx
	
	For ROS Indigo:
	$ sudo apt-get install ros-indigo-lms1xx

	For ROS Hydro:
	$ sudo apt-get install ros-hydro-lms1xx


Get and Install usb_cam Package that allows to communicate with usb cameras and webcams

	For ROS Jade:
	$ sudo apt-get install ros-jade-usb-cam
	
	For ROS Indigo:
	$ sudo apt-get install ros-indigo-usb-cam

	For ROS Hydro:
	$ sudo apt-get install ros-hydro-usb-cam


Get pioneer_bringup package that allows to launch base functionalities of Pioneer robots

	$ git clone https://github.com/amineHorseman/pioneer_bringup.git

## Build the catkin packages from source

	$ cd ~/catkin_ws
	$ catkin_make


# Usage

##Bringup Modes

	In this package, there are three different ways of bringing up pioneer robots: 

	- Minimal : this starts up the robot with single master ROS environment and ROSARIA.

		$ roslaunch pioneer_bringup minimal.launch

	- Laser1xx : can do everything minimal does, but also launches the Sick LMS1xx laser node

		$ roslaunch pioneer_bringup laser_lms1xx.launch

	- Camera : can do everything minimal does, but also launches the usb cam node

		$ roslaunch pioneer_bringup camera.launch

		Note: is you want to bringup both the laser and camera together use the following command:

		$ roslaunch pionner_bringup laser_lms1xx.launch _camera:=1


##Some issues about port configuration

	All the bringup modes call first RosAria package which is responsible to link ROS with the robot hardware.
	Generally, the pioneer robots come with an onboard computer which communicate with the hardware throught Serial port, that's why, in the minimal.launch file we specify the port value as "/dev/ttyS0" (default value).
	Sometimes however, RosAria need to communicate throught USB port, and then, you need to replace the minimal.launch file

	$ <param name="port" value="/dev/ttyS0" />

	by this one:

	$ <param name="port" value="/dev/ttyUSB0" />

	For more information about this modification, please refer to [RosAria documentation](http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA):
	
## Other issues

Feel Free to contribute to this repository, or to report the bugs in the [issues panel](https://github.com/amineHorseman/pioneer_bringup/issues)
