#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32 
import numpy
#from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import LaserScan
from math import pi
#hdr = Header(Timestamp=rospy.Time.now(), Frame_id='base_link')

def scanner():
    rospy.init_node('fake_scan_publisher')
    scan = LaserScan()
    pub = rospy.Publisher('fake_scan',LaserScan,queue_size=10)
    scan.header.frame_id="base_link"
    scan.header.stamp=rospy.Time.now()
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        scan.angle_min = (-2.0/3.0)*pi
        scan.angle_max = (2.0/3.0)*pi
        scan.angle_increment = (1.0/300.0)*pi 
        scan.scan_time = 0.05 
        scan.range_min = 1.0
        scan.range_max = 10.0
        #scan.ranges = numpy.linspace(1.0,10.0,400.0,endpoint=True)
        scan.ranges = numpy.random.uniform(scan.range_min,scan.range_max,400)
        pub.publish(scan)
        rospy.loginfo(scan)
        rospy.sleep

if __name__=='__main__':
    try:
        scanner()
    except rospy.ROSInterruptException:
        pass
