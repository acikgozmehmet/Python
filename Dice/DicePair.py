#@author: Mehmet ACIKGOZ

from random import randint

class DicePair:
    def __init__(self, numSides = 6):
        self._die1 = 0
        self._die2 = 0        
        self.setTotalDoubles(0)
        self.setNumSides(numSides)
    
## mutators            
    def setTotalDoubles(self, totalDoubles):
        if (totalDoubles > 0):
            self._totalDoubles = totalDoubles
        else:
            self._totalDoubles = 0
        
        
    def setNumSides(self, numSides):
        if (numSides > 2):
            self._numSides = numSides
        else:
            self._numSides = 2
        
## accessors        
    def getDie1(self):
        return self._die1
    
    def getDie2(self):
        return self._die2
    
    def getTotalDoubles(self):
        return self._totalDoubles

    
    def roll(self):
        self._die1 = randint(1, self._numSides)
        self._die2 = randint(1, self._numSides)
        
        if (self._die1 == self._die2):
            self._totalDoubles = self._totalDoubles + 1
            