from ezgraphics import GraphicsWindow 
from math import *
from random import randint







def configureWindow(winSize):
        
    win = GraphicsWindow(winSize, winSize)
    canvas = win.canvas()
    #canvas.setFill("red")     
    canvas.setBackground(0, 128, 0)
    return canvas

## Prompt the user as to whether they want to roll again or quit. 
#  @return True if the user wants to roll again
def rollAgain() :
    userInput = input("Press the Enter key to roll again or enter Q to quit: ")
    if userInput.upper() == "Q" :
        return False  
    else :
        return True




def rollDice(canvas, size):
    print(" In the function rollDice now")
    #canvas.clear()
    
    xOffset = size
    yOffset = size
    
    for die in range(5):
        dieValue = randint(1, 6)
        drawDie(canvas, xOffset, yOffset, size, dieValue)
        if die == 2 :
            xOffset = size * 2
            yOffset = size * 3
        else:
            xOffset = xOffset + size * 2
            
        
## Draws a single die on the canvas.
#  @param canvas the canvas on which to draw the die
#  @param x the x-coordinate for the upper-left corner of the die 
#  @param y the y-coordinate for the upper-left corner of the die 
#  @param size an integer indicating the dimensions of the die 
#  @param dieValue an integer indicating the number of dots on the die 
#
def drawDie(canvas, x, y, size, dieValue):    
    dotSize = size // 5
    offset1 = dotSize // 2
    offset2 = dotSize // 2 * 4
    offset3 = dotSize // 2 * 7
    
    canvas.setFill("white")
    canvas.setOutline("black")
    canvas.setLineWidth(2)
    canvas.drawRect(x, y, size, size)
    
    # Set the color used for the dots.
    canvas.setColor("black")
    canvas.setLineWidth(1)
      # Draw the center dot or middle row of dots, if needed.
    if dieValue == 1 or dieValue == 3 or dieValue == 5 :
        canvas.drawOval(x + offset2, y + offset2, dotSize, dotSize)        
    elif dieValue == 6 :
        canvas.drawOval(x + offset1, y + offset2, dotSize, dotSize)
        canvas.drawOval(x + offset3, y + offset2, dotSize, dotSize)
      
    # Draw the upper-left and lower-right dots, if needed.   
    if dieValue >= 2 :
        canvas.drawOval(x + offset1, y + offset1, dotSize, dotSize)
        canvas.drawOval(x + offset3, y + offset3, dotSize, dotSize)
        
    # Draw the lower-left and upper-right dots, if needed.
    if dieValue >= 4 :
        canvas.drawOval(x + offset1, y + offset3, dotSize, dotSize)
        canvas.drawOval(x + offset3, y + offset1, dotSize, dotSize)
    




def insideButton(clickx, clicky):
        if (clickx <= (DIE_SIZE * 7) ) and (clicky <= (DIE_SIZE * 7)):
                return True
        else:
                return False                
            

DIE_SIZE = 50

def main() :
    goOn = True
    player = 1
    win = GraphicsWindow(DIE_SIZE * 8, DIE_SIZE * 8)
    canvas = win.canvas()
    #canvas.setFill("red")     
    canvas.setBackground(0, 128, 0)    
    #canvas.setFont(20)
    #canvas.getAvailableFonts()
    
    
    #canvas = configureWindow(DIE_SIZE * 7)
    #rollDice(canvas, DIE_SIZE)


    HOWMANY = 10
    
    cnt = 0
    player1Scores=[]
    player2Scores=[]


    while cnt < HOWMANY :        
            
            initilizeScreen(win, canvas, cnt)
            player = 1        
            #print(player)            
            #clickx, clicky = win.getMouse()  
            #canvas.setBackground(0, 128, 0)    
            #canvas.clear()
            canvas.setColor(0,0,0)            
            canvas.setTextFont("arial", "bold", 15)            
            canvas.drawText(DIE_SIZE*3/2, DIE_SIZE*1,"Yourself")     
            canvas.setTextFont("arial", "bold", 40)            
            run=randint(1,6)
            drawDie(canvas, DIE_SIZE*3/2, DIE_SIZE*4, DIE_SIZE,run)
            canvas.setBackground(0, 128, 0)
            player1Scores.append(run)
            scoreboardClean(canvas,player)
            sumPlayer1Scores = str(sum(player1Scores))  
            canvas.drawText(DIE_SIZE*3/2, DIE_SIZE*2, sumPlayer1Scores )
            win.sleep(900)       
                        
        ### player 2 
            player = 2
            #print(player)
            canvas.setTextFont("arial", "bold", 15)          
            canvas.drawText(DIE_SIZE*4.5, DIE_SIZE*1, "Computer")
            canvas.setTextFont("arial", "bold", 40)
            run=randint(1,6)            
            drawDie(canvas, DIE_SIZE*5, DIE_SIZE*4, DIE_SIZE,run)
            player2Scores.append(run) 
            scoreboardClean(canvas,player)            
            sumPlayer2Scores = str(sum(player2Scores))              
            canvas.drawText(DIE_SIZE*5, DIE_SIZE*2, sumPlayer2Scores)
            
        ### increment the iteratuion    
            cnt = cnt + 1
            
            if (cnt == HOWMANY) :
                reportScore(canvas, whoIsWinner(sumPlayer1Scores, sumPlayer2Scores))
    
                win.sleep(3000)  
                #print(terminateGame(win, canvas))
    
                if terminateGame(win, canvas):
                    #win.close()
                    win.quit()
                else:
                    cnt = 0
                    player1Scores=[]
                    player2Scores=[] 
                    canvas.clear()
                    
                    #initilizeScreen(win, canvas, cnt)
                    #canvas.clear()
                    #canvas.setColor("red")        
                    #canvas.setTextFont("arial", "bold", 20)  
                    #canvas.drawText(DIE_SIZE*3/2, DIE_SIZE*2, " Click to start !")      
        
               
                
                
    
    
    #win.close()
        
