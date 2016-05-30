Pionner_bringup
===============

A ROS package providing roslaunch scripts for starting the Adept MobileRobots Pioneer and Pioneer-compatible robots (Including Pioneer 2, Pioneer 3, Pioneer LX, AmigoBot, PeopleBot, PatrolBot, PowerBot, Seekur and Seekur Jr.)

Note: This package have not yet been tested on ROS Kinetic Kame

# Installation

### 1. Dependencies

- RosAria:

RosAria is used to communicate with Pioneer robots hardware:

*or refer to the official [How to install RosAria tutorial](http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA)*

	$ cd ~/catkin_ws/src
	$ git clone https://github.com/amor-ros-pkg/rosaria.git
	$ source ~/catkin_ws/devel/setup.bash
	$ rosdep install rosaria

- LMS1XX or LMS200 [optional]:

Allow to communicate with Sick LMS1xx/LMS200 Laser Range Finders

	#replace <distro> by 'kinetic', 'jade', 'indigo' or 'hydro' according to your ROS version:
	$ sudo apt-get install ros-<ditro>-lms1xx

- Usb_cam  [optional]:

Allows to communicate with usb cameras and webcams

*this step can be skipped if you don't want to use usb camera, or if you want to invoke it yourself using another package*

	#replace <distro> by 'jade', 'indigo' or 'hydro' according to your ROS version:	
	$ sudo apt-get install ros-<distro>-usb-cam

For kinetic users: read *known issues* section

## 2. Get the source and build the workspace

	$ cd ~/catkin_ws/src
	$ git clone https://github.com/amineHorseman/pioneer_bringup.git
	$ cd ..
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

### ros-kinetic-usb-cam package doesn't exist

At the moment of writing this tutorial, usb_cam can be located by 'sudo apt-get install'

Instead try to install it from source:

	$ cd ~/catkin_ws/src
	$ git clone https://github.com/bosch-ros-pkg/usb_cam.git
	$ cd ..
	$ catkin_make
	
### Other issues

Please report any problem in the [issues panel](https://github.com/amineHorseman/pioneer_bringup/issues)

# TODO

Feel free to contribute to this repository:
- Test the package on ROS Kinetic Kame
- Add argument to choose between Serial and USB port
- Add Hokuyo Laser bringup mode
- Add Rviz launcher?
