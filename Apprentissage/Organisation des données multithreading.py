from threading import Thread
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from scipy.spatial import *
import random
import time

chem = ["C:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Image IA",
        "C:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Image IA New",
        "C:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Image IA NewR",
        "C:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Image IA Redim",
        "C:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Image IA test",
        "C:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Test"]
dic = ["Round", "Square", "Triangle", "Star"]
marqueur = ['o', 's', '^', '*', 'P', 'D', 'h', 'X', '1', 'p']
lab = ["Rond-Rond", "Carre-Carre", "Triangle-Triangle", "Etoile-Etoile", "Rond-Carre", "Rond-Triangle", "Rond-Etoile",
       "Carre-Triangle", "Carre-Etoile", "Triangle-Etoile"]


class Lecture_image(Thread):
    matr = [[], [], [], []]
    dic = ["Round", "Square", "Triangle", "Star"]

    def __init__(self, chemin, nom):
        Thread.__init__(self)
        self.chemin = chemin
        self.nom = nom

    def run(self):
        matt = []
        folder_path_bis = self.chemin + "/" + self.nom
        folder_in_bis = os.listdir(folder_path_bis)
        for index, photos in enumerate(folder_in_bis):
            Image = cv2.imread(folder_path_bis + "/" + photos)
            gray_image = cv2.cvtColor(Image, cv2.COLOR_RGB2GRAY)
            print("Lecture de l'image {} n°: {}".format(self.nom, index+1))
            matt.append(gray_image)
        for index, nnn in enumerate(self.dic):
            if self.nom == nnn:
                self.matr[index] = matt


class Traitement:
    def __init__(self, nbre_img, npf, numero_chemin, mod):
        self.nbre_img = nbre_img
        self.npf = npf
        self.numero_chemin = numero_chemin
        self.mod = mod

    def mise_en_matrice(self, var, text):
        if self.mod == "ORB":
            mod_descri = cv2.ORB_create(nfeatures=self.npf)
        elif self.mod == "SIFT":
            mod_descri = cv2.xfeatures2d.SIFT_create(nfeatures=self.npf)
        labelx, labely, matrice_kp = [], [], []
        if text == "Round":
            nbr = 0
        elif text == "Square":
            nbr = 1
        elif text == "Triangle":
            nbr = 2
        elif text == "Star":
            nbr = 3
        else:
            nbr = 10
        for index, matrice in enumerate(var):
            print("Image mise en matrice {} n°: {}".format(text, index+1))
            labelx.append(nbr)
            if self.mod == "ORB":
                kp, des = mod_descri.detectAndCompute(matrice, None)
            elif self.mod == "SIFT":
                kp, des = mod_descri.detectAndCompute(matrice, None)
            des = np.asarray(des)
            des = list(des.flatten())
            labely.append(des)
            matrice_kp = cv2.drawKeypoints(matrice, kp, matrice)
        return labelx, labely, matrice_kp

    def mise_en_matrice_tout(self, var):
        labelx, labely, matrice_kp = [], [], []
        for index, a in enumerate(var):
            temp1, temp2, temp3 = self.mise_en_matrice(a, dic[index])
            labelx.extend(temp1)
            labely.append(temp2)
            matrice_kp.append(temp3)
        return labelx, labely, matrice_kp

    def obtenir_longueur(self, var):
        long = []
        for le in var:
            long.append(len(le))
        return long

    def obtenir_longueur_tout(self, var):
        mat = []
        for a in var:
            mat.append(self.obtenir_longueur(a))
        return mat

    def obtenir_longeur_max(self, var):
        maxi = 0
        for a in var:
            for b in a:
                if len(b) > maxi:
                    maxi = len(b)
        return maxi

    def obtenir_nbre_maxi(self, var, max):
        nbre_maxi = []
        for a in var:
            for b in a:
                nbre_maxi.append(len(b))
        return nbre_maxi.count(max)

    def calcul_distance_unique(self, var, valcom):
        dist = []
        b, c = 0, 0
        while b < len(var):
            if len(var[b]) != valcom:
                b += 1
                continue
            c = b + 1
            while c < len(var):
                if len(var[c]) != valcom:
                    c += 1
                    continue
                dist.append(distance.euclidean(var[b], var[c]))
                c += 1
            b += 1
        return dist

    def calcul_distance_inter(self, var1, var2, valcom):
        dist = []
        b, c = 0, 0
        while b < len(var1):
            if len(var1[b]) != valcom:
                b += 1
                continue
            c = 0
            while c < len(var2):
                if len(var2[c]) != valcom:
                    c += 1
                    continue
                dist.append(distance.euclidean(var1[b], var2[c]))
                c += 1
            b += 1
        return dist

    def calcul_distance_tout(self, var, valcom):
        mat = []
        a, b = 0, 0
        for c in var:
            mat.append(self.calcul_distance_unique(c, valcom))
        while a < len(var):
            b = a + 1
            while b < len(var):
                mat.append(self.calcul_distance_inter(var[a], var[b], valcom))
                b += 1
            a += 1
        return mat

    def mise_en_matrice_comparative(self, var, n_img, prendre=False, debut=0, fin=0, n=0, m=0):
        if prendre:
            n = int((n_img / 2))
            m = int((n_img / 2))
        else:
            debut = 0
            fin = (n_img * 5)
            n = int((n_img / 2))
            m = int((n_img / 2))
        random.shuffle(var)
        mat = var[debut:fin]
        mat = np.asarray(mat)
        mat = mat.reshape((n, m))
        return mat

    def mise_en_matrice_comparative_tout(self, var, n_img):
        mat = []
        mat.append(self.mise_en_matrice_comparative(var[0], n_img))
        mat.append(self.mise_en_matrice_comparative(var[1], n_img))
        mat.append(self.mise_en_matrice_comparative(var[4], n_img))
        mat.append(self.mise_en_matrice_comparative(var[4], n_img, True, debut=(n_img * 5), fin=(n_img * 10)))
        return mat

    def rassembler_matrice(self, var):
        a = np.concatenate((var[0], var[1]), axis=1)
        b = np.concatenate((var[2], var[3]), axis=1)
        c = np.concatenate((a, b), axis=0)
        return c

    def nonpair(self, var):
        if var % 2 == 1:
            return True
        else:
            return False

    def creer_vecteur(self, var):
        mat = []
        for index, a in enumerate(var):
            mat.append(list(np.full(shape=len(a), fill_value=index).flatten()))
        return mat

    def calcul_des_ecarts(self, var):
        mat = []
        mat.append(np.max(var))
        mat.append(np.min(var))
        mat.append(np.mean(var))
        mat.append(np.std(var))
        return mat

    def affichage_delatl(self, var):
        vect = self.creer_vecteur(var)
        for index, a in enumerate(var):
            plt.scatter(x=vect[index], y=a, s=5, marker=marqueur[index], label=lab[index])
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)
        plt.grid()
        plt.savefig('fig1.png', dpi=600)
        plt.show()

    def affichage_tout(self, var1, var2, var3, var4, n_arond=3):
        print("\nLes valeur de distance des classe sont:\nmax: {}\nmin: {}\nmoy: {}\necart: {}\n".format(
            np.format_float_positional(var1[0], n_arond),
            np.format_float_positional(var1[1], n_arond),
            np.format_float_positional(var1[2], n_arond),
            np.format_float_positional(var1[3], n_arond)))
        print(
            "Fin du tris des données:\nnpf valide: {}\nNombre d'image par classe: {}\nNombre de KP valide de: {}\n".format(
                var2, var3, var4))

    def affichage_kp(self, var):
        for a in var:
            cv2.imshow('Key point', a)
            cv2.waitKey(2)

    def lancement_tache(self):
        thread_1 = Lecture_image(chem[self.numero_chemin], "Round")
        thread_2 = Lecture_image(chem[self.numero_chemin], "Square")
        thread_3 = Lecture_image(chem[self.numero_chemin], "Triangle")
        thread_4 = Lecture_image(chem[self.numero_chemin], "Star")
        thread_1.start()
        thread_2.start()
        thread_3.start()
        thread_4.start()
        thread_1.join()
        thread_2.join()
        thread_3.join()
        thread_4.join()
        return Lecture_image.matr


