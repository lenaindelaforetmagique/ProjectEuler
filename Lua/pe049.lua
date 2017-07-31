--[[
PE049.lua
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is
unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this
property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
--]]

--[[commentaires perso:
  la suppression des elements ne sert à rien > le test peut être intégré dans is3Seq()
  -> conservé pour l'exemple d'élimination d'éléments d'une table.
--]]

dofile("DIVlib.lua")
-- include nextPrime(n)
-- include isPrime(n)





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
function is3Seq(t)
  for i=1,table.maxn(t)-2 do -- indice du premier nbre
    for j=i+2,table.maxn(t) do
      for k=i+1,j-1 do
        if t[k]==(t[i]+t[j])/2 then
          return true,t[i] .. t[k] .. t[j]
        end
      end
    end
  end
  return false,nil
end
--





-- écriture de la table des nbres premiers
NBMAX=1e4

n=nextPrime(1000)
i=0
prime={}
while n<NBMAX do
  --print(n)
  i=i+1
  prime[i]=n
  n=nextPrime(n)
end

nbPrime=table.maxn(prime)
print("nbPrime",nbPrime)



--[[
Identifications des permutations de nbres premiers :
  id=chiffres du nombre premier triés dans l'ordre décroissant
  tab[id] contient tous les nombres premiers de même id
  index[i] contient la liste des identifiants
--]] 
index={}
tab={}
lgIndex=0

for i=1,nbPrime do
  --print(i,prime[i])
  local id=ordre(prime[i])
  if tab[id]==nil then
    tab[id]={prime[i]}
    lgIndex=lgIndex+1
    index[lgIndex]=id
  else
    tab[id][table.maxn(tab[id])+1]=prime[i]
  end
end

print("nbId",lgIndex)

-- suppression de l'index des séries non intéressantes (moins de 3 nbres)
for i=1,lgIndex do
  if table.maxn(tab[index[i]])<3 then
    index[i]=NBMAX
    lgIndex=lgIndex-1
  end
end

print("lgIndex",lgIndex)
print("tblesize avant tri",table.maxn(index))
quickSort(index)
-- supprime de l'index les elements en trop
for i=lgIndex+1,table.maxn(index) do
  index[i]=nil
end
print("tblesize apres tri",table.maxn(index))






for i=1,lgIndex do
  local s=index[i] ..":"
  for j=1,table.maxn(tab[index[i]]) do
    s=s .. tab[index[i]][j] .."-"
  end
  print(s)

end


for i=1,lgIndex do
  test,chaine=is3Seq(tab[index[i]])
  if test then
    print(chaine)
  end
end



















