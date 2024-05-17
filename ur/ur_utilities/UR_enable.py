#!/usr/bin/env python3

import rospy
import actionlib
from ur_dashboard_msgs.msg import SetModeAction, SetModeGoal, RobotMode
from std_srvs.srv import Trigger, TriggerRequest

class UR_enable():
    
    
    def __init__(self):
        self.ur_hardware_interface_topic = rospy.get_param('~ur_hardware_interface_topic', 'mur620a/UR10_l/ur_hardware_interface')

    def main(self):
        rospy.init_node('UR_enable')
        # first stop the dashboard server
        rospy.loginfo("Stopping dashboard server")
        trigger_client = rospy.ServiceProxy(self.ur_hardware_interface_topic + '/dashboard/stop', Trigger)
        rospy.loginfo("Waiting for dashboard server to start")
        trigger_client.wait_for_service()
        rospy.loginfo("Dashboard server started")
        trigger_request = TriggerRequest()
        trigger_client(trigger_request)


        # initialize action server to enable the robot
        client = actionlib.SimpleActionClient(self.ur_hardware_interface_topic + "/set_mode", SetModeAction)
        client.wait_for_server()
        
        set_mode_goal = SetModeGoal()
        robot_mode = RobotMode()
        robot_mode.mode = 7

        set_mode_goal.target_robot_mode = robot_mode
        set_mode_goal.play_program = True        
        client.send_goal(set_mode_goal)
        
        # wait for the action server to finish
        client.wait_for_result()
        rospy.loginfo("Robot enabled")

        # shutdown the node
        rospy.signal_shutdown("Robot enabled")
    
if __name__ == '__main__':
    rospy.init_node('UR_enable')
    UR_enable = UR_enable().main()