def lancement(nbre_img=20, npf=20, numero_chemin=2, mod="ORB", recom=True):
    trait = Traitement(nbre_img, npf, numero_chemin, mod)
    print("\nExécution initialle avec:\n{} Images par classes\nNpf de: {}\nChemin image: {}\nDiscrpiteur: {}\n".format(
        nbre_img, npf, chem[numero_chemin], mod))
    matrix = trait.lancement_tache()
    while recom:
        xlabel, ylabel, kp_matrice = trait.mise_en_matrice_tout(matrix)
        longeur = trait.obtenir_longueur_tout(ylabel)
        long_max = trait.obtenir_longeur_max(ylabel)
        nombre_max = trait.obtenir_nbre_maxi(ylabel, long_max)
        if trait.nonpair(nombre_max):
            npf -= 1
            if npf < 1:
                print("Aucun npf valid trouvé choisisez en un plus élévé")
                break
            print(
                "\nLe npf choisi n'est pas valide et donne un nombre de KP valide impair {}, passage a npf ancien: {} à npf: {}\n".format(
                    nombre_max, npf + 1, npf))
            continue
        else:
            deltal = trait.calcul_distance_tout(ylabel, long_max)
            compar = trait.mise_en_matrice_comparative_tout(deltal, nbre_img)
            compar_finale = trait.rassembler_matrice(compar)
            recom = False
    observation = trait.calcul_des_ecarts(compar_finale)
    trait.affichage_tout(observation, npf, nbre_img, nombre_max)
    trait.affichage_delatl(deltal)
    #trait.affichage_kp(kp_matrice)


# Exécution programme
lancement(npf=45)

print("")
