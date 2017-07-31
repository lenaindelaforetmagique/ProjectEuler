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
coins={}
NUMBER=100
for i=1,NUMBER-1 do
  coins[i]=i
end

memoization={}


function nbCombi(S,e_t)
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
  if e_t==1 then
    if S%t[e_t]==0 then
      return 1
    else
      return 0
    end
  else
    local nb=0
    local imax=math.floor(S/t[e_t])
    local somme=0
    for i=0,imax do
      somme=somme+nbCombi_old(S-i*t[e_t],t,e_t-1)
    
    end
    return somme
  end
end

print("-->new",nbCombi(NUMBER,table.maxn(coins)))


--print("-->old",nbCombi_old(NUMBER,coins,table.maxn(coins)))























