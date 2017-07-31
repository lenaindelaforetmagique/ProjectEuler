--[[
PE243.lua

A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d1 proper fractions; for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its
proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

--]]

-- se référer au PE069 et phi(n)/n car R(n)=phi(n)/n


dofile("DIVlib.lua")
-- includes pgcd(a,b)
-- includes nPrime(n,t)


function R(d)
  local cpt=1
  for i=2,d-1 do
    if pgcd(i,d)==1 then
      cpt=cpt+1
    end
  end
  return cpt/(d-1)
end
--

function R2(d)
  local cpt=1
  for i=2,d-1 do
    if isResilient(i,d) then
      cpt=cpt+1
    end
  end
  return cpt/(d-1)
end


i=2
--[[
while R(i)>=15499/94744 do
  i=i+1
  
  print(i,R(i))
end

print("-->",i)
--]]

function isResilient(a,b)
  local i=1
  for i=1,math.min(table.maxn(nbMem[a]),table.maxn(nbMem[b])) do
    if nbMem[a][i]>0 and nbMem[b][i]>0 then
      return false
    end
  end
  return true
end


--[[
primeMem={}
nbMem={}

primeMax=nPrime(50,primeMem)
i=1
repeat
  i=i+1
  if i>primeMax then
    print(i)
    primeMax=nPrime(table.maxn(primeMem)*2,primeMem)
  end
  nbMem[i]=decomp(i,primeMem)
  --print(i)
until R2(i)<15499/94744 --4/10
print("-->",i)


--]]



function phi(t,fact) -- retourne le nb de nbres premiers inférieurs à un nombre décomposé en fact premiers
  local result=1
  for i=1,t[0] do
    if t[i]~=0 then
      result=result*(fact[i]-1)*fact[i]^(t[i]-1)
    end
  end
  return result
end
--

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
  t[0]=i-1 -- on stocke en 0 le no du dernier facteur premier
  return t
end
--


prime={}
iMax=100
_=nPrime(iMax,prime)
i=0
A=1
B=1
repeat
  i=i+1

  if i>iMax then
    iMax=iMax*2
    local _=nPrime(iMax,prime)
  end
  A=A*prime[i]
  B=B*(1-1/prime[i])
  print(i,prime[i],A,phi(decomp(A,prime),prime))
  --print("-->",A,":",phi(decomp(A,prime),prime)/(A-1),"<",15499/94744)  
until phi(decomp(A,prime),prime)/(A-1)<15499/94744

print("-->",A,":",phi(decomp(A,prime),prime)/(A-1),"<",15499/94744)
t=decomp(i,prime)
a=94744
b=prime[t[0]+1]

test=4
print("test",phi(decomp(test,prime),prime)/(test-1))


--------
prime={}

_=nPrime(20,prime)

function blah(ratio,list)
  local d,s=1,1
  for i=1,table.maxn(list) do
    d=d*list[i]
    s=s*(list[i]-1)
    for j=2,list[i] do
      print(s,d,j)
      if s*j/(d*j-1)<ratio then
        --print("_-_-_",d*j,s*j/(d*j-1))
        return d*j
      end
    end
  end
  return "beurk"
end


print("--->",blah(15499/94744,prime))
print(table.concat(decomp(blah(15499/94744,prime),prime)))





















