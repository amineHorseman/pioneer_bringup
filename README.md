Pionner_bringup
===============

A ROS package providing roslaunch functionalities for starting the Adept MobileRobots Pioneer and Pioneer-compatible robots (Including Pioneer 2, Pioneer 3, Pioneer LX, AmigoBot, PeopleBot, PatrolBot, PowerBot, Seekur and Seekur Jr.)

Compatible with RosAria and P2OS hardware controllers.

# Installation

Depending on you needs, you may need to install some of these dependencies:
- ROSARIA
- P2OS
- Urg_node: for using Hokuyo lidars
- LMS1XX: for using Sick LMS100 lidar
- Sicktoolbox_wrapper: for using Sick LMS2xx lidar
- Sick_scan: for using other Sick lidars (see list bellow)
- Usbcam: for using usb cameras and webcams
- Freenect: for using Kinect
- Pionner_dashboard: for GUI dashboard window

# Usage

For starting the robot using the default parameters:

	$ roslaunch pioneer_bringup pioneer_bringup.launch

You can activate more features by using these arguments:

| Argument        | Possible values                                                                                                                       | Default    | Description                                                                 |
|-----------------|------------------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------------|
| controller      | rosaria, p2os                                                                                                                | rosaria    | Hardware driver controller                                                  |
| controller_port | /dev/ttySx or /dev/ttyUSBx                                                                                                   | /dev/ttyS0 | Serial port to communicate with the controller                              |
| sonar           | true, false                                                                                                                  | false      | Activate sonars                                                             |
| laser           | hokuyo, lms_1xx, lms_2xx, lms_1xxx, lms_4xxx, lms_5xx, mrs_1xxx, mrs_6xxx, rms_3xx, tim_5xx, tim_7xx, tim_7xxS | false      | Laser reference code or 'false' if no laser                                 |
| usbcam          | true, false                                                                                                                  | false      | launch usbcam node                                                          |
| kinect          | true, false                                                                                                                  | false      | launch kinect nodes                                                         |
| dashboard       | true, false                                                                                                                  | false      | launch a GUI window in rqt to visualize sensors readings and control motors |

**Example:**

	$ roslaunch pioneer_bringup pioneer_bringup.launch controller:=p2os laser:=lms_5xx usbcam:=true 

### More controls for Laser node:

You can use the following arguments to lidar parameters:

| Argument                | Possible values                     | Default           | Description                                                              |
|-------------------------|----------------------------|-------------------|--------------------------------------------------------------------------|
| laser_hostname          | IP Address                 | 192.168.0.1       | Laser IP address or hostname (if applicable)                             |
| laser_serial_port       | /dev/ttySx or /dev/ttyUSBx | /dev/ttyUSB0      | Laser Port (if applicable)                                               |
| laser_baselink_distance | x y z roll pitch yaw       | 0.13 0 0.39 0 0 0 | Distance between baselink and lidar in meters (for setting tf broadcast) |

**Example:**

	$ roslaunch pioneer_bringup pioneer_bringup.launch laser:=lms_1xx laser_hostname:=192.168.0.4 laser_baselink_distance:='0.20 0 0.3 0 0 0'

### More controls for Camera node:

You can use the following arguments to customize the camera parameters:

| Argument                | Values               | Default           | Description                                                              |
|-------------------------|----------------------|-------------------|--------------------------------------------------------------------------|
| camera_port             | /dev/videox (x = device number)         | /dev/video0       | USB Camera port                                                          |
| camera_display          | true, false          | true              | Display video feed on the screen (or stop it)                            |

**Other parameters:** You can customize more parameters in the config/camera.yaml file, such as: image_width, image_height, pixel_format, camera_frame_id and io_method.

**Example:**

	$ roslaunch pioneer_bringup pioneer_bringup.launch usbcam:=true camera_display:=false camera_port:=/dev/video2

### More controls for Kinect node:

You can use the following arguments to customize the kinect parameters:

| Argument         | Values    | Default | Description                               |
|------------------|-----------|---------|-------------------------------------------|
| kinect_data_skip | <number>  | 0       | Number of frames to skip from kinect data |
| kinect_id        | #<number> | #1      | kinect device number                      |


**Example:**

	$ roslaunch pioneer_bringup pioneer_bringup.launch kinect:=true kinect_data_skip:=5
	

# Known issues

### Cannot open /dev/ttyUSB0: Permission denied

This is a frequent issue when using an USB-Serial adapter to connect to the robot hardware or lidar.

Basically you just need to give the correct autorizations:

	sudo chmod 777 -R /dev/ttyUSB0

### Other issues

Please report any problem in the [issues section](https://github.com/amineHorseman/pioneer_bringup/issues)
