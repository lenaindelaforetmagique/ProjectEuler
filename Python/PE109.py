##Problem 109


simples = [i for i in range(1,21)]+[25]
doubles = [2*i for i in range(1,21)]+[2*25]
triples = [3*i for i in range(1,21)]

"""
tour12 = [0] + simples + doubles + triples #deux fois

"""

scores12 = sorted([0] + simples + doubles + triples)
l = len(scores12)


Dico12 = {}
for i in range(l):
    for j in range(i, len(scores12)):
        score = scores12[i] + scores12[j]
        if score not in Dico12:
            Dico12[score]=0
        Dico12[score] += 1

scoreMax = 100
cpt = 0
for score in Dico12.keys():
    for v in doubles:
        if v + score < scoreMax:
            cpt += Dico12[score]

print(cpt)
            


    



