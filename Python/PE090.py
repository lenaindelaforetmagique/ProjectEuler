##Problem 90

liste = []

def combi(n, k, p=0, t=[]):
    global liste
    if len(t) == 0:
        t = [0]*k

    for i in range(p, n-k+1):
        t[-k] = i
        if k == 1:
            liste.append(t[:])
        else:
            combi(n, k-1, i+1, t)

combi(10,6)

for t in liste:
    if 6 in t and 9 not in t:
        t.append(9)
    if 9 in t and 6 not in t:
        t.append(6)

def verif(de1, de2):
    jeu = set()
    for v1 in de1:
        for v2 in de2:
            jeu.add(v1*10+v2)
            jeu.add(v2*10+v1)
    test = True
    for i in range(1,10):
        if i**2 not in jeu:
            test = False
    return test

    
cpt = 0
for t1 in liste:
    for t2 in liste:
        if verif(t1, t2):
            cpt += 1
        
    
print(cpt//2)

