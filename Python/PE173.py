## PE 173

def calc(lint, n):
    s = 0
    for i in range(1, n+1):
        s += 4*(lint-1 +2*i)
    return s


vmax = 10**6
s = 0
for lint in range(1, vmax//4 -1+1):
    nmax = int((-lint+(lint**2 + vmax)**0.5)/2)
    #print(lint, nmax, calc(lint, nmax))
    s += nmax

print(s)

