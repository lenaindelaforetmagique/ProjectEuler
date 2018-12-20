##Problem 78
##
##Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
##OOOOO
##OOOO   O
##OOO   OO
##OOO   O   O
##OO   OO   O
##OO   O   O   O
##O   O   O   O   O
##
##Find the least value of n for which p(n) is divisible by one million.

from time import time
t0 = time()

mem = {}
mem[0] = 1

def p(n):
    """génération des partitions d'un nombre grace à la récurrence
    sur les nombres pentagonaux d'Euler"""
    if n in mem:
        return mem[n]
    else:
        s = 0
        k = 1      
        nb1 = (n-k*(3*k+1)//2)
        while nb1 >= 0:
            s += p(nb1)*(-1)**(k-1)
            k += 1
            nb1 = (n-k*(3*k+1)//2)
            
        k = 1
        nb2 = (n-k*(3*k-1)//2)
        while nb2 >= 0:
            s += p(nb2)*(-1)**(k-1)
            k += 1
            nb2 = (n-k*(3*k-1)//2)
        
        mem[n] = s
        return s

    
i = 1
while p(i)%10**6 != 0:
    i += 1

print("-->",i)#,p(i))
print(time()-t0)


##
##def partition(n, k):
##    if (n,k) in mem:
##        return mem[(n,k)]
##    elif n < k:
##        return 0
##    elif n == k or k == 1:
##        return 1
##    else:
##        mem[(n,k)] = partition(n-1, k-1) + partition(n-k, k)
##        return mem[(n,k)]

##def main(n):
##    s = 0
##    for k in range(1,n+1):
##        s += partition(n, k)
##    return s
    
    
