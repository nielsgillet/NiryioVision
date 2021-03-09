from tkinter import *
from tkinter.messagebox import *
import time

fenetre = Tk()
fenetre.title('Gestion Robot 6 Axes')
fenetre.geometry("800x480")
texte_connexion_robot = StringVar()
texte_connexion_robot.set("Connexion au robot")
texte_connexion_reconnaissance = StringVar()
texte_connexion_reconnaissance.set("Connexion à la reconnaissance")

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


def connexion_robot():
    texte_connexion_robot.set("Connexion ...")
    time.sleep(3.0) # mettre procedure de connexion
    if 1 == 1:
        showinfo('', 'Connecté')
    else:
        showerror('', 'Erreur de connexion')
    texte_connexion_robot.set("Connexion au robot")


def connexion_reconnaissance():
    texte_connexion_reconnaissance.set("Connexion ...")
    time.sleep(3.0) # mettre procedure de connexion
    if 1 == 1:
        showinfo('', 'Connecté')
    else:
        showerror('', 'Erreur de connexion')
    texte_connexion_reconnaissance.set("Connexion à la reconnaissance")


def lancement_fenetre_manu():
    def quitter():
        top.destroy()  ## Détruit la fenêtre secondaire
        fenetre.deiconify()  ## Remet en avant-plan
    top=Toplevel(fenetre)
    fenetre.withdraw()
    top.overrideredirect(1)
    top.geometry("800x480")
    bouton_quitter = Button(top, text='Quitter', command=quitter)
    bouton_quitter.pack()


#elements présents sur la fenetre principale
Bouton_connexion_robot = Button(textvariable=texte_connexion_robot, command=connexion_robot, width=25)
Bouton_connexion_robot.grid(row=0, column=0)

Bouton_connexion_reconnaissance = Button(textvariable=texte_connexion_reconnaissance, command=connexion_reconnaissance, width=25)
Bouton_connexion_reconnaissance.grid(row=0, column=1)

Bouton_mode_manu = Button(text="Mode Manuel", command=lancement_fenetre_manu, width=25)
Bouton_mode_manu.grid(row=0, column=2)



fenetre.mainloop()