--[[
PE076.lua
-->See PE031 
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
--]]

--coins={1,2,5,10,20,50,100,200}

dofile("DIVlib.lua")

function nbCombi__(S,coins,e_t)
print("--")
  if memoization[S]==nil then
    memoization[S]={}
  elseif memoization[S][e_t]~=nil then
    return memoization[S][e_t]
  end
  
  if e_t==1 then
    if S%coins[e_t]==0 then
      return 1
    else
      return 0
    end
    print("---")
  else
    local nb=0
    local imax=math.floor(S/coins[e_t])
    local somme=0
    for i=0,imax do
      somme=somme+nbCombi(S-i*coins[e_t],e_t-1)
    
    end
    memoization[S][e_t]=somme
    return somme
  end
end




function nbCombi_old(S,t,e_t)
  --print(S,e_t,t[e_t])
  --if t[e_t]>S then
  --  print("bla")
  --  return nbCombi_old(S,t,e_t-1)
  --end
    if e_t==1 then
      if S%t[e_t]==0 then
        return 1
      else
        return 0
      end
    else
      local nb=0
      --print("----",e_t)
      local imax=math.floor(S/t[e_t])
      local somme=0
      for i=0,imax do
        somme=somme+nbCombi_old(S-i*t[e_t],t,e_t-1)
      end
      return somme
    end
end





NUMBER=1
prime={}
iMax=100
_=nPrime(iMax,prime)

e_i=1

repeat
  NUMBER=NUMBER+1
  --print(NUMBER,prime[iMax])
  --while NUMBER>prime[iMax] do
  --  iMax=iMax*2
  --  _=nPrime(iMax,prime)
  --end
  
  local memoization={}
  
  while prime[e_i+1]<=NUMBER do
    e_i=e_i+1
  end
  
  print("-",NUMBER,nbCombi_old(NUMBER,prime,e_i),e_i)
  
until nbCombi_old(NUMBER,prime,e_i)>5000

print("-->",NUMBER,nbCombi_old(NUMBER,prime,e_i))






















