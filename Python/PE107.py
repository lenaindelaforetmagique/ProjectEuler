##Problem 107

## Kruskal


fichier=open('PE107_network.txt','r')
L=fichier.readlines()
fichier.close()

M = [[int(s) if s!='-' and s!='-\n' else 0 for s in l.split(',')] for l in L]

def aretes(graph):
    liste = []
    for i, l in enumerate(graph):
        for j, p in enumerate(l):
            if p !=0 and (p, j, i) not in liste:
                liste.append((p, i, j))
    liste.sort(key = lambda x:x[0])
    return liste


def connectes(graph, i, j, exclus=[]):
#    print("===",i,j, exclus)
    if graph[i][j] != 0:
        return True
    else:
        exclus += [i]
        ens = [k for k in range(len(graph)) if graph[i][k]!=0 and k not in exclus]
        for k in ens:
            if connectes(graph, k, j, exclus):
                return True
        return False


def poids(graph):
    l = len(graph)
    s = 0
    for i in range(l):
        for j in range(i+1, l):
            s += graph[i][j]
    return s


def ajouteArete(graph, arete):
    (p, i, j) = arete
    graph[i][j] = p
    graph[j][i] = p
    
    return graph
    


##M = [[0,16,12,21,0,0,0],
##     [16,0,0,17,20,0,0],
##     [12,0,0,28,0,31,0],
##     [21,17,28,0,18,19,23],
##     [0,20,0,18,0,0,11],
##     [0,0,31,19,0,0,27],
##     [0,0,0,23,11,27,0]]


n = len(M)

listAretes = aretes(M)
new = [[0]*n for _ in range(n)]

for (p,i,j) in listAretes:
#    print(p,i,j)
    if not connectes(new, i, j,[]):
#        print('oui')
        new = ajouteArete(new, (p,i,j))
#    else:
#        print("non")
        



#print(poids(new))
print(poids(M)-poids(new))

#print(new)





