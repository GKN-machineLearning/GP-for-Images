import os
from PIL import Image
import numpy as np
from numpy import asarray
# Open the image form working directory
os.chdir("C:\Python")

def decodeImage(fileName):
    #get image array
    image = Image.open(fileName)
    
    #TODO size/mode checking
    
    data = asarray(image)
    dataArr = []
    lblArr = []
    for x in range(0,256):
        for y in range(0,256):
            newDA = []
            if x < 16:
                newDA.append(0)
                newDA.append(x)
            else:   
                hexX = str(hex(x))
                newDA.append(int(hexX[2],16))
                newDA.append(int(hexX[3],16))
            if y < 16:
                newDA.append(0)
                newDA.append(y)
            else:
                hexY = str(hex(y))
                newDA.append(int(hexY[2],16))
                newDA.append(int(hexY[3],16))
            dataArr.append(newDA)
            lblArr.append(data[x][y])
    return np.array(dataArr), np.array(lblArr)
        
def drawImage(dataArr, lblArr):
    outArr = np.arange(256*256).reshape((256,256))
    nRows = len(dataArr)
    for r in range(0,nRows):
        dRow = dataArr[r]
        x = int("".join([str(hex(dRow[0]))[2],str(hex(dRow[1]))[2]]),16)
        y = int("".join([str(hex(dRow[2]))[2],str(hex(dRow[3]))[2]]),16)
        outArr[x][y] = lblArr[r]
    Image.fromarray((outArr * 16).astype('uint8'), mode='L').save('out_Portrait.png')
