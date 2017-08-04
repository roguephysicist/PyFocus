import sys
import cv2
import numpy as np

infile = sys.argv[1]
bitval = np.linspace(0, 255, 256)

imgg = cv2.imread(infile,0)
imgc = cv2.imread(infile)
histgray = cv2.calcHist([imgg],[0],None,[256],[0,256])
histr = cv2.calcHist([imgc],[2],None,[256],[0,256])
histg = cv2.calcHist([imgc],[1],None,[256],[0,256])
histb = cv2.calcHist([imgc],[0],None,[256],[0,256])

np.savetxt('hist.dat', np.c_[bitval, histgray, histr, histb, histg], \
                       fmt='%03i    %.6e    %.6e    %.6e    %.6e', \
                       header='val gray red blue green')
