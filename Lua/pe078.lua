--[[
PE078.lua
-->See PE076&31 
Let p(n) represent the number of different ways in which n coins can be separated into piles.
For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.

--]]

--coins={1,2,5,10,20,50,100,200}

dofile("GNlib.lua")



function nbCombi_GN(S,e_t)
  if memoization[S]==nil then
    memoization[S]={}
  elseif memoization[S][e_t]~=nil then
    return memoization[S][e_t]
  end
  if e_t==1 then
    if S%coins[e_t]==0 then
      return {1}
    else
      return {0}
    end
  else
    local nb=0
    local imax=math.floor(S/coins[e_t])
    local somme={0}
    for i=0,imax do
      somme=GN_add(somme,nbCombi_GN(S-i*coins[e_t],e_t-1))
    end
    memoization[S][e_t]=somme
    return somme
  end
end
--


coins={}
memoization={}

--55374
i=0
repeat
  i=i+1
  --print(i)
  coins[i]=i
  print("-->",i,nbCombi_GN(i,i)[1])
until i==30 --nbCombi_GN(i,i)[1]%1e3==0


print("-->",i,nbCombi_GN(i,i)[1])


