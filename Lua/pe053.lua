--[[
PE053.lua

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	
n!
r!(nr)!
,where r  n, n! = n(n1)...321, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?
--]]


dofile("DIVlib.lua")
-- includes nextPrime(n)
-- inculdes isPrime(n)
--decomposition en facteurs premiers

function prime_generator(min,max) -- generates all primes in [min,max]
  local t={}
  local n=nextPrime(min-1)
  local i=0
  while n<=max do
    i=i+1
    t[i]=n
    n=nextPrime(n)
  end
  return t
end
--

function decomp(n,div) -- decompose selon une table de diviseurs (ici premiers)
  local t={}
  for i=1,table.maxn(div) do
    t[i]=0
    while n%div[i]==0 do
      t[i]=t[i]+1
      n=n/div[i]
    end
  end
  return t
end
--

function tableToString(t)
  local s=""
  for i=1,table.maxn(t) do
    s=(t[i] or '_') .. s
  end
  return s
end
--

function prod_decomp(t1,t2)
  local t={}
  for i=1,table.maxn(t1) do
    t[i]=t1[i]+t2[i]
  end
  return t
end
--

function div_decomp(t1,t2)
  local t={}
  for i=1,table.maxn(t1) do
    t[i]=t1[i]-t2[i]
  end
  return t
end
--


function C_n_k(n,k)
  local t=tab[1]
  for i=1,n do
    t=prod_decomp(t,tab[i])
  end
  for i=1,k do
    t=div_decomp(t,tab[i])
  end
  for i=1,n-k do
    t=div_decomp(t,tab[i])
  end
  return t
end
--


function decompToVal(t,div)
  local val=1
  for i=1,table.maxn(div) do
    val=val*div[i]^t[i]
  end
  return val
end
--


prime=prime_generator(1,100)

tab={}
for i=1,100 do
  tab[i]=decomp(i,prime)
  --print(tableToString(tab[i]))
end
--


cpt=0
for n=1,100 do
  for k=1,n do
    if decompToVal(C_n_k(n,k),prime)>1e6 then
      cpt=cpt+1
    end
  end
end

print("-->",cpt)
--decompToVal(C_n_k(23,10),prime))















