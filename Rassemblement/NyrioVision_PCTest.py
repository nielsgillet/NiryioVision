from threading import Thread
import numpy as np
import cv2
from pymodbus.client.sync import ModbusTcpClient
from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
import time

textType = ""
mat = ['', '', '', 0]
dic = ["Round", "Square", "Triangle", "Star", "Rien", "Autre"]
dim = [400, 400]
gorobot = False


class Reco(Thread):
    def __init__(self):
        print("init Reco")
        Thread.__init__(self)
        self.cap = cv2.VideoCapture(0)

    def run(self):
        print("run Reco")
        while True:
            _, frame = self.cap.read()
            frame = cv2.resize(frame, (dim[0], dim[1]))
            frame = cv2.flip(frame, 1)
            blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
            hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2RGB)
            lower_red = np.array([0, 0, 0])
            upper_red = np.array([170, 70, 70])
            mask = cv2.inRange(hsv, lower_red, upper_red)
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            for contour in contours:
                area = cv2.contourArea(contour)
                approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
                if area > 2000:
                    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
                    x = approx.ravel()[0]
                    y = approx.ravel()[1]
                    if len(approx) == 12:
                        cv2.putText(frame, dic[3], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                        mat[2] = 1
                    elif len(approx) == 4:
                        cv2.putText(frame, dic[1], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                        mat[2] = 2
                    elif len(approx) == 3:
                        cv2.putText(frame, dic[2], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                        mat[2] = 3
                    elif len(approx) == 8:
                        cv2.putText(frame, dic[0], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                        mat[2] = 4
                    elif len(approx) == 0:
                        cv2.putText(frame, dic[4], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                        mat[2] = 0
                    else:
                        cv2.putText(frame, dic[5], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                        mat[2] = -1
            mat[0] = frame
            mat[1] = mask


class Affichage(Thread):
    def __init__(self, ro):
        print("init Affichage")
        Thread.__init__(self)
        self.rob = ro
        self.rob.test = False

    def lanc(self):
        self.rob.test = True

    def run(self):
        print("run Affichage")

        fenetre = Tk()
        fenetre.title('Gestion Robot 6 Axes')
        fenetre.geometry("800x480")
        fenetre.resizable(width=False, height=False)

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

        def lancement_fenetre_manu():
            def quitter():
                top.destroy()  ## Detruit la fenêtre secondaire
                fenetre.deiconify()  ## Remet en avant-plan

            def manu_position1_bas():
                self.rob.envoi_position(self.rob.position_bas[1])

            def manu_position1_haut():
                self.rob.envoi_position(self.rob.position_haut[1])

            def manu_position1_camera():
                self.rob.envoi_position(self.rob.position_camera[1])

            def manu_position2_bas():
                self.rob.envoi_position(self.rob.position_bas[2])

            def manu_position2_haut():
                self.rob.envoi_position(self.rob.position_haut[2])

            def manu_position2_camera():
                self.rob.envoi_position(self.rob.position_camera[2])

            def manu_position3_bas():
                self.rob.envoi_position(self.rob.position_bas[3])

            def manu_position3_haut():
                self.rob.envoi_position(self.rob.position_haut[3])

            def manu_position3_camera():
                self.rob.envoi_position(self.rob.position_camera[3])

            def manu_position4_bas():
                self.rob.envoi_position(self.rob.position_bas[4])

            def manu_position4_haut():
                self.rob.envoi_position(self.rob.position_haut[4])

            def manu_position4_camera():
                self.rob.envoi_position(self.rob.position_camera[4])

            def manu_position5_bas():
                self.rob.envoi_position(self.rob.position_bas[5])

            def manu_position5_haut():
                self.rob.envoi_position(self.rob.position_haut[5])

            def manu_position5_camera():
                self.rob.envoi_position(self.rob.position_camera[5])

            def manu_position_Square():
                self.rob.envoi_position(self.rob.position_Square)

            def manu_position_Triangle():
                self.rob.envoi_position(self.rob.position_Triangle)

            def manu_position_Round():
                self.rob.envoi_position(self.rob.position_Round)

            def manu_position_Star():
                self.rob.envoi_position(self.rob.position_Star)

            def learning_mode():
                self.rob.client.write_register(300, 1)

            def manu_position_repos():
                self.rob.envoi_position(self.rob.position_repos)

            top = Toplevel(fenetre)
            fenetre.withdraw()
            top.overrideredirect(1)
            top.geometry("800x480")

            bouton_quitter = Button(top, text='Quitter', command=quitter, borderwidth=1, height=4, width=14).grid(row=1,
                                                                                                                  column=1)
            Bouton_position1_bas = Button(top, text='Position 1 bas', command=manu_position1_bas,
                                          borderwidth=1, height=4, width=14).grid(row=3, column=1)
            Bouton_position1_haut = Button(top, text='Position 1 haut', command=manu_position1_haut,
                                           borderwidth=1, height=4, width=14).grid(row=5, column=1)
            Bouton_position2_bas = Button(top, text='Position 2 bas', command=manu_position2_bas,
                                          borderwidth=1, height=4, width=14).grid(row=3, column=2)
            Bouton_position2_haut = Button(top, text='Position 2 haut', command=manu_position2_haut,
                                           borderwidth=1, height=4, width=14).grid(row=5, column=2)
            Bouton_position3_bas = Button(top, text='Position 3 bas', command=manu_position3_bas,
                                          borderwidth=1, height=4, width=14).grid(row=3, column=3)
            Bouton_position3_haut = Button(top, text='Position 3 haut', command=manu_position3_haut,
                                           borderwidth=1, height=4, width=14).grid(row=5, column=3)
            Bouton_position4_bas = Button(top, text='Position 4 bas', command=manu_position4_bas,
                                          borderwidth=1, height=4, width=14).grid(row=3, column=4)
            Bouton_position4_haut = Button(top, text='Position 4 haut', command=manu_position4_haut,
                                           borderwidth=1, height=4, width=14).grid(row=5, column=4)
            Bouton_position5_bas = Button(top, text='Position 5 bas', command=manu_position5_bas,
                                          borderwidth=1, height=4, width=14).grid(row=3, column=5)
            Bouton_position5_haut = Button(top, text='Position 5 haut', command=manu_position5_haut,
                                           borderwidth=1, height=4, width=14).grid(row=5, column=5)
            Bouton_fermeture = Button(top, text='Fermeture pince', command=self.rob.fermeture_pince,
                                      borderwidth=1, height=4, width=14).grid(row=6, column=1)
            Bouton_ouverture = Button(top, text='Ouverture pince', command=self.rob.ouverture_pince,
                                      borderwidth=1, height=4, width=14).grid(row=6, column=2)
            Bouton_position_repos = Button(top, text='Position Repos', command=manu_position_repos,
                                           borderwidth=1, height=4, width=14).grid(row=6, column=3)
            Bouton_learning_mode = Button(top, text='Learning mode', command=learning_mode, borderwidth=1, height=4,
                                          width=14).grid(row=6, column=4)
            Bouton_position_milieu = Button(top, text='Position Star', command=manu_position_Star,
                                            borderwidth=1, height=4, width=14).grid(row=7, column=1)
            Bouton_position_droite = Button(top, text='Position Triangle', command=manu_position_Triangle,
                                            borderwidth=1, height=4, width=14).grid(row=7, column=2)
            Bouton_position_gauche = Button(top, text='Position Round', command=manu_position_Round,
                                            borderwidth=1, height=4, width=14).grid(row=7, column=3)
            Bouton_position_gauche = Button(top, text='Position Square', command=manu_position_Square,
                                            borderwidth=1, height=4, width=14).grid(row=7, column=4)
            Bouton_position1_camera = Button(top, text='Position 1 Camera', command=manu_position1_camera,
                                             borderwidth=1, height=4, width=14).grid(row=8, column=1)
            Bouton_position2_camera = Button(top, text='Position 2 Camera', command=manu_position2_camera,
                                             borderwidth=1, height=4, width=14).grid(row=8, column=2)
            Bouton_position3_camera = Button(top, text='Position 3 Camera', command=manu_position3_camera,
                                             borderwidth=1, height=4, width=14).grid(row=8, column=3)
            Bouton_position4_camera = Button(top, text='Position 4 Camera', command=manu_position4_camera,
                                             borderwidth=1, height=4, width=14).grid(row=8, column=4)
            Bouton_position1_camera = Button(top, text='Position 5 Camera', command=manu_position5_camera,
                                             borderwidth=1, height=4, width=14).grid(row=8, column=5)

        Bouton_mode_auto = Button(text="Mode Auto", command=self.lanc, width=45, height=2)
        Bouton_mode_auto.grid(row=0, column=0)
        Bouton_mode_manu = Button(text="Mode Manuel", command=lancement_fenetre_manu, width=45, height=2)
        Bouton_mode_manu.grid(row=0, column=1)
        Image_mask, Image_Frame = Canvas(fenetre), Canvas(fenetre)

        while True:
            if (len(mat[0]) != 0) or (len(mat[1]) != 0):
                labfps = Label(text=textType, width=25)
                labfps.grid(row=1, column=0)
                labtype = Label(text=dic[mat[2]], width=25)
                labtype.grid(row=1, column=1)

                image_frame = Image.fromarray(mat[0])
                image_mask = Image.fromarray(mat[1])

                image_frame = ImageTk.PhotoImage(image_frame)
                image_mask = ImageTk.PhotoImage(image_mask)

                Image_mask.config(height=dim[0], width=dim[1])
                Image_mask.create_image(dim[0] / 2, dim[1] / 2, image=image_frame)
                Image_mask.grid(row=4, column=0)

                Image_Frame.config(height=dim[0], width=dim[1])
                Image_Frame.create_image(dim[0] / 2, dim[1] / 2, image=image_mask)
                Image_Frame.grid(row=4, column=1)

                fenetre.update()
        fenetre.mainloop()


class Robot(Thread):
    def __init__(self):
        print("init Robot")
        Thread.__init__(self)
        self.test = False
        self.position_repos = [0, 0.64, -1.397, 0, 0, -0.5]
        self.position_bas = [[0, 0.64, -1.397, 0, 0, -0.5], [-1.582, -1.115, 0.183, 0.015, -0.585, -0.5],
                             [-0.75, -1.115, 0.183, 0.015, -0.585, -0.5], [-0.05, -1.115, 0.183, 0.015, -0.585, -0.5],
                             [0.62, -1.115, 0.183, 0.015, -0.585, -0.5], [1.42, -1.115, 0.183, 0.015, -0.585, -0.5]]
        self.position_haut = [[0, 0.64, -1.397, 0, 0, -0.5], [-1.582, -1, 0.183, 0.015, -0.73, -0.5],
                              [-0.75, -1, 0.183, 0.015, -0.73, -0.5], [-0.05, -1, 0.183, 0.015, -0.73, -0.5],
                              [0.62, -1, 0.183, 0.015, -0.73, -0.5], [1.42, -1, 0.183, 0.015, -0.73, -0.5]]
        self.position_camera = [[0, 0.64, -1.397, 0, 0, -0.5], [-1.582, -1.242, 1.244, 0.015, -0.73, -0.5],
                                [-0.75, -1.242, 1.244, 0.015, -0.73, -0.5], [-0.05, -1.242, 1.244, 0.015, -0.73, -0.5],
                                [0.62, -1.242, 1.244, 0.015, -0.73, -0.5], [1.42, -1.242, 1.244, 0.015, -0.73, -0.5]]
        self.position_Square = [3, -0.3, -0.357, 0.491, -0.668, -0.5]
        self.position_Triangle = [2.77, -0.456, -0.207, 0.084, -0.763, -0.5]
        self.position_Round = [-2.837, -0.456, -0.207, 0.084, -0.763, -0.5]
        self.position_Star = [-2.537, -0.456, -0.207, 0.084, -0.763, -0.5]
        print("<--- START --->")
        if gorobot:
            self.client = ModbusTcpClient("10.111.20.242", port=6677)
            self.client.connect()
            print("Connected to modbus server")
            print("Calibrate Robot if needed")
            self.client.write_register(311, 1)
            time.sleep(1)
            while self.client.read_input_registers(402, 1).registers[0] == 1:
                time.sleep(0.05)
            self.client.write_register(500, 11)
            time.sleep(1)
            self.client.write_register(401, 1000)
            time.sleep(1)
            self.client.write_register(402, 1000)
            time.sleep(1)

    def run(self):
        print("run Robot")
        while True:
            if self.test == True:
                print("run Robot automatique")
                self.mode_auto()

    def number_to_raw_data(self, val):
        if val < 0:
            val = (1 << 15) - val
        return val

    def raw_data_to_number(self, val):
        if (val >> 15) == 1:
            val = - (val & 0x7FFF)
        return val

    def envoi_position(self, parametre_position):
        joints_to_send = list(map(lambda j: int(self.number_to_raw_data(j * 1000)), parametre_position))
        self.client.write_registers(0, joints_to_send)
        self.client.write_register(100, 1)
        # Wait for end of Move command
        while self.client.read_holding_registers(150, count=1).registers[0] == 1:
            time.sleep(0.01)

    def fermeture_pince(self):
        self.client.write_register(511, 11)
        time.sleep(1.5)

    def ouverture_pince(self):
        self.client.write_register(510, 11)
        time.sleep(1.5)

    def mode_auto(self):
        typeText = ""
        compteur = 1
        resultat = ['']
        self.ouverture_pince()
        self.envoi_position(self.position_repos)
        while compteur < 6:
            self.envoi_position(self.position_camera[compteur])
            time.sleep(1)
            resultat.append(mat[2])
            typeText += (", " + dic[mat[2] - 1])
            if resultat[compteur] == 1:
                self.envoi_position(self.position_haut[compteur])
                self.envoi_position(self.position_bas[compteur])
                self.fermeture_pince()
                self.envoi_position(self.position_haut[compteur])
                self.envoi_position(self.position_Round)
                self.ouverture_pince()
            elif resultat[compteur] == 2:
                self.envoi_position(self.position_haut[compteur])
                self.envoi_position(self.position_bas[compteur])
                self.fermeture_pince()
                self.envoi_position(self.position_haut[compteur])
                self.envoi_position(self.position_Square)
                self.ouverture_pince()
            elif resultat[compteur] == 3:
                self.envoi_position(self.position_haut[compteur])
                self.envoi_position(self.position_bas[compteur])
                self.fermeture_pince()
                self.envoi_position(self.position_haut[compteur])
                self.envoi_position(self.position_Triangle)
                self.ouverture_pince()
            elif resultat[compteur] == 4:
                self.envoi_position(self.position_haut[compteur])
                self.envoi_position(self.position_bas[compteur])
                self.fermeture_pince()
                self.envoi_position(self.position_haut[compteur])
                self.envoi_position(self.position_Star)
                self.ouverture_pince()
            else:
                compteur += 1
                textType = typeText
                continue
            compteur += 1
            textType = typeText
        self.envoi_position(self.position_repos)
        self.client.write_register(300, 1)
        self.test = False


# exécution
thread_reco = Reco()
thread_robot = Robot()
thread_affichage = Affichage(thread_robot)

thread_reco.start()
thread_robot.start()
thread_affichage.start()

thread_reco.join()
thread_robot.join()
thread_affichage.join()
