import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from scipy.spatial import *
import random

chem = ["E:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Image IA",
        "E:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Image IA New",
        "E:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Image IA NewR",
        "E:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Image IA Redim",
        "E:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Image IA test",
        "E:/Webstorage/OneDrive - Haute Ecole de Namur-Liege-Luxembourg/Image machine learning/Test"]
dic = ["Round", "Square", "Triangle", "Star"]
marqueur = ['o', 's', '^', '*', 'P', 'D', 'h', 'X', '1', 'p']
lab = ["Rond-Rond", "Carre-Carre", "Triangle-Triangle", "Etoile-Etoile", "Rond-Carre", "Rond-Triangle", "Rond-Etoile",
       "Carre-Triangle", "Carre-Etoile", "Triangle-Etoile"]


def construction_matrice_image_tout(chemin, nbrimage):
    folder_in = os.listdir(chemin)
    a = 0
    mat, mat_rond, mat_square, mat_star, mat_triangle = [], [], [], [], []
    for class_path in folder_in:
        folder_path_bis = chemin + "/" + class_path
        folder_in_bis = os.listdir(folder_path_bis)
        for index, photos in enumerate(folder_in_bis):
            if index >= nbrimage:
                continue
            Image = cv2.imread(folder_path_bis + "/" + photos)
            gray_image = cv2.cvtColor(Image, cv2.COLOR_RGB2GRAY)
            a += 1
            if a <= nbrimage:
                print("Lecture de l'image round n°: {}".format(index))
                mat_rond.append(gray_image)
            elif a > nbrimage and (a <= 2 * nbrimage):
                print("Lecture de l'image square n°: {}".format(index))
                mat_square.append(gray_image)
            elif (a > 2 * nbrimage) and (a <= 3 * nbrimage):
                print("Lecture de l'image Star n°: {}".format(index))
                mat_star.append(gray_image)
            elif (a > 3 * nbrimage) and (a <= 4 * nbrimage):
                print("Lecture de l'image Triangle n°: {}".format(index))
                mat_triangle.append(gray_image)
    mat.append(mat_rond)
    mat.append(mat_square)
    mat.append(mat_star)
    mat.append(mat_triangle)
    return mat


def mise_en_matrice(var, text, type, nf):
    if type == "ORB":
        mod_descri = cv2.ORB_create(nfeatures=nf)
    elif type == "SIFT":
        mod_descri = cv2.xfeatures2d.SIFT_create(nfeatures=nf)
    labelx, labely = [], []
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
        print("Image mise en matrice {} n°: {}".format(text, index))
        labelx.append(nbr)
        kp, des = mod_descri.detectAndCompute(matrice, None)
        des = np.asarray(des)
        des = list(des.flatten())
        labely.append(des)
    return labelx, labely


def mise_en_matrice_tout(var, text, type, nf):
    labelx, labely = [], []
    for index, a in enumerate(var):
        temp1, temp2 = mise_en_matrice(a, text[index], type, nf)
        labelx.extend(temp1)
        labely.append(temp2)
    return labelx, labely


def obtenir_longueur(var):
    long = []
    for le in var:
        long.append(len(le))
    return long


def obtenir_longueur_tout(var):
    mat = []
    for a in var:
        mat.append(obtenir_longueur(a))
    return mat


def obtenir_longeur_max(var):
    maxi = 0
    for a in var:
        for b in a:
            if len(b) > maxi:
                maxi = len(b)
    return maxi


def obtenir_nbre_maxi(var, max):
    nbre_maxi = []
    for a in var:
        for b in a:
            nbre_maxi.append(len(b))
    return nbre_maxi.count(max)


def calcul_distance_unique(var, valcom):
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


def calcul_distance_inter(var1, var2, valcom):
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


