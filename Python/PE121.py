##Problem 121
##
##A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.
##
##The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.
##
##If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.
##
##Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.

def fact(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def Cnk(n, k):
    return fact(n) // (fact(k)*fact(n-k))


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

liste = []
nbTours = 15
# on liste les tirages de rouge
for i in range(1, (nbTours-1)//2 + 1):
    combi(nbTours, i)

# liste contient les tirages de rouges menant à la victoire

cpt = 1 # tient compte du coup 0*R
for t in liste:
    v = 1
    for val in t:
        v *= (val + 1)
    cpt += v

print(cpt)

print(fact(nbTours+1)//cpt)
    
    


    
