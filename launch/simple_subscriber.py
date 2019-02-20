#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import math

def callback(data):
    rospy.loginfo(math.log(data.data))
    pub = rospy.Publisher('random_float_log',Float32,queue_size=10)

def alterer():
    rospy.init_node('simple_subscriber')
    sub = rospy.Subscriber('my_random_float',Float32,callback)
    rospy.spin()

if __name__=='__main__':
    alterer()



