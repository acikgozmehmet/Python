from math import pow
from sys import exit


sum=0
print("\t\t\t12345678")
bin=input("Enter the binary number:")

if len(bin) > 8 :
    exit("Error: more than 8 bits were entered. Please type 8 bits")

for i in range(len(bin)):
    #print(i,"  ",len(bin))
    j=7-i
    # print(j)
    # print(bin[j])
    num=int(bin[j])*pow(2,i)
    sum = sum + num
print(str(sum))



