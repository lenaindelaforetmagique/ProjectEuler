##PE106

from itertools import combinations
from time import time
t0 = time()


n = 15
val = [i for i in range(n)]
cpt = 0
for i in range(2, n//2+1):
    for B in combinations(val, i):
        val2 = [v for v in val if v not in B]
        for C in combinations(val2,i):
            s = sum([int(B[j]>C[j]) for j in range(i)])
            cpt += int(s !=0 and s!=i)

print(cpt//2)
print(time()-t0)
    
t0 = time()
def verif(t1, t2):
    l = len(t1)
    s = sum([int(t1[j]>t2[j]) for j in range(l)])
    return s == 0 or s == l


val = [i for i in range(n)]
cpt = 0
for i in range(2, n//2+1):
    for B in combinations(val, i):
        val2 = [v for v in val if v not in B]
        for C in combinations(val2,i):
            if not verif(B, C):
                cpt += 1
            

            

print(cpt//2)
print(time()-t0)






