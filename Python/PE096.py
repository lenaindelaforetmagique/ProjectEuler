##Problem 96
##By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

from random import randrange

fichier=open('PE096_sudoku.txt','r')
L=fichier.readlines()
fichier.close()

#L = L.split("\n")

def genCarre(inf,sup):
    for i in range(inf, sup):
        for j in range(inf, sup):
            yield i, j

def initGrille(t):
    """ crée une grille de sudoku 9 * 9
    chaque case est de la forme :
    [ val , { valeurs possibles } ]
    """
    grille = []
    for i in range(9):
        l = [[int(c),{1,2,3,4,5,6,7,8,9}] for c in t[i] if c != '\n']
        grille.append(l)
    return grille

def copie(g):
    """ renvoie une copie de la grille"""
    t =[]
    for i in range(9):
        t.append(''.join([str(g[i][j][0]) for j in range(9)]))
    return initGrille(t)


def afficheGrille(g):
    """afficheur de grille"""
    t = []
    for i in range(9):
        if i == 3 or i == 6:
            t.append("------+-------+------")
        s = ''
        for j in range(9):
            if j == 3 or j == 6:
                s = s + '| '
            if g[i][j][0] == 0:
                c = ' '
            else:
                c = str(g[i][j][0])
            s = s + c + ' '
        t.append(s)
    print('\n'.join(t))
    print("======================")

