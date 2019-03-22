from Soda import Soda

def main():
    Pepsi = Soda("Pepsi", 10, 50)
    print(Pepsi.getName())
    print( Pepsi.__str__() )
    Pepsi.purchase()
    print(Pepsi.getQuantity() )
    print( Pepsi.__str__() )





main()