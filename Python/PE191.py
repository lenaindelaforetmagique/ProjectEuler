##Problem 191
##
##A particular school offers cash rewards to children with good attendance and punctuality. If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.
##
##During an n-day period a trinary string is formed for each child consisting of L's (late), O's (on time), and A's (absent).
##
##Although there are eighty-one trinary strings for a 4-day period that can be formed, exactly forty-three strings would lead to a prize:
##
##OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
##OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
##AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
##AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
##LAOO LAOA LAAO
##
##How many "prize" strings exist over a 30-day period?

"""

"""


def fact(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

def C_n_k(n, k):
    return fact(n)//(fact(k)*fact(n-k))

def anag(t):
    """Nombre d'anagrammes"""
    num = fact(sum(t))
    den = 1
    for v in t:
        den *= fact(v)
    return num//den
    

Ltot = 30
arr = 0
# Boucle sur le nombre de AA
for k1 in range(0, (Ltot+1)//(2+1)+1):
    # Boucle sur le nombre de A
    for k2 in range(0, (Ltot+1-(2+1)*k1)//(1+1)+1):
        nbLibres = Ltot-2*k1-1*k2
        arr += C_n_k(nbLibres+1, k1+k2)*anag([k1, k2])*(1+nbLibres)
        # k1+k2 blocs à répartir sur nbLibres+1 intervalles
        # anag(k1 k2)
        # 1+nbLibres : nb de cas pour L (+1 car peut ne pas se produire)

print(arr)

##from time import time
##
##def bruteForce(S, lmax):
##    if len(S)<lmax:
##        if len(S)>1:
##            if S[-1]!='A' or S[-2]!='A':
##                bruteForce(S+'A', lmax)
##        else:
##            bruteForce(S+'A', lmax)
##    
##        if 'L' not in S:
##            bruteForce(S+'L', lmax)
##        
##        bruteForce(S+'O', lmax)
##
##    else:
##        global cpt
##        cpt += 1
##
##l = 1
##
##while l<=30:
##    t0 = time()
##    cpt = 0
##    bruteForce('',l)
##    print(l, cpt, time()-t0)
##    l += 1
##1 3 0.0
##2 8 0.0
##3 19 0.0
##4 43 0.0
##5 94 0.0
##6 200 0.0
##7 418 0.0
##8 861 0.0
##9 1753 0.015600442886352539
##10 3536 0.0
##11 7077 0.0
##12 14071 0.01560068130493164
##13 27820 0.04680132865905762
##14 54736 0.04680156707763672
##15 107236 0.09360313415527344
##16 209305 0.2028064727783203
##17 407167 0.5772185325622559
##18 789720 0.9048290252685547
##19 1527607 1.60685133934021
##20 2947811 3.354107618331909
##21 5675882 6.411805629730225
##22 10906776 12.246392488479614
##23 20920006 23.22914433479309
##24 40058421 46.832700967788696
##25 76585973 89.40027236938477
##26 146210464 169.4068295955658
##27 278757449 325.03803181648254
##28 530803311 613.2004585266113
        
        


