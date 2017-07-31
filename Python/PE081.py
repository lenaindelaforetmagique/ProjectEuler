##Problem 81
##
##In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
##
##Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.


fichier=open('PE081_matrix.txt','r')
L=fichier.readlines()
fichier.close()

for i, l in enumerate(L):
    L[i] = [int(m) for m in l.split(',')]

b = len(L[0]) #base de numérotation et largeur de la matrice
h = len(L) # hauteur de la matrice

L_u = {} #liste des noeuds non visités
en_cours = {}
traites = {}

en_cours['D'] = [0, [[0,L[0][0]]]]

infini = 80*80*9999

for i, l in enumerate(L):
    for j, c in enumerate(l):
        voisins = []
        if i<h-1:
            voisins.append([(i+1)*b+j, L[i+1][j]])
        if j<b-1:
            voisins.append([i*b+j+1, L[i][j+1]])
        L_u[i*b+j] = [infini, voisins]



while len(en_cours)>0:
    distMini = infini
    clefMini = -1
    #1 recherche du plus proche noeud
    for n in en_cours:
        if en_cours[n][0] < distMini:
            distMini = en_cours[n][0]
            clefMini = n

    current = en_cours.pop(clefMini)

    #2 balayge de ses voisins
    for (num, dist) in current[1]:
        if num in L_u:
            en_cours[num] = L_u.pop(num)

        if num in en_cours:
            en_cours[num][0] = min(en_cours[num][0], current[0] + dist)

    #3 stockage du courant :
    traites[clefMini] = current

print(traites[80*79+79])
            



