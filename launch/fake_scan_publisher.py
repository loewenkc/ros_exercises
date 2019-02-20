#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32 
import numpy
from sensor_msgs.msg import LaserScan
from math import pi

def scanner():
    rospy.init_node('fake_scan_publisher')
    scan = LaserScan()
    fp = rospy.get_param('/fpubt','fake_scan')
    pub = rospy.Publisher(fp,LaserScan,queue_size=10)
    scan.header.frame_id="base_link"
    scan.header.stamp=rospy.Time.now()
    ra = rospy.get_param('/r')
    rate = rospy.Rate(ra)
    while not rospy.is_shutdown():
        scan.angle_min = rospy.get_param('angle_min')
        scan.angle_max = rospy.get_param('angle_max')
        scan.angle_increment = rospy.get_param('angle_increment')
        scan.scan_time = 0.05 
        scan.range_min = rospy.get_param('range_min')
        scan.range_max = rospy.get_param('range_max')
        scan.ranges = numpy.random.uniform(scan.range_min,scan.range_max,400)
        pub.publish(scan)
        rospy.loginfo(scan)
        rospy.sleep

if __name__=='__main__':
    try:
        scanner()
    except rospy.ROSInterruptException:
        pass
