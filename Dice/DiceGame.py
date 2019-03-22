#@author: Mehmet ACIKGOZ

from DicePair import DicePair

def main():
    player1 = DicePair()
    player2 = DicePair()
    
    for i in range(10):
        player1.roll()
        player2.roll()
        
        print("Player1 rolled:", player1.getDie1(), end = ", ")        
        print(player1.getDie2())
        if ( player1.getDie1() == player1.getDie2()) :
            print("%s" %("  Double rolled for player 1") )           

        print("Player2 rolled:", player2.getDie1(), end = ", ")
        print(player2.getDie2())
        if ( player2.getDie1() == player2.getDie2()) :
            print("%s" %("  Double rolled for player 2") )    
            
        print()
            
            
    print("Player 1 total doubles:", player1.getTotalDoubles())
    print("Player 2 total doubles:", player2.getTotalDoubles())
    
    if ( player1.getTotalDoubles() > player2.getTotalDoubles() ):
        print("Player 1 wins!")
    elif ( player1.getTotalDoubles() < player2.getTotalDoubles() ):
        print("Player 2 wins!")
    else:
        print("Tie!")
        

main()
        
    