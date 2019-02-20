#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from random import randint


#generate a random number

def numgen():
    rospy.init_node('simple_publisher')
    pub = rospy.Publisher('my_random_float',Float32, queue_size=10)
    rate = rospy.Rate(20) #20 Hz
    while not rospy.is_shutdown():
        rnd_gen=randint(1,10) #math domain error when have 0
	rospy.loginfo(rnd_gen)
        pub.publish(rnd_gen)
	rate.sleep()

if __name__=='__main__':
	try:
		numgen()
	except rospy.ROSInterruptException:
		pass
