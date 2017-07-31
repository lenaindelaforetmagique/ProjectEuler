--[[
PE042.lua
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten
triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and
adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
two-thousand common English words, how many are triangle words?
--]]


function score(s)
  local score=0
  for i=1,string.len(s),1 do
    score=score+string.byte(s,i)-string.byte('A')+1
  end
  return score
end
--


-- 1 charger le fichier
io.input("pe042_words.txt",r)
line=nil
fich=""

for line in io.lines() do
  fich=fich .. line
end

io.close()

fich=string.gsub(fich,"\n","")
fich=string.gsub(fich,"\"","")
lgFich=string.len(fich)
t={}
c_s=1
c_e=string.find(fich,',') --,c_s)
i=1
while c_e>c_s do
  t[i]=string.sub(fich,c_s,c_e-1)
  c_s=c_e+1
  c_e=string.find(fich,',',c_s) or lgFich+1
  i=i+1
end

taille=table.maxn(t)

-- 2 calcul des scores et du max
max=0
for i=1,taille do
  t[i]=score(t[i])
  max=math.max(t[i],max)
end

-- 3 calcul des nbres triangles
i=1
triangle={}
while i*(i+1)/2<max do
  triangle[i*(i+1)/2]=true
  i=i+1
end

-- 4 compte les mots "triangle"
nombre=0
for i=1,taille do
  if triangle[t[i]] then
    nombre=nombre+1
  end
end
print("-->",nombre)













