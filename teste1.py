import sys
import dlib
import cv2
import os
import glob

for arquivos in glob.glob(os.path.join('output' , '*jpg')):
    imagem = cv2.imread(arquivos)
    detector = dlib.simple_object_detector("teste.svm")
    logosDetectadas = detector(imagem, 4)
    numLogosDetectadas = len(logosDetectadas)
    if numLogosDetectadas > 0:
        print(arquivos)

