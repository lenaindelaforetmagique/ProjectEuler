--[[
PE031.lua
In England the currency is made up of pound, £, and pence, p, and there are eight coins in
general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1£1 + 150p + 220p + 15p + 12p + 31p
How many different ways can £2 be made using any number of coins?
--]]

coins={1,2,5,10,20,50,100,200}


function nbCombi(S,t,e_t)
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
      somme=somme+nbCombi(S-i*t[e_t],t,e_t-1)
    
    end
    return somme
  end
end

print(nbCombi(200,coins,8))
























