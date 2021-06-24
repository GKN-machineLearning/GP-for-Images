import os
from PIL import Image
import numpy as np
from numpy import asarray
# Open the image form working directory
os.chdir("C:\Python")

dataArr = np.array(np.meshgrid(range(0,4), range(0,4))).T.reshape(-1,2)

def decodeImage(fileName):
    pass
        
def drawImage(lblArr, filename):
    outArr = np.arange(4*4).reshape((4,4))
    nRows = len(dataArr)
    for r in range(0,nRows):
        dRow = dataArr[r]
        outArr[dRow[0]][dRow[1]] = lblArr[r]
    Image.fromarray((outArr * 16).astype('uint8'), mode='L').save(''.join([filename, ".png"]))