def initilizeScreen(win, canvas, cnt):
    if (cnt == 0) :
        canvas.clear()
        canvas.setColor("red")        
        canvas.setTextFont("arial", "bold", 20)  
        canvas.drawText(DIE_SIZE*2, DIE_SIZE*3, " Roll a dice ? ")       
        canvas.drawText(DIE_SIZE*2, DIE_SIZE*5, " Click to start !")      
        clickx, clicky = win.getMouse()  
        canvas.clear()                
    else:
        clickx, clicky = win.getMouse()          
        
        
def terminateGame(win, canvas):
    canvas.setOutline(0,128,0)            
    #canvas.setFill(255,128,0)     
    canvas.drawRect(DIE_SIZE*3/2, DIE_SIZE*6, DIE_SIZE*5.5, DIE_SIZE*2)
    canvas.setColor("red")
    canvas.setTextFont("arial", "bold", 20)         
    canvas.drawText(DIE_SIZE*3.5, DIE_SIZE*6, "Exit ?")

    ## Yes
    canvas.setOutline(0,0,0)
    canvas.setFill(0,128,0)       
    canvas.drawRect(DIE_SIZE*3/2, DIE_SIZE*6.70, DIE_SIZE*1.5, DIE_SIZE*0.75)
    canvas.setColor("red")
    canvas.setTextFont("arial", "bold", 20)         
    canvas.drawText(DIE_SIZE*3/2, DIE_SIZE*6.75, "  Yes ")
    
    ## No
    canvas.setOutline(0,0,0)
    canvas.setFill(0,128,0)       
    canvas.drawRect(DIE_SIZE*5, DIE_SIZE*6.70, DIE_SIZE*1.5, DIE_SIZE*0.75)
    canvas.setColor("red")
    canvas.setTextFont("arial", "bold", 20)         
    canvas.drawText(DIE_SIZE*5, DIE_SIZE*6.75, "  No ")   
    
    ## test 
    clickx, clicky = win.getMouse()  
    #print(testExit(clickx,clicky))
    if (testExit(win, clickx, clicky)):
        return True
    else: 
        return False
            
                                          
                                          
                                          
    
    
    
    
            
            
            
        
        

'''        
    userInput=input("devam")
    while (userInput[0].lower() !='n'):
        print(win.getMouse())
        drawDie(canvas, 10, 10, 60, randint(1,6))
        win.sleep(1000)
        userInput=input("devam")

    win.wait()
'''
    #clear()
    #    userInput=input("devam")
    
    #while rollAgain() :
    #    print(rollAgain())
    #    rollDice(canvas, DIE_SIZE)

def scoreboardClean(canvas, player):
    # It is for the scoreboard which is above the dice. It cleans the board after each rolling            
    canvas.setOutline(0,128,0)            
    canvas.setFill(0,128,0)     
    if player == 1 :
        canvas.drawRect(DIE_SIZE*3/2, DIE_SIZE*2, DIE_SIZE*2, DIE_SIZE)
    else:
        canvas.drawRect(DIE_SIZE*5, DIE_SIZE*2, DIE_SIZE*2, DIE_SIZE)
    canvas.setOutline(0,0,0) 
    
def reportScore(canvas, winner):
    canvas.setTextFont("arial", "bold", 20)        
    if (winner == 1) :
        canvas.drawText(DIE_SIZE*2, DIE_SIZE*6, "You Win !")    
    elif (winner == 2 ):
        canvas.drawText(DIE_SIZE*2, DIE_SIZE*6, "Computer Wins !")  
    else:
        canvas.drawText(DIE_SIZE*2, DIE_SIZE*6, "It is a tie !")  
    
def whoIsWinner(score1, score2):
    if (int(score1) > int(score2)):
        winner = 1 
    elif (int(score2) > int(score1)) :
        winner = 2
    else :
        winner = 0
    return winner

### bunu butona denk gelecek sekilde ayarlamak lazim
def testExit(win, clickx,clicky):        
    temp = 1
    while temp :
        if (clickx >= DIE_SIZE*3/2) and (clickx <= (DIE_SIZE*3/2 + DIE_SIZE*1.5)) :
            if (clicky >= DIE_SIZE*6.70) and (clicky <= (DIE_SIZE*6.70+DIE_SIZE*0.75)) :
                return True
        if (clickx >= DIE_SIZE*5) and (clickx <= (DIE_SIZE*5+ DIE_SIZE*1.5)) :
            if (clicky >= DIE_SIZE*6.70) and (clicky <= (DIE_SIZE*6.70+DIE_SIZE*0.75)) :
                return False
        clickx, clicky = win.getMouse() 


main()