## @author Mehmet ACIKGOZ
# This program simulates a simple game of Tic-Tac-Toe
def main():
    MAX_TURNS = 9
    turnsTaken = 0
    isWinner = False
    board = createBoard()
    player = "O"
    
    while (not isWinner and turnsTaken < MAX_TURNS) :
        # Switch players 
        # (If player contained an O assign an "X", else assign an "O")
        if (player == 'O'):
            player = 'X'
        elif (player == 'X'):
            player = 'O'
        
        # Show the board (Call the showBoard function)
        showBoard(board)

        
        # Prompt for and retrieve the row and column for the player
        # (Be sure to match the output)
        print("\nPlayer %s's turn " % player)
        r = int(input("Row: "))
        c = int(input("Col: "))
        
        ## to prevent the over-write of a previously placed X or O.
        ##  to prevent the input of an out-of-bounds row or column 
        while ((r > 3 or r < 1) or (c > 3 or c <1) or board[r-1][c-1] != '-'):
            r = int(input("Row: "))
            c = int(input("Col: "))
           
       
        # Place the X or O on the board (Hint: use the value of player)
        ## This will allow the user to enter row and column values they are accustomed to
        ## ie: The first elements are 1 and 1
        r = r-1
        c = c-1

        board[r][c] = player
 
        # Increment # of turns and check for win (completed)
        turnsTaken = turnsTaken + 1
        isWinner = checkWin(board, player)
    
    # Game is now over, so show the final board (Call showBoard function)
    showBoard(board)
    
    # Display who won or if it was a cat. (Match the output)
    if turnsTaken == MAX_TURNS:
        print("Cat!")
    else:
        print("%s wins!" % player)
    

        
# showBoard shows a tic tac toe board in a table format
# @param board The tic tac toe board
def showBoard(matrix):
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end = " ")
        print()


# createBoard creates a 3x3 tic-tac-toe board 
# where each element is a dash
# @return the created board
def createBoard():
    A = []
    for i in range(3):
        row = ['-']*3
        A.append(row)
    return A



# checkWin determines if a win occurred in a row, column, or diagonal
# @param board The Tic-Tac-Toe board
# @param player Contains an "X" or "O" representing a player
# @return True or False depending if the game is won 
def checkWin(board,player):
    for i in range(3):
        if (player == board[i][0] == board[i][1] == board[i][2]): 
            return True
        if (player == board[0][i] == board[1][i] == board[2][i]):
            return True
    
    if (player == board[0][0] == board[1][1] == board[2][2]) :
        return True
    
    if(player == board[2][0] == board[1][1] == board[0][2]):
        return True
            
    
main()