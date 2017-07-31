##Problem 99
##Published on Friday, 1st July 2005, 07:00 pm; Solved by 22426; Difficulty rating: 10%
##
##Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.
##
##However, confirming that 632382**518061 > 519432**525806 would be much more difficult, as both numbers contain over three million digits.
##
##Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
##
##NOTE: The first two lines in the file represent the numbers in the example given above.

from math import *


fichier=open('PE099_base_exp.txt','r')
L=fichier.readlines()
fichier.close()

#l = [[int(c),{1,2,3,4,5,6,7,8,9}] for c in t[i] if c != '\n']


vMax = 0
iMax = 0
for i, l in enumerate(L):
    t = l.split(',')
    a, b = int(t[0]), int(t[1])
#    print(b * log(a))
    if b * log(a) > vMax:
        vMax = b * log(a)
        iMax = i

print(iMax+1)
    
    
