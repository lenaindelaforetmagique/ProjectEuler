--[[
PE072.lua
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is
called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

--]]


--faire un test sur le pgcd de chaque paire : si égal 1 > +1 au compteur, sinon, on ne compte pas.

dofile("DIVlib.lua")

d=1e4
compteur=0
---[[
for i=1,d do
  compteur=0
  if i%2==0 then
    pas=2
  else
    pas=1
  end
  for j=1,i-1,pas do
    if pgcd(i,j)==1 then
      -- print(j,"/",i)
      compteur=compteur+1
    end
  end
  print("i=",i,"cpt=",compteur)
end


print("-->",compteur)

--]]


--[[
function isMultiple(nombre,t)
  for i=1,table.maxn(t) do
    if nombre%t[i]==0 then
      return true
    end
  end
  return false
end



d=1e5
cpt=0
for i=2,d do
  local t={}
  t=decompPrime2(i,t)
  --print("-->" .. i .. " = " .. table.concat(t," ; "))
  for j=1,i-1 do
    if isMultiple(j,t)==false then
      cpt=cpt+1
      --print(j)
    end
  end
  
  

end

  print("-->" .. d .. " = " .. cpt )--table.concat(t," ; "))


--]]












