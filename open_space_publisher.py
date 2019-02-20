#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
import math
import numpy
from math import pi

def callback(data):
    ind = numpy.argmax(data.ranges)
    dist = data.ranges[ind]
    angle = data.ranges[ind]*(1.0/300.0)*pi-(2.0/3.0*pi) #get angles from range? or only ang
    print(angle)
    #rospy.loginfo(dist)
    #rospy.loginfo(angle)
    pub1 = rospy.Publisher('open_space/distance',Float32,queue_size=10)
    pub1.publish(dist)
    pub2 = rospy.Publisher('open_space/angle',Float32,queue_size=10)
    pub2.publish(angle)

def subby():
    rospy.init_node('open_space_publisher', anonymous=True)
    sub = rospy.Subscriber('fake_scan',LaserScan,callback)
    rospy.spin()

if __name__=='__main__':
    try:
        subby()
    except rospy.ROSInterruptException:
        pass

