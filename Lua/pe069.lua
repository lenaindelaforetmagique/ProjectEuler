--[[
PE069.lua

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the
number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine,
φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	        1	2
3	1,2	        2	1.5
4	1,3	        2       2
5	1,2,3,4	        4        1.25
6	1,5              2	3
7	1,2,3,4,5,6      6	1.1666...
8	1,3,5,7	        4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	        4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n  10.

Find the value of n  1,000,000 for which n/φ(n) is a maximum.
--]]

dofile("DIVlib.lua")
-- includes pgcd(a,b)
-- includes nPrime(n,t)


function decomp(n,div,imax) -- decompose selon une table de diviseurs (ici premiers)
-- imax détermine la position au delà de laquelle on ne fait plus de vérif (évite de fouiller
-- intégralement la table des diviseurs et un calcul de table.maxn)
  local imax=imax or table.maxn(div)
  local t={}
  --for i=1,table.maxn(div) do
  local i=1
  repeat
  --for i=1,imax do
    t[i]=0
    while n%div[i]==0 do
      t[i]=t[i]+1
      n=n/div[i]
    end
    i=i+1
  until n==1 or i>imax
  --end
  t[0]=i-1 -- on stocke en 0 le nb de facteurs premiers différents
  return t
end
--


function phi(t)
  local result=1
  for i=1,t[0] do
    if t[i]~=0 then
      result=result*(prime[i]-1)*prime[i]^(t[i]-1)
    end
  end
  return result
end
--


NB=1e6

--[[ SOLUTION CONVERGENTE MAIS TRES LENTE !!! 

tab={}
prime={}

imax=1
while nPrime(imax,prime)<NB do
  imax=imax*2
end
print("--",imax)

--_=nPrime(NB,prime)

ratioMax=0
nMax=0
for i=2,NB do
  print(i)
  local fi=phi(decomp(i,prime,imax))
  if i/fi>ratioMax then
    ratioMax=i/fi
    nMax=i
  end
end

print("-->",nMax)

--]]


prime={}
_=nPrime(50,prime)

n=1
i=1
while n*prime[i]<NB do
print(n, prime[i])
  n=n*prime[i]
  i=i+1
end

print("-->",n) --,n/phi(decomp(n,prime,10)))

print("---->",prime[50])













