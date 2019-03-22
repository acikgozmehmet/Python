#@author Mehmet ACIKGOZ

class Soda:
    
    def __init__(self, name ="", price = 0, quantity = 0):
        self.setName(name)
        self.setPrice(price)
        self.setQuantity(quantity)
    
    
        
# mutators        
    def setName(self, name):
        self._name = name
    
    def setPrice(self, price):
        if (price > 0 ):
            self._price = price
        else:
            self._price = 0
       
    def setQuantity(self, quantity):
        if (quantity > 0):
            self._quantity = quantity
        else:
            self._quantity = 0
    
# accesors
    
    def getName(self):
        return self._name
    
    def getPrice(self):
        return self._price
    
    def getQuantity(self):
        return self._quantity


    def purchase(self, amount = 1):
        if ( (amount <= self._quantity) and (amount > 0) ):
            self._quantity = self._quantity - amount
    
    def __str__(self):
        #result = self._name + ", " + "$"+ '{0:.2f}'.format(self._price) + ", " + str(self._quantity)
        result = self._name + ", " + "$"+ str("%.2f" % self._price) + ", " + str(self._quantity)
        return result
