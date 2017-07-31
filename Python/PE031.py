# PE 31


pounds=[1,2,5,10,20,50,100,200]

# 9)
##def detailAppoints(M,devises):
##    s=0
##    if len(devises)==0:
##        if M==0:
##            return 1
##        else:
##            return 0
##    else:
##        for i in range(0,M//devises[-1]+1):
##            s+=detailAppoints(M-i*devises[-1],devises[:-1])
##        # print(s)
##        return s


##print(detailAppoints(200,pounds))

def test2(M,devises):
    t=[0 for i in range(M+1)]
    t[0]=1

    for billet in devises:
        for i in range(M+1):
##        print(i)
            if i-billet >= 0:
                t[i]+=t[i-billet]

##    for i,nb in enumerate(t):
##        print(i,nb)
    return t[M]





nbre=200
pieces=[i for i in range(1,nbre)]
print(test2(nbre,pieces))
