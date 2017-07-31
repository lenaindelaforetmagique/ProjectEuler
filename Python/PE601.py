##Problem 601
##
##For every positive number n
##we define the function streak(n)=k as the smallest positive integer k such that n+k is not divisible by k+1.
##E.g:
##13 is divisible by 1
##14 is divisible by 2
##15 is divisible by 3
##16 is divisible by 4
##17 is NOT divisible by 5
##So streak(13)=4.
##Similarly:
##120 is divisible by 1
##121 is NOT divisible by 2
##So streak(120)=1
##
##.
##
##Define P(s,N)
##to be the number of integers n, 1<n<N, for which streak(n)=s.
##So P(3,14)=1 and P(6,106)=14286
##
##.
##
##Find the sum, as i
##ranges from 1 to 31, of P(i,4**i). 


from arithmetique import *

"""
pgcd( n+k, k+1) = 1

(n+k) = (k+1)*p +1


observations:
pair > 1
2 4 8 10 16  > 2
6*k+1 > 3
12*k+1 > 4

60*k+1 > 6
60*7+1 > 7


aucun ? > 5, 9, 11, 13
"""
##
##def streak(n):
##    k = 1
##    while (n+k)%(k+1) == 0:
##        k += 1
##    return k



def P(s, N):
    ppcm1 = ppcm_L([i for i in range(1, s+1)])
    ppcm2 = ppcm_L([i for i in range(1, s+2)])
    if ppcm1 == ppcm2:
        return 0
    else:
        #print(s, N, ppcm1, ppcm2)
        return (N-2)//ppcm1-(N-2)//ppcm2


##print(P(3,14))
##print(P(6,10**6))


S = 0
for i in range(1, 32):
    print(i, P(i, 4**i))
    S += P(i, 4**i)


print(S)
    