def calcul_distance_tout(var, valcom):
    mat = []
    a, b = 0, 0
    for c in var:
        mat.append(calcul_distance_unique(c, valcom))
    while a < len(var):
        b = a + 1
        while b < len(var):
            mat.append(calcul_distance_inter(var[a], var[b], valcom))
            b += 1
        a += 1
    return mat


def mise_en_matrice_comparative(var, n_img, prendre=False, debut=0, fin=0, n=0, m=0):
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


def mise_en_matrice_comparative_tout(var, n_img):
    mat = []
    mat.append(mise_en_matrice_comparative(var[0], n_img))
    mat.append(mise_en_matrice_comparative(var[1], n_img))
    mat.append(mise_en_matrice_comparative(var[4], n_img))
    mat.append(mise_en_matrice_comparative(var[4], n_img, True, debut=(n_img * 5), fin=(n_img * 10)))
    return mat


def rassembler_matrice(var):
    a = np.concatenate((var[0], var[1]), axis=1)
    b = np.concatenate((var[2], var[3]), axis=1)
    c = np.concatenate((a, b), axis=0)
    return c


def dimentionement_matrice(var):
    return 0


def nonpair(var):
    if var % 2 == 1:
        return True
    else:
        return False


def creer_vecteur(var):
    mat = []
    for index, a in enumerate(var):
        mat.append(list(np.full(shape=len(a), fill_value=index).flatten()))
    return mat


def calcul_des_ecarts(var):
    mat = []
    mat.append(np.max(var))
    mat.append(np.min(var))
    mat.append(np.mean(var))
    mat.append(np.std(var))
    return mat


def affichage_delatl(var):
    vect = creer_vecteur(var)
    for index, a in enumerate(var):
        plt.scatter(x=vect[index], y=a, s=5, marker=marqueur[index], label=lab[index])
    plt.legend()
    plt.grid()
    plt.show()


def affichage_tout(var1, var2, var3, var4, n_arond=3):
    print("\nLes valeur de distance des classe sont:\nmax: {}\nmin: {}\nmoy: {}\necart: {}\n".format(
        np.format_float_positional(var1[0], n_arond),
        np.format_float_positional(var1[1], n_arond),
        np.format_float_positional(var1[2], n_arond),
        np.format_float_positional(var1[3], n_arond)))
    print(
        "Fin du tris des données:\nnpf valide: {}\nNombre d'image par classe: {}\nNombre de KP valide de: {}\n".format(
            var2, var3, var4))


def lancement(nbre_img=20, npf=20, numero_chemin=2, mod="ORB", recom=True):
    print("\nExécution initialle avec:\n{} Images par classes\nNpf de: {}\nChemin image: {}\nDiscrpiteur: {}\n".format(
        nbre_img, npf, chem[numero_chemin], mod))
    matrix = construction_matrice_image_tout(chem[numero_chemin], nbre_img)
    while recom:
        xlabel, ylabel = mise_en_matrice_tout(matrix, dic, mod, npf)
        longeur = obtenir_longueur_tout(ylabel)
        long_max = obtenir_longeur_max(ylabel)
        nombre_max = obtenir_nbre_maxi(ylabel, long_max)
        if nonpair(nombre_max):
            npf -= 1
            if npf < 1:
                print("Aucun npf valid trouvé choisisez en un plus élévé")
                break
            print(
                "\nLe npf choisi n'est pas valide et donne un nombre de KP valide impair {}, passage a npf ancien: {} à npf: {}\n".format(
                    nombre_max, npf + 1, npf))
            continue
        else:
            deltaL = calcul_distance_tout(ylabel, long_max)
            compar = mise_en_matrice_comparative_tout(deltaL, nbre_img)
            compar_finale = rassembler_matrice(compar)
            recom = False
    observation = calcul_des_ecarts(compar_finale)
    affichage_tout(observation, npf, nbre_img, nombre_max)
    affichage_delatl(deltaL)


# Exécution programme
lancement(npf=45, numero_chemin=2)

print("")
