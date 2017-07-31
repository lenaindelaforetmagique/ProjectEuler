##Problem 67


fichier=open('PE067_triangle.txt','r')
L=fichier.readlines()
fichier.close()

for i, l in enumerate(L):
    L[i] = [int(m) for m in l.split(' ')]


for i in range(len(L)-2, -1,-1):
    for j in range(len(L[i])):
        L[i][j] += max(L[i+1][j],L[i+1][j+1])


print(L[0][0])


