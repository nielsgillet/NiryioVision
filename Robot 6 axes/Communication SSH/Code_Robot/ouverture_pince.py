#!/usr/bin/env python
# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import rospy
import time

rospy.init_node('niryo_one_example_python_api')
n = NiryoOne()
try:
    n.change_tool(TOOL_GRIPPER_1_ID)
    n.open_gripper(TOOL_GRIPPER_1_ID, 500)
    #n.close_gripper(TOOL_GRIPPER_1_ID, 500)

except NiryoOneException as e:
    print(e)
    # handle exception here
    # you can also make a try/except for each command separately

print("done")#utilisé pour detecter fin commande sur le maitre
