--[[
PE039.lua
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there
are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p<=1000, is the number of solutions maximised?
--]]


function nbSol(p)
  local nb=0
  for a=1,math.floor(p-1)/3 do
    local b=math.floor(p*(p-2*a)/(2*(p-a)))
    local c=math.floor(p-a-b)
    if c^2==a^2+b^2 then
      nb=nb+1
      --print(a,b,c)
    end
  end
  return nb
end

valMax=0
nbMax=0
for i=1,1000 do
  local nb=nbSol(i)
  if nb>nbMax then
    nbMax,valMax=nb,i
  end
end

print("-->",valMax)
