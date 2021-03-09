import numpy as np
import cv2
import os
import tarfile
from scipy.spatial import distance



HEIGHT = 500
FOLDER_PATH = 'C:/Users/Nicolas/Desktop/Image IA grandes'
FOLDER_IN = os.listdir(FOLDER_PATH)
matrix_rond = []
matrix_square = []
matrx_square_im_kp = []
matrx_rond_im_kp = []
A, B, C = 0, 0, 0
dico = {"Square": 0, "Round": 1, "Triangle": 2, "Star": 3}
xlabel = []
ylabel = []
orb = cv2.ORB_create()
dist = []
matrice_test1=[]
matrice_test2=[]
size=tuple((500,500))

for class_path in FOLDER_IN:
    FOLDER_PATH_BIS = FOLDER_PATH + "/" + class_path
    FOLDER_IN_BIS = os.listdir(FOLDER_PATH_BIS)
    for index, photos in enumerate(FOLDER_IN_BIS):
        Image = cv2.imread(FOLDER_PATH_BIS + "/" + photos)
        gray_image = cv2.cvtColor(Image, cv2.COLOR_RGB2GRAY)
        gray_image=cv2.resize(gray_image,size)
        A += 1
        Image = Image.sort()
        if A <= 20:
            matrix_rond.append(gray_image)
        elif A > 20:
            matrix_square.append(gray_image)



for matrice in matrix_rond:
    xlabel.append(1)
    orb = cv2.ORB_create(nfeatures=20)
    kp, des_rond = orb.detectAndCompute(matrice, None)
    matrice=cv2.drawKeypoints(matrice,kp,None)
    matrice_test1.append(matrice)
    des_rond = np.asarray(des_rond)
    des_rond = list(des_rond.flatten())
    ylabel.append(des_rond)


for matrice in matrix_square:
    xlabel.append(0)
    orb = cv2.ORB_create(nfeatures=20)
    kp, des_square = orb.detectAndCompute(matrice, None)
    matrice = cv2.drawKeypoints(matrice, kp, None)
    matrice_test2.append(matrice)
    print(len(matrice_test2))
    des_square = np.asarray(des_square)
    des_square = list(des_square.flatten())
    ylabel.append(des_square)


cv2.imshow("test",matrice_test1[12])

cv2.waitKey(0)
