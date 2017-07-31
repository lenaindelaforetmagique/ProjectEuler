"""Problem 79

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""


fichier=open('PE079_keylog.txt','r')
lignes=fichier.readlines()
fichier.close()

lignes=[s[:-1] for s in lignes]


def test_key(passcode, key):
    p1 = passcode.find(key[0])
    p2 = passcode.find(key[1], max(0,p1))
    p3 = passcode.find(key[2], max(0,p2))
    return [p1, p2, p3]

passcode = lignes.pop()
lK = 3

posMin={}
posMax={}

while len(lignes)>0:
    key = lignes.pop(0)
    print('*',passcode,key,len(lignes))
    pos = test_key(passcode, key)
    if -1 in pos:
        t = [c for i, c in enumerate(key) if pos[i]==-1] # tables des non-trouves
        
        for c in t:
            # création des instances dans la table min/max
            if c not in posMin:
                posMin[c]=-1
            if c not in posMax:
                posMax[c]=len(passcode)
                            
        for i, c in enumerate(key[:-1]):
            #cas des posMax
            if pos[i]==-1 and pos[i+1]!=-1:
                posMax[c] = min(posMax[c], pos[i+1])    

        for i, c  in enumerate(key[1:]):
            j = i + 1 # i contient une position de la tranche de key[1:]
            #cas de posMin
            if pos[j]==-1 and pos[j-1]!=-1:
                posMin[c] = max(posMin[c], pos[j-1])

        insertion = False
        i = 0
        while not insertion and i<len(t):
            if posMax[t[i]]-posMin[t[i]] == 1:
                insertion = True
                passcode = passcode[:posMin[t[i]]+1] + t[i] + passcode[posMax[t[i]]:]
                posMin.clear()
                posMax.clear()
            i+=1

        lignes.append(key)
              
            

print(passcode)
