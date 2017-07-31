--[[
PE051.lua

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine
possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is
the first example having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this
property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
--]]

dofile("DIVlib.lua")
-- includes isPrime(a)
-- includes nextPrime(a)


function mask_generator(n)  -- generates all possible masks
  local t={}
  for i=1,2^n-1 do
    t[i]=numberToTable(i,n,2)
  end
  return t
end
--

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

function numberToTable(a,dim,base) -- put 'a' in a 'dim'-size table in 'base'-value base
  local t={}
  for i=1,dim do
    t[i]=a%base
    a=math.floor(a/base)
  end
  return t
end
--

function isPossiblePattern(maskTable,numberTable) -- checks if mask is valid on number
  if table.maxn(maskTable)~=table.maxn(numberTable) then return false end
  local val=nil
  local test=true
  for i=1,table.maxn(maskTable) do
    if maskTable[i]==1 then
      if val==nil then val=numberTable[i] end
      test=test and val==numberTable[i]
    end
  end
  return test
end
--

function pattern_generator(maskTable,numberTable)
  local s=""
  for i=1,table.maxn(maskTable) do
    if maskTable[i]==0 then
      s=numberTable[i] .. s
    else
      s='*' .. s
    end
  end
  return s
end
--

function tableToString(t)
  local s=""
  for i=1,table.maxn(t) do
    s=t[i] .. s
  end
  return s
end
--



notFound=true
target=8
nbDig=1

while notFound do
  print("NB DIGITS :",nbDig)
  print("Masks ...")
  mask=mask_generator(nbDig)
  print("-->",table.maxn(mask))
  print("Primes ...")
  prime=prime_generator(10^(nbDig-1),10^nbDig-1)
  print("-->",table.maxn(prime))
  -- generation of all patterns
  patterns=nil
  patterns={}
  index={}
  cpt=0

  print("Patterns ...")
  for i=1,table.maxn(prime) do
    local numb=numberToTable(prime[i],nbDig,10)
    for j=1,table.maxn(mask) do
      if isPossiblePattern(mask[j],numb) then
        local pat=pattern_generator(mask[j],numb)
        if patterns[pat]==nil then
          cpt=cpt+1
          index[cpt]=pat
          patterns[pat]=1
        else
          patterns[pat]=patterns[pat]+1
        end
      end
    end
  end
  print("-->",table.maxn(index))

  print("recherche ...")
  for i=1,table.maxn(index) do
    if patterns[index[i]]==target then
      print("-->",index[i])
      pat=index[i]
      for j=0,9 do
        local nb,_=string.gsub(pat,"*",tostring(j))
        if isPrime(tonumber(nb)) then
          print(nb)
        end
      end
      notFound=false
      break
    end
  end
  nbDig=nbDig+1
end









