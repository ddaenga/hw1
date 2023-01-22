#! /usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from hw1.msg import circular_motion_turtlesim 

msg = circular_motion_turtlesim()

def main():
    # Node 생성
    rospy.init_node('input', anonymous=True)
    # Publisher 생성 
    pub = rospy.Publisher("/cmd_input",circular_motion_turtlesim, queue_size=10)
    # 1Hz의 속도로
    rate = rospy.Rate(1)
    
    # 종료전까지 반복
    while not rospy.is_shutdown():
        # Cmd 출력문
        print("\nPut Your Command\n")
        # msg에 input넣어주기
        msg.radius = input("Radius: ")
        msg.velocity = input("Velocity: ")
        msg.direction = input("Direction(CW or CCW): ")
        print("\nPublishing...\n")
        # publishing
        pub.publish(msg)
        rate.sleep()        


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass