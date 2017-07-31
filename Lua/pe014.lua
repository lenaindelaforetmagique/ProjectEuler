--[[
PE014.lua
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting
numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

--]]


tab={}
tab[1]=1

function C_next(a)
  if a%2==0 then
    return a/2
  else
    return 3*a+1
  end
end


--collatz(n)=1+(collatz(suivant) or liste[suivant])

function lgChemin(a)
  if tab[a]==nil then
    tab[a]=1+lgChemin(C_next(a))
  end
  return tab[a]
end

valMax=0
startNo=1
for i=1,1e6-1,1 do
  local val=lgChemin(i)
  if val>valMax then
    valMax=val
    startNo=i
  end
  --print(i,tab[i])
end

print(startNo,tab[startNo])

