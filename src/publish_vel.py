#! /usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
from hw1.msg import circular_motion_turtlesim

msg = Twist()

# subscriber로 받아오는 message를 callback
def callback(data): 
    # subscriber 로 받아온 velocity와 radius등을 Twist로 전환
    msg.linear.x = data.velocity
    msg.angular.z = data.velocity/data.radius
    if data.direction == "CW":
        msg.angular.z *= -1

def main():
    # Node 생성
    rospy.init_node('move', anonymous=True)
    # Publisher 생성
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    # Subscriber 생성
    sub = rospy.Subscriber('/cmd_input', circular_motion_turtlesim ,callback)
    # 1Hz의 속도로
    rate = rospy.Rate(1)

    # 종료 전까지 반복
    while not rospy.is_shutdown():
        # publishing
        pub.publish(msg)
        print(msg.linear.x)        
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass