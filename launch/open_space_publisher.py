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
    angle = data.ranges[ind]*(1.0/300.0)*pi-(2.0/3.0*pi)
#topic was 'open_space/distance'
#topic was 'open_space/angle'
    odi = rospy.get_param('/odis','open_space/distance')
    pub1 = rospy.Publisher(odi,Float32,queue_size=10)
    pub1.publish(dist)
    oan = rospy.get_param('/oang','open_space/angle')
    pub2 = rospy.Publisher(oan,Float32,queue_size=10)
    pub2.publish(angle)

def subby():
    rospy.init_node('open_space_publisher', anonymous=True)
    #sub = rospy.Subscriber('fake_scan',LaserScan,callback)
    opensub = rospy.get_param('/opensubt')
    sub = rospy.Subscriber(opensub,LaserScan,callback)
    rospy.spin()

if __name__=='__main__':
    try:
        subby()
    except rospy.ROSInterruptException:
        pass

