"""Problem 206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""

from time import time
from math import *



def test(j):
    return "1234567890"==str(j)[::2]


def prog():
    #s="1_2_3_4_5_6_7_8_9_0"
    #n=int("0".join(s.split("_")))
    n=1020304050607080900

    chif=4
    solution=[]

    s=0
    for i in range(1,10**chif):
        n1=int("".join([c+"0" for c in str(i)]))*10**(18-2*chif)

        n2=n1+int("90"*(9-chif))
        for j in range(floor(sqrt(n+n1)),ceil(sqrt(n+n2))):
            if test(j**2):
                solution.append(j)
                
    return solution


t1=time()
for i in range(20):
    a=prog()
    
print((time()-t1)/20,a)
        

