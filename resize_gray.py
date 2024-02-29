import cv2
import glob
import os
inputfolder = ''
os.mkdir('resized')
i=0
for img in glob.glob(inputfolder + "/*.jpg"):
    image = cv2.imread(img)
