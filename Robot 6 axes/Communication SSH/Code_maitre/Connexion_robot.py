#import paramiko
#import warnings
#warnings.filterwarnings(action='ignore',module='.*paramiko.*')
#import os,sys,time


#client = paramiko.SSHClient()
#client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#client.connect("10.111.20.10",port=22,username="niryo", password="robotics")

#stdin, stdout, stderr = client.exec_command('getconf PATH')
#print ("PATH: ", stdout.readlines())


#stdin, stdout, stderr = client.exec_command('./raccourci.sh')
#print ("stderr: ", stderr.readlines())

#stdin, stdout, stderr = client.exec_command("ls -l")
#for line in stdout.read().splitlines():
#     print (line)


#!/bin/python
#import sys
#import os


#os.system("sshpass -p robotics ssh -T niryo@10.111.20.10 ./raccourci.sh")

#ssh niryo@ip_address ‘source ~/catkin_ws/devel/setup.bash && export PYTHONPATH=${PYTHONPATH}:/home/niryo/catkin_ws/src/niryo_one_python_api/src/niryo_python_api && python your_script.py’
# sudo apt-get install sshpass
#sshpass -p your_password ssh user@hostname



###########################################################################################





import sys
import os

#os.system("sshpass -p robotics ssh -T niryo@10.111.20.10 ‘source ~/catkin_ws/devel/setup.bash && export PYTHONPATH=${PYTHONPATH}:/home/niryo/catkin_ws/src/niryo_one_python_api/src/niryo_python_api && python your_script.py’")


#fonction envoyant position
parametre_position = [3, -0.38596709744103175, -0.02792526803190927, -0.06450736915371043, -1.1104482832888722, 0.1569050]
def envoi_position(parametre_position):
    f = open('position.txt', 'w')
    for i in range(0,6):
        f.write(str(parametre_position[i]) + '\n')
    #envoi fichier txt avec position
    os.system("sshpass -p robotics scp  /home/portable/Documents/Projets/NyrioVision/Robot 6 axes/Code_maitre/position.txt Nyrio@10.111.20.10:/home/Nyrio")
    #execute code python sur le robot changeant position
    os.system("sshpass -p robotics ssh -T niryo@10.111.20.10 ‘source ~/catkin_ws/devel/setup.bash && export PYTHONPATH=${PYTHONPATH}:/home/niryo/catkin_ws/src/niryo_one_python_api/src/niryo_python_api && python envoi_position.py’")

def calibrage():
    os.system("sshpass -p robotics ssh -T niryo@10.111.20.10 ‘source ~/catkin_ws/devel/setup.bash && export PYTHONPATH=${PYTHONPATH}:/home/niryo/catkin_ws/src/niryo_one_python_api/src/niryo_python_api && python calibrage.py’")

def ouverture_pince():
    os.system("sshpass -p robotics ssh -T niryo@10.111.20.10 ‘source ~/catkin_ws/devel/setup.bash && export PYTHONPATH=${PYTHONPATH}:/home/niryo/catkin_ws/src/niryo_one_python_api/src/niryo_python_api && python ouverture_pince.py’")

def fermeture_pince():
    os.system("sshpass -p robotics ssh -T niryo@10.111.20.10 ‘source ~/catkin_ws/devel/setup.bash && export PYTHONPATH=${PYTHONPATH}:/home/niryo/catkin_ws/src/niryo_one_python_api/src/niryo_python_api && python fermeture_pince.py’")



calibrage()
ouverture_pince()
fermeture_pince()
envoi_position([3,0.1,3.5,1,7,8])

print("finit.")
