--[[
PE022.lua
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over
five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of
938*53 = 49714.

What is the total of all the name scores in the file?
--]]



function quickSort(t,s_i,e_i)
  s_i=s_i or 1
  e_i=e_i or table.maxn(t)
  
  if s_i>=e_i then return t end
  --print(s_i,e_i)
  
  --local tampon
  local pivot=t[s_i] -- choisi arbitrairement en pos 1
  
  -- calcule la position définitive du pivot
  local posPivot=s_i
  for i=s_i,e_i do
    if pivot>t[i] then posPivot=posPivot+1 end
  end
  -- switch pivot
  t[s_i],t[posPivot]=t[posPivot],t[s_i]
  
  -- ordre
  for i=s_i,posPivot-1 do
    if t[i]>pivot then
      -- i contient la position d'un elt à envoyer de l'autre côté du pivot
      for j=posPivot+1,e_i do
        if t[j]<=pivot then
          -- switch
          t[i],t[j]=t[j],t[i]
        end
      end
    end
  end
  t=quickSort(t,s_i,posPivot-1)
  t=quickSort(t,posPivot+1,e_i)
  
  return t
end
--
function scorePrenom(s)
  local score=0
  for i=1,string.len(s),1 do
    score=score+string.byte(s,i)-string.byte('A')+1
  end
  return score
end
--


-- 1 charger le fichier
io.input("pe022_names.txt",r)
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

-- 2 trier la table
taille=table.maxn(t)
t=quickSort(t)


-- 3 score prénom
somme=0
for i=1,taille do
  somme=somme+i*scorePrenom(t[i])
end
print(somme)
