#!/usr/bin/python
import cv2
import numpy as np

def cleanUpImage (imageName):
    img = cv2.imread(imageName + '.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = gray[40:-40,60:-60]
    ret,res1 = cv2.threshold(res,127,255,cv2.THRESH_BINARY)
    ret,res2 = cv2.threshold(res,50,255,cv2.THRESH_BINARY_INV)
    x, y = np.nonzero(res2)
    res3 = res1[np.amin(x):np.amax(x), np.amin(y):np.amax(y)]
    height, width = res3.shape
    res4 = res3[:,0:int(width/3)]
    res5 = res3[:,int(width/3)+1:int(2*width/3)]
    res6 = res3[:,int(2*width/3)+1:]

    cv2.imwrite('cleanedImage/' + imageName + '_1.jpg',res4)
    cv2.imwrite('cleanedImage/' + imageName + '_2.jpg',res5)
    cv2.imwrite('cleanedImage/' + imageName + '_3.jpg',res6)

def cleanImages ():
    for i in range(10):
        cleanUpImage('catalogofcopyr11libr_00' + str(i + 22))

if __name__ == '__main__':
    cleanImages()
