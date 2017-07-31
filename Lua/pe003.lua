--[[
PE003.lua
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
--]]


--[[
function ppfp(n) --renvoie le plus petit facteur premier
  for i=2,n^(0.5),1 do
    if n%i==0 then return i end
  end
  return n
end
--]]

dofile("DIVlib.lua")

nombre=600851475143
--print("pgfp=",pgfp(nombre))

print("Decomposition de " .. nombre .. ":")

local t={}

t=decompPrime(nombre,t)
print("-->" .. nombre .. " = " .. table.concat(t," ; "))

