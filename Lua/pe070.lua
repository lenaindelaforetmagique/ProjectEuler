--[[
PE070.lua

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the
number of positive numbers less than or equal to n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine,
φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1<n<10^7, for which φ(n) is a permutation of n and the ratio n/φ(n)
produces a minimum.

--]]

dofile("DIVlib.lua")
-- includes pgcd(a,b)
-- includes nPrime(n,t)


function decomp(n,div,imax) -- decompose selon une table de diviseurs (ici premiers)
-- imax détermine la position au delà de laquelle on ne fait plus de vérif (évite de fouiller
--intégralement la table des diviseurs et un calcul de table.maxn)
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


function phi(t) -- retourne le nb de nbres premiers inférieurs à un nombre décomposé en fact premiers
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














