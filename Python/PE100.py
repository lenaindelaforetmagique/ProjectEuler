#PE 100
# b*(b-1)/((b+r)*(b+r-1))
# = b*(b-1)/(b*(b-1) + r*(2*b-1+r)) = 1/2
# -> b*(b-1) = r*(2*b-1+r)
# <=> r**2 + r*(2*b-1) - b*(b-1)
# => r = (sqrt((2*b-1)**2 + 4*b*(b-1)) - (2*b-1))/2
# => (2*b-1)**2 + 4*b*(b-1) = X**2, impair
#<=> X**2 - 2*(2*b-1)**2 = -1
#<=> X**2 - 2*Y**2 = -1
# -> Y == PellNumber impairs

PellNumbers = [0, 1]
def nextPN():
    global PellNumbers
    PellNumbers.append(2*PellNumbers[-1]+PellNumbers[-2])
    if PellNumbers[-1]%2 == 0:
        PellNumbers.append(2*PellNumbers[-1]+PellNumbers[-2])
    return PellNumbers[-1]

def racine(N):
##    print(N)
##    print(N**0.5)
    return int(N**0.5)

b = 85
r = 35
while b+r< 10**12:
    Y = nextPN()
    X = racine(2*Y**2-1)
    b = (Y+1)//2
    r = (X - Y)//2


print(r+b)
print("-->", b)
# verif :
#print(b*(b-1)/((b+r)*(b+r-1)))
