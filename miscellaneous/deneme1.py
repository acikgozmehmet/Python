#us flag 

from ezgraphics import GraphicsWindow
from math import *

A= 400 

# dimensions of the flag 
flagHeight  = A
flagWidth= 1.9* flagHeight
flagC = flagHeight * 7 / 13
flagD = flagWidth * 2 / 5
flagE = flagC / 10 
flagF = flagE
flagG = flagD / 12
flagH = flagG
flagL = flagHeight / 13
StarK = flagL * 4 / 5



us = GraphicsWindow(flagWidth, flagHeight )
canvas = us.canvas()

# the stripes are being drawn
for i in range(13):
    canvas.setColor("white")
    if (i % 2 ) == 0 :
        canvas.setColor(191, 10, 48)      
    canvas.drawRect(0, i*flagL, flagWidth, flagL)
   
# The canton part
canvas.setFill (0, 40, 104)
canvas.drawRect(0,0, flagD, flagC) 

canvas.setColor("white")

# the 6 star row of the canton
# getting the positions of stars 
#posOfStars=[]
posOfStarsX=[]
posOfStarsY=[]

for i in range(5):
    for j in range(1,7):
        #canvas.drawOval(flagG+(j-1)*2*flagH,flagE+i*2*flagF,2*StarK,2*StarK)
        #posOfStars.append([round(flagG+(j-1)*2*flagH), round(flagE+i*2*flagF)])
        posOfStarsX.append(round(flagG+(j-1)*2*flagH))
        posOfStarsY.append(round(flagE+i*2*flagF))
# the 5 star row of the canton
for i in range(4):
    for k in range(1,6):
            #canvas.drawOval(flagG+(2*k-1)*flagH,flagE+(2*i+1)*flagF,2*StarK,2*StarK) 
            #posOfStars.append([round(flagG+(2*k-1)*flagH),round(flagE+(2*i+1)*flagF)])
            posOfStarsX.append(round(flagG+(2*k-1)*flagH))
            posOfStarsY.append(round(flagE+(2*i+1)*flagF))


### drawing stars
RHO = 180 / pi
radiusOfCircle = StarK/2
canvas.setColor("white")
for j in range(len(posOfStarsX)) :
    x = []
    y = []    
    for  i in range(5) :
        teta=float((i*72+270)/RHO)
        x1 = round(posOfStarsX[j] + radiusOfCircle * cos(teta))
        y1 = round(posOfStarsY[j] + radiusOfCircle * sin(teta))
        x.append(x1)
        y.append(y1)
    canvas.drawPolygon(x[0], y[0], x[2], y[2], x[4], y[4], x[1], y[1], x[3], y[3],x[0],y[0])  



us.wait()