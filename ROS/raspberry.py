#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64


def move_servo_1(angle):
    pub = rospy.Publisher("servo_1", Float64, queue_size=10)
    pub.publish(angle)


def move_servo_2(angle):
    pub = rospy.Publisher("servo_2", Float64, queue_size=10)
    pub.publish(angle)


if __name__ == "__main__":
    rospy.init_node("raspberry_pi_controller")
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        # Call the function to move the servos to desired angles
        move_servo_1(120)
        move_servo_2(60)
        rate.sleep()
