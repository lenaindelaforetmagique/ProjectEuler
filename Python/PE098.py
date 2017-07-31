##Problem 98
##
##By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.
##
##Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).
##
##What is the largest square number formed by any member of such a pair?
##
##NOTE: All anagrams formed must be contained in the given text file.

fichier=open('PE098_words.txt','r')
L=fichier.readlines()
fichier.close()
L = "".join(L[0].split('"')).split(',')

dico_mots = {}
for l in L:
    clef = ''.join(sorted(l))
    if clef not in dico_mots:
        dico_mots[clef] = []
    if l not in dico_mots[clef]:
        dico_mots[clef].append(l)

dico_anag = {}
lMax = 0
for ID in dico_mots:
    if len(dico_mots[ID]) != 1:
        lMax = max(lMax, len(ID))
        dico_anag[ID] = dico_mots[ID][:]
        
##print(len(dico_mots))
##print(len(dico_anag))
liste_carr = []
for i in range(int((10**lMax)**0.5)):
    liste_carr.append(i**2)

dico_carr2 = {}
for l in liste_carr:
    clef = ''.join(sorted(str(l)))
    if clef not in dico_carr2:
        dico_carr2[clef] = []
    dico_carr2[clef].append(l)

dico_carr = {}
for ID in dico_carr2:
    if len(dico_carr2[ID]) != 1:
        lMax = max(lMax, len(ID))
        dico_carr[ID] = dico_carr2[ID][:]


def convertit(nb, mot1, mot2):
    dico1 = {}
    dico2 = {}
    strnb = str(nb)
    for i, c in enumerate(mot1):
        dico1[c] = strnb[i]
        dico2[strnb[i]] = c

    if ''.join([dico1[c] for c in mot1]) == strnb:
        if ''.join([dico2[c] for c in strnb]) == mot1:
            return int(''.join([dico1[c] for c in mot2]))
        else:
            return -1
    else:
        return -1
    

carrMax = 0
for id_NB in dico_carr:
    for id_mot in dico_anag:
        if len(id_NB) == len(id_mot):
            for i in range(len(dico_anag[id_mot])-1):
                for j in range(i+1, len(dico_anag[id_mot])):
                    for nb in dico_carr[id_NB]:
                        val = convertit(nb, dico_anag[id_mot][i],dico_anag[id_mot][j])
                        if val in dico_carr[id_NB]:
                            print(dico_anag[id_mot][i],dico_anag[id_mot][j], nb, val)
                            carrMax = max(carrMax, nb, val)
                                

print(carrMax)
                            
                        
            

            





