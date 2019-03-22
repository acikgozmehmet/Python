# trflag.py
# @author Mehmet ACIKGOZ
# This program displays Turkish flag
# Date:08/22/2017


from ezgraphics import GraphicsWindow 
from math import *


flagWidth = int(input("Please enter the width of the flag eg. 100 : "))
flagLength = 1.5 * flagWidth
flagA = 0.5 * flagWidth
flagB = 0.5 * flagWidth
flagC = 1/16 * flagWidth
flagD = 0.4 * flagWidth
flagE = 1/3 * flagWidth
flagF = 1/4 * flagWidth


win = GraphicsWindow(flagLength,flagWidth) 
win.setTitle("Turkish Flag")
canvas = win.canvas() 
#canvas.title('Turkish Flag')
canvas.setFill("red")  
canvas.drawRect(0, 0, flagLength, flagWidth) 

canvas.setOutline(255, 255, 255)
canvas.setFill(255, 255, 255) 
canvas.drawOval((flagA-flagB/2), (flagWidth/2-flagB/2), flagB, flagB) 

canvas.setOutline("red")
canvas.setFill("red") 
canvas.drawOval(flagA+flagC-flagD/2, flagWidth/2-flagD/2, flagD, flagD) 

# Center of the star circle
#starPoint1x=flagA+flagC-flagD/2+flagE
#starPoint1y=flagWidth/2
centerOfCircleX = flagA+flagC-flagD/2+flagE + flagF/2
centerOfCircleY = flagWidth/2 


RHO = 180 / pi
radiusOfCircle = flagF/2
x = []
y = []

for  i in range(5) :
    teta=float((i*72+270)/RHO)
    x1 = round(centerOfCircleX + radiusOfCircle * cos(teta))
    y1 = round(centerOfCircleY + radiusOfCircle * sin(teta))
    x.append(x1)
    y.append(y1)
#    print("x=", x[i], "  y= ", y[i])
 
canvas.setOutline(255,255, 255)    
canvas.setFill(255, 255, 255) 
canvas.drawPolygon(int(x[0]), int(y[0]), int(x[2]), int(y[2]), int(x[4]), int(y[4]), int(x[1]), int(y[1]), int(x[3]), int(y[3]),int(x[0]),int(y[0]))   

win.wait() 

