--[[
PE032.lua
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as
a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once
in your sum.
--]]

--[[
on fait défiler les Permunations lexicographiques du PE24.
le produit a forcément 4 digits > 4 derniers,
les facteurs sont 1*4 digits ou 2*3 digits.
--]]


dofile("DIVlib.lua")
-- includes nextPermt(t)




function print_t(t)
  local s=""
  for i=1,table.maxn(t) do
    s=s .. t[i]
  end
  print(s)
end


--

tab={}
for i=1,9 do
  tab[i]=i
end


function tableToNb(t,s_i,e_i)
  local nombre=""
  for i=s_i,e_i do
    nombre=nombre .. t[i]
  end
  return tonumber(nombre) 
end

--tab=init(10)
compteur=0
stock={}
--print_t(tab)
print("Parcours des pandigitaux ...")
for i=1,9*8*7*6*5*4*3*2*1-1 do
  nextPerm(tab)
  local nC=tableToNb(tab,6,9)
  if tableToNb(tab,1,1)*tableToNb(tab,2,5)==nC then
    compteur=compteur+1
    stock[compteur]=nC
    print(tableToNb(tab,1,1) .. "*" .. tableToNb(tab,2,5) .."="..nC)
  elseif tableToNb(tab,1,2)*tableToNb(tab,3,5)==nC then
    compteur=compteur+1
    stock[compteur]=nC
    print(tableToNb(tab,1,2) .. "*" .. tableToNb(tab,3,5) .."="..nC)
  end
  --print_t(tab)
end

print("Tri des résultats...")
stock=quickSort(stock)
compteur=1
somme=stock[1]
for i=2,table.maxn(stock) do
  if stock[i]~=stock[i-1] then
    compteur=compteur+1
    somme=somme+stock[i]
  end
end

print(table.maxn(stock),compteur,somme)















