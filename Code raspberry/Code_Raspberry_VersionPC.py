#!/usr/bin/env python

# ! You need to launch the server first !
parametre_position=[0, 0, 0, 0, 0, 0]


position_repos=[0, 0.64, -1.397, 0, 0, -2.04]

position1_bas = [-1.582, -1.115, 0.183, 0.015, -0.585, -2.04]
position2_bas = [-0.75, -1.115, 0.183, 0.015, -0.585, -2.04]
position3_bas = [-0.05, -1.115, 0.183, 0.015, -0.585, -2.04]
position4_bas = [0.62, -1.115, 0.183, 0.015, -0.585, -2.04]
position5_bas = [1.42, -1.115, 0.183, 0.015, -0.585, -2.04]

position1_haut = [-1.582, -1, 0.183, 0.015, -0.73, -2.04]
position2_haut = [-0.75, -1, 0.183, 0.015, -0.73, -2.04]
position3_haut = [-0.05, -1, 0.183, 0.015, -0.73, -2.04]
position4_haut = [0.62, -1, 0.183, 0.015, -0.73, -2.04]
position5_haut = [1.42, -1, 0.183, 0.015, -0.73, -2.04]

position_milieu = [3, -0.3 , -0.357, 0.491, -0.668, -2.04]



from pymodbus.client.sync import ModbusTcpClient
from tkinter import *
from tkinter.messagebox import *
import time

###################################
#interface graphique

fenetre = Tk()
fenetre.title('Gestion Robot 6 Axes')
fenetre.geometry("800x480")

def alert():
    showinfo("Logiciel de gestion de robot", "By Gillet, Hartman, Houba")


menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)


menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)


######################################################
#Commandes robot

# Positive number : 0 - 32767
# Negative number : 32768 - 65535
def number_to_raw_data(val):
    if val < 0:
        val = (1 << 15) - val
    return val


def raw_data_to_number(val):
    if (val >> 15) == 1:
        val = - (val & 0x7FFF)
    return val


def envoi_position(parametre_position):
    joints_to_send = list(map(lambda j: int(number_to_raw_data(j * 1000)), parametre_position))

    client.write_registers(0, joints_to_send)
    client.write_register(100, 1)

    # Wait for end of Move command
    while client.read_holding_registers(150, count=1).registers[0] == 1:
        time.sleep(0.01)

def fermeture_pince():
    client.write_register(511, 11)
    time.sleep(1.5)
def ouverture_pince():
    client.write_register(510, 11)
    time.sleep(1.5)

def connexion_robot():
    texte_connexion_robot.set("Connexion ...")

    texte_connexion_robot.set("Connexion au robot")


def mode_auto():
    envoi_position(position5_haut)
    ouverture_pince()
    envoi_position(position5_bas)
    fermeture_pince()
    envoi_position(position5_haut)
    envoi_position(position1_haut)
    envoi_position(position1_bas)
    ouverture_pince()
    envoi_position(position1_haut)
    time.sleep(1)
    envoi_position(position_repos)

    # Activate learning mode
    client.write_register(300, 1)

def lancement_fenetre_manu():
    def quitter():
        top.destroy()  ## Detruit la fenêtre secondaire
        fenetre.deiconify()  ## Remet en avant-plan
    def manu_position1_bas():
        envoi_position(position1_bas)
    def manu_position1_haut():
        envoi_position(position1_haut)

    def manu_position2_bas():
        envoi_position(position2_bas)
    def manu_position2_haut():
        envoi_position(position2_haut)

    def manu_position3_bas():
        envoi_position(position3_bas)
    def manu_position3_haut():
        envoi_position(position3_haut)

    def manu_position4_bas():
        envoi_position(position4_bas)
    def manu_position4_haut():
        envoi_position(position4_haut)

    def manu_position5_bas():
        envoi_position(position5_bas)
    def manu_position5_haut():
        envoi_position(position5_haut)

    def learning_mode():
        client.write_register(300, 1)

    def manu_position_repos():
        envoi_position(position_repos)

    top=Toplevel(fenetre)
    fenetre.withdraw()
    top.overrideredirect(1)
    top.geometry("800x480")
    bouton_quitter = Button(top, text='Quitter', command=quitter, borderwidth=1).grid(row=1, column=1)
    Bouton_position1_bas = Button(top, text='Position 1 bas', command=manu_position1_bas, borderwidth=1).grid(row=3, column=1)
    Bouton_position1_haut = Button(top, text='Position 1 haut', command=manu_position1_haut, borderwidth=1).grid(row=5, column=1)

    Bouton_position2_bas = Button(top, text='Position 2 bas', command=manu_position2_bas, borderwidth=1).grid(row=3, column=2)
    Bouton_position2_haut = Button(top, text='Position 2 haut', command=manu_position2_haut, borderwidth=1).grid(row=5, column=2)

    Bouton_position3_bas = Button(top, text='Position 3 bas', command=manu_position3_bas, borderwidth=1).grid(row=3, column=3)
    Bouton_position3_haut = Button(top, text='Position 3 haut', command=manu_position3_haut, borderwidth=1).grid(row=5, column=3)

    Bouton_position4_bas = Button(top, text='Position 4 bas', command=manu_position4_bas, borderwidth=1).grid(row=3,column=4)
    Bouton_position4_haut = Button(top, text='Position 4 haut', command=manu_position4_haut, borderwidth=1).grid(row=5,column=4)

    Bouton_position5_bas = Button(top, text='Position 5 bas', command=manu_position5_bas, borderwidth=1).grid(row=3,column=5)
    Bouton_position5_haut = Button(top, text='Position 5 haut', command=manu_position5_haut, borderwidth=1).grid(row=5,column=5)

    Bouton_fermeture = Button(top, text='Fermeture pince', command=fermeture_pince, borderwidth=1).grid(row=6,column=1)
    Bouton_ouverture = Button(top, text='Ouverture pince', command=ouverture_pince, borderwidth=1).grid(row=6,column=2)
    Bouton_position_repos = Button(top, text='Position Repos', command=manu_position_repos, borderwidth=1).grid(row=6,column=3)
    Bouton_learning_mode = Button(top, text='Learning mode', command=learning_mode, borderwidth=1).grid(row=6,column=4)


if __name__ == '__main__':

    print("--- START")

    ################################################
    ###lignes a supprimer pour demarrer sans robot##
    ################################################

    client = ModbusTcpClient("10.111.20.242", port=6677)

    client.connect()
    print("Connected to modbus server")

    print("Calibrate Robot if needed")
    client.write_register(311, 1)
    time.sleep(1)

    # Wait for end of calibration
    while client.read_input_registers(402, 1).registers[0] == 1:
        time.sleep(0.05)

    client.write_register(500, 11)
    time.sleep(1)
    client.write_register(401, 1000)
    time.sleep(1)
    client.write_register(402, 1000)
    time.sleep(1)



    ####################################################
    ####################################################
    ####################################################




    # elements présents sur la fenetre principale

    Bouton_mode_auto = Button(text="Mode Auto",command=mode_auto, width=25)
    Bouton_mode_auto.grid(row=0, column=1)

    Bouton_mode_manu = Button(text="Mode Manuel", command=lancement_fenetre_manu, width=25)
    Bouton_mode_manu.grid(row=0, column=2)

    fenetre.mainloop()








