--[[
PE062.lua

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits
which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

--]]

dofile("DIVlib.lua")
-- includes quickSort(t,s_i,e_i)

-----------
function ordre(n) -- retourne un nombre dont les digits sont ordonnés dans l'odre décroissant
  local i=1
  local t={}
  while n/10>0 do
    t[i]=n%10
    n=(n-n%10)/10
    i=i+1
  end
  t=quickSort(t,1,i-1)
  n=0
  for j=1,i-1 do
    --print(t[j])
    n=n+10^(j-1)*t[j]
  end
  return n
end
--

--[[
i=0
tab={}
id=0
repeat
  i=i+1
  id=ordre(i^3)
  if tab[id]==nil then
    t={i}
    tab[id]=t
  else
    tab[id][table.maxn(tab[id])+1]=i
  end

until table.maxn(tab[id])==5

--]]


valMax=5
i=0
imax=math.huge
curseur=0
tab={}
tabIDmax={}
idFinal=0

while i<imax do
  i=i+1
  id=ordre(i^3)
  if tab[id]==nil then
    t={i}
    tab[id]=t
  else 
    tab[id][table.maxn(tab[id])+1]=i
  end
  if table.maxn(tab[id])==valMax then
    tabIDmax[table.maxn(tabIDmax)+1]=math.floor(id)
    if curseur==0 then
      curseur=curseur+1
      imax=(tabIDmax[curseur])^(1/3)
    end
  elseif table.maxn(tab[id])==valMax+1 then
    print("**")
    curseur=curseur+1
    imax=(tabIDmax[curseur])^(1/3)
  end
end

id=tabIDmax[curseur]
for i=1,table.maxn(tab[id]) do
  print(i,tab[id][i],tab[id][i]^3)
end
print("-->",id, tab[id][1]^3)





















