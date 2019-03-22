def createMatrix(rows,columns):
    matrix = []
    for i in range(rows):
        row = ['-']*columns
        matrix.append(row)
    return matrix

def printMatrix(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end = " ")
        print()
        
def changePlayer(player, A):
    row = int(input("Row :"))
    col = int(input("Column"))
    A[row][col] = player
    printMatrix(A)


def main():
    A = createMatrix(3,3)
    printMatrix(A)
    
    isOver = False
    
    while( not isOver):
        changePlayer('X',A)
        if checkMatrix(A, 'X'):
            print("X wins")
            isOver = True
            
        changePlayer('O',A)
        if checkMatrix(A, 'O'):
            print("O wins")
            isOver = True
 
        
        #isOver = True  # check the A if a winner
    
def checkMatrix(matrix, player):
    total3 = 0
    for i in range(len(matrix)):
        total1 = 0
        total2 = 0
        
        if (matrix[i][i] == player):
            total3 = total3 + 1
            
        for j in range(len(matrix[0])):
            if (matrix[i][j] == player) :
                total1 = total1 + 1
            
            if (matrix[j][i] == player) :
                total2 = total2 + 1           

    if (total1 == 3 or total2 == 3 or total3 ==3):
        return True
    else:
        return False
    
main()


