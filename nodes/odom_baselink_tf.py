#!/usr/bin/env python
import roslib
import rospy
import tf
from nav_msgs.msg import Odometry

# Transform from /odom to /base_link

def poseCallback(msg):

    odomBroadcaster = tf.TransformBroadcaster()

    o = Odometry()
    position = (msg.pose.pose.position.x / 1000.0,
                msg.pose.pose.position.y / 1000.0,
                msg.pose.pose.position.z / 1000.0)
    orientation = ( msg.pose.pose.orientation.x,
                    msg.pose.pose.orientation.y,
                    msg.pose.pose.orientation.z,
                    msg.pose.pose.orientation.w)

    odomBroadcaster.sendTransform(  position, 
                                    orientation, 
                                    rospy.Time.now(), 
                                    "/base_link",
                                    "/odom")

if __name__ == '__main__':

    rospy.init_node('odom_baselink_tf')

    rate = rospy.Rate(20.0)

    rospy.Subscriber('/pose', Odometry, poseCallback)

    rospy.spin()
