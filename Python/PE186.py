##Connectedness of a network
##Problem 186
##
##Here are the records from a busy telephone system with one million users:
##RecNr	Caller	Called
##1	200007	100053
##2	600183	500439
##3	600863	701497
##...	...	...
##
##The telephone number of the caller and the called number in record n are Caller(n) = S2n-1 and Called(n) = S2n where S1,2,3,... come from the "Lagged Fibonacci Generator":
##
##For 1 ≤ k ≤ 55, Sk = [100003 - 200003k + 300007k3] (modulo 1000000)
##For 56 ≤ k, Sk = [Sk-24 + Sk-55] (modulo 1000000)
##
##If Caller(n) = Called(n) then the user is assumed to have misdialled and the call fails; otherwise the call is successful.
##
##From the start of the records, we say that any pair of users X and Y are friends if X calls Y or vice-versa. Similarly, X is a friend of a friend of Z if X is a friend of Y and Y is a friend of Z; and so on for longer chains.
##
##The Prime Minister's phone number is 524287. After how many successful calls, not counting misdials, will 99% of the users (including the PM) be a friend, or a friend of a friend etc., of the Prime Minister?


memory_S = {}



def S(k):
    if k <=0:
        return None
    elif k not in memory_S.keys():
        if k <= 55:
            memory_S[k] = (100003 - 200003*k + 300007* k**3) % 1000000
        else:
            memory_S[k] = (S(k-24) + S(k-55)) % 1000000

    return memory_S[k]
        
k=1
while S(k) != 524287:
    #print(k)
    k+=1

print(k, S(k))
##print(S(32))
##    
##for i in range(57):
##    print(i, S(i))
    
