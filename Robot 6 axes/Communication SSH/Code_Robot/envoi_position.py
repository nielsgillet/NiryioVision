#!/usr/bin/env python
pos = [3, -0.38596709744103175, -0.02792526803190927, -0.06450736915371043, -1.1104482832888722, 0.1569050]
compteur = 0
# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import rospy
import time

rospy.init_node('niryo_one_example_python_api')
n = NiryoOne()
try:
    #desactiver mode apprentissage (maintient position actif)
    n.activate_learning_mode(False)
    #vitesse maximale
    n.set_arm_max_velocity(100)
	
    compteur=0
	#lit fichier position et place chaque ligne dans un tableau
    f = open("position.txt",'r')
    for line in f:
	if compteur < 6:
            pos[compteur]=float(line.strip())
	compteur+=1
    f.close()
	#envoi position
    n.move_joints(pos)

except NiryoOneException as e:
    print(e)
    # handle exception here
    # you can also make a try/except for each command separately

print("done")