def valPossibles(g):
    """élimine case par case les valeurs impossibles"""
    # case [i][j]
    for i, j in genCarre(0, 9):
        if g[i][j][0] != 0:
            g[i][j][1].clear()
        else:
            # balayage de la ligne
            for k in range(9):
                v = g[i][k][0]
                if v !=0 and v in g[i][j][1]:
                    g[i][j][1].remove(v)
                
            # balayage de la colonne
            for k in range(9):
                v = g[k][j][0]
                if v !=0 and v in g[i][j][1]:
                    g[i][j][1].remove(v)

            # balayage de la case 3*3
            for k, l in genCarre(0, 3):
                v = g[(i//3)*3 + k][(j//3)*3 + l][0]
                if v !=0 and v in g[i][j][1]:
                    g[i][j][1].remove(v)
    return g
                        
def algo1(g):
    """algo naif : parcours de chaque cellule inconnue
    si une seule valeur possible > on note la bonne valeur"""
    g = valPossibles(g)
    cpt = 0
    # case [i][j]
    for i, j in genCarre(0, 9):
        if g[i][j][0] == 0 and len(g[i][j][1]) == 1:
            g[i][j][0] = g[i][j][1].pop()
            cpt += 1
    return g, cpt

def algo2(g):
    """algo 2 : parcours de chaque cellule inconnue
    si dans les valeurs possibles, l'une d'elle est la seule possible
    - soit sur sa ligne
    - soit sur sa colonne
    - soit dans sa case
    > on note la bonne valeur"""
    g = valPossibles(g)
    cpt = 0 # comptient le nombre de changements effectués
    # case [i][j]
    for i, j in genCarre(0, 9):
        if g[i][j][0] == 0:
            # balayage des elements possibles
            Trouve = False # indique si la valeur V[m] n'est pas trouvée dans...
            V = [v for v in g[i][j][1]] # copie des possibilités
            m = 0
            while not Trouve and m<len(V):
                # test sur la ligne
                Trouve = True
                for k in range(9):
                    if V[m] in g[i][k][1] and k != j:
                        Trouve = False
                # test sur la colonne
                if not Trouve:
                    Trouve = True
                    for k in range(9):
                        if V[m] in g[k][j][1] and k != i:
                            Trouve = False
                # test sur la case
                if not Trouve:
                    Trouve = True
                    for k_, l_ in genCarre(0,3):
                        k, l = (i//3)*3 + k_, (j//3)*3 + l_
                        if V[m] in g[k][l][1] and (k, l) != (i, j):
                            Trouve = False
                m += 1
            if Trouve:
                m -= 1
                g[i][j][0]=V[m]
                g[i][j][1].clear()
                cpt += 1
                g = valPossibles(g) # actualisation des valeurs possibles
    return g, cpt

def algo3(g):
    """algo 3 : parcours de chaque cellule inconnue
    si une case contient seulement 2 possibilités :
    - recherche d'une case voisine qui contient les memes possibilités
    - suppression des apparitions des valeurs possibles dans les voisines
    """
    g = valPossibles(g)
    cpt = 0 
    # case [i][j]
    for i, j in genCarre(0, 9):
        if len(g[i][j][1]) == 2: # case à seulement 2 possibilités
            t1=[v for v in g[i][j][1]]
            t1.sort()

            # test sur la ligne
            for k in range(9):
                if len(g[i][k][1]) == 2 and k != j:
                    t2 = [v for v in g[i][k][1]]
                    t2.sort()
                    if t1 == t2:
                        # suppression des apparitions voisines
                        for q in [_ for _ in range(9) if _!=k and _!=j]:
                            if t1[0] in g[i][q][1]:
                                g[i][q][1].remove(t1[0])
                                cpt += 1
                            if t1[1] in g[i][q][1]:
                                g[i][q][1].remove(t1[1])
                                cpt += 1

            # test sur la colonne
            for k in range(9):
                if len(g[k][j][1]) == 2 and k != i:
                    t2 = [v for v in g[k][j][1]]
                    t2.sort()
                    if t1 == t2:
                        # suppression des apparitions voisines
                        for q in [_ for _ in range(9) if _!=k and _!=i]:
                            if t1[0] in g[q][j][1]:
                                g[q][j][1].remove(t1[0])
                                cpt += 1
                            if t1[1] in g[q][j][1]:
                                g[q][j][1].remove(t1[1])
                                cpt += 1

            # test sur la case
            for k_, l_ in genCarre(0, 3):
                k, l = (i//3)*3 + k_, (j//3)*3 + l_
                if len(g[k][l][1]) == 2 and (k, l) != (i, j):
                    t2 = [v for v in g[k][l][1]]
                    t2.sort()
                    if t1 == t2:
                        # suppression des apparitions voisines
                        for q_, r_ in genCarre(0, 3):
                            q, r = (i//3)*3 + q_, (j//3)*3 + r_
                            if (t1[0] in g[q][r][1]) and (q, r)!=(i,j) and (q,r)!=(k,l):
                                g[q][r][1].remove(t1[0])
                                cpt += 1
                            if (t1[1] in g[q][r][1]) and (q, r)!=(i,j) and (q,r)!=(k,l):
                                g[q][r][1].remove(t1[1])
                                cpt += 1
    return g, cpt

def algo4(g):
    """algo 4 : force brute
    trouve une case avec peu de possibilités et essaie d'éliminer les cas"""
    # recherche de la 'bonne' case

    bonneCase = False
    nbre = 2
    
    g = valPossibles(g)
    casesVides = []
    for i, j in genCarre(0, 9):
        if g[i][j][0] == 0:
            casesVides.append((i,j))

    aleat = randrange(len(casesVides))
    i_, j_ = casesVides[0] #aleat]

##    while not bonneCase:
##        for i, j in genCarre(0, 9):
##            if not bonneCase and g[i][j][0] == 0 and len(g[i][j][1]) == nbre:
##                i_, j_ = i, j
##                bonneCase = True
##        nbre +=1

    OK = False
    k = 0
    t = [v for v in g[i_][j_][1]]
    while not OK and k<len(t):
#        print(len(casesVides), k)
        g2 = copie(g)
        g2[i_][j_][0] = t[k]
#        print(i_, j_,':', t[k])
        g2, OK = resous(g2)
        OK = estResolue(g2) and pasErreur(g2)
#        print(i_, j_,':', t[k], OK)
        k += 1

    if OK:
        return g2
    else:
        # retourne ce cas si la grille g n'est pas resoluble
        return g
        


def estResolue(g):
    """vérifie si la grille est pleine"""
    for i, j in genCarre(0, 9):
        if g[i][j][0] == 0:
            return False
    return True

def pasErreur(g):
    """vérifie :
    pas de doublon
    pas de case avec aucune possibilité
    """
    test = True

    # case vide impossible
    for i, j in genCarre(0, 9):
        if g[i][j][0] == 0 and len(g[i][j][1])==0:
            test = False

    # doublons sur ligne
    for i in range(9):
        s = ''.join([str(g[i][j][0]) for j in range(9) if g[i][j][0]!=0])
        for c in s:
            if s.count(c)>1:
                test = False
    
    # doublons sur colonne
    for j in range(9):
        s = ''.join([str(g[i][j][0]) for i in range(9) if g[i][j][0]!=0])
        for c in s:
            if s.count(c)>1:
                test = False

    # doublons dans case
    for i_, j_ in genCarre(0, 3):
        i, j = i_*3, j_*3
        s = ''.join([str(g[i+k][j+l][0]) for k, l in genCarre(0, 3) if g[i+k][j+l][0]!=0])
        for c in s:
            if s.count(c)>1:
                test = False
        
    return test


def resous(g):
    """résout la grille de sudoku
    renvoit la grille et
    True si succès
    False si echec"""
    cpt = 1
    fini = False
    grilleOK = True
    while not fini and grilleOK and cpt !=0:
        cpt = 0
        # méthode 1
        p = 1
        while p != 0:
            g, p = algo1(g)
            cpt += p
        # méthode 2
        if not estResolue(g):
            p = 1
            while p !=0:
                g, p = algo2(g)
                cpt += p
        # méthode 3
        if not estResolue(g) and cpt == 0:
            p = 1
            while p !=0:
                g, p = algo3(g)
                cpt += p

        # méthode 4
        if not estResolue(g) and cpt == 0:
            g = algo4(g)
        
        # place pour d'autres méthodes de résolution
        # ...
        fini = estResolue(g)
        grilleOK = pasErreur(g)
        
    return g, grilleOK



##
##s = 0
##for n in range(1,51):
##    print("\n*** Grille n°{} :".format(n))
##    grille = initGrille(L[(n-1)*10+1:n*10])
##    grille, test = resous(grille)
##    s += grille[0][0][0]*100 + grille[0][1][0]*10 + grille[0][2][0]
##    print(test)
##
##print(s)
#    afficheGrille(grille)

fichier=open('sudoku_tres_difficiles.txt','r')
L=fichier.readlines()
fichier.close()

for i in range(2): #len(L)):
    print("Grille n°{}".format(i+1))
    L[i] = L[i].replace('.','0')
    t=[L[i][9*j:9*(j+1)] for j in range(9)]
    g = initGrille(t)
    afficheGrille(g)
    g, test = resous(g)
    afficheGrille(g)
    print(pasErreur(g), estResolue(g))

### grille vide
##t = '0'*81
###t = "735609010140700650009514070051208040902050300087301095094806100073005960016073520"
##t=[t[9*j:9*(j+1)] for j in range(9)]
###print(t)
##g = initGrille(t)
##afficheGrille(g)
##g, test = resous(g)
##afficheGrille(g)





    
