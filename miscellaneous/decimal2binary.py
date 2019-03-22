from math import pow

number=int(input("Enter a decimal number"))

bin=[]
#bin="10000000"
#print(bin[0])
for i in range(0,8):
#    print(i, "  ", number)
#    print(number)
    j=7-i
    if  number >= pow(2,j):
        number = number - pow(2,j)
        #bin[i]='1'
        bin.append(1)
    else:
        #bin[i] = 0
        bin.append(0)
        
print(bin)

        
    
    
        
