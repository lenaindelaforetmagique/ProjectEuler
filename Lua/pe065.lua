--[[
PE065.lua



--]]

dofile("GNlib.lua")

dofile("DIVlib.lua")
-- includes pgcd(a,b)

function suivant(t,n) -- table des valeurs pour racine de a
  local a=0
  a=math.floor((t[1]*math.sqrt(n)+t[2])/t[3])
  t[2]=t[2]-a*t[3]
  --inversion de la fraction
  local t2={}
  t2[1]=t[3]*t[1]
  t2[2]=-1*t[3]*t[2]
  t2[3]=t[1]^2*n-t[2]^2

  local dc=pgcd(t2[1],pgcd(t2[2],t2[3]))
  t2[1]=t2[1]/dc
  t2[2]=t2[2]/dc
  t2[3]=t2[3]/dc
  return a,t2 --table.concat(t2," ")
end


function lgCycle(n)
  local t={1,0,1}
  local a=0
  a,t=suivant(t,n)
  local s1=table.concat(t," ")
  --print(n,a)
  local cpt=0
  repeat
    cpt=cpt+1
    a,t=suivant(t,n)
    local s2=table.concat(t," ")
    --print(n,a)
  until s1==s2
  return cpt
end


--[[
local cpt=0
for i=1,1e4 do
  if math.floor(math.sqrt(i))^2~=i then
    --print(i,lgCycle(i))
    if lgCycle(i)%2==1 then
      cpt=cpt+1
    end
  end
end

print("-->",cpt)
--]]



function F(a,t1)
  local t2={}
  t2[1]=t1[2]
  t2[2]=a*t1[2]+t1[1]
  --local dc=pgcd(t2[1],t2[2])
  --t2[1]=t2[1]/dc
  --t2[2]=t2[2]/dc
  return t2
end
--
function F_GN(a,t1)
  local t2={}
  t2[1]=t1[2]
  t2[2]=GN_add(GN_mult(a,t1[2]),t1[1])
  return t2
end
--

function rac2(NB)
  local tab={}
  local i=1
  tab[i]=1
  for i=2,NB do
    tab[i]=2
  end
  local t={1,tab[NB]}
  for i=NB-1,1,-1 do
    t=F(tab[i],t)
  end
  t[1],t[2]=t[2],t[1]
  return t
end

function exp(NB)
  local tab={}
  local i=1
  tab[i]=2
  for i=2,NB do
    tab[i]=1
  end
  for i=3,NB,3 do
    tab[i]=2*i/3
  end
  print(table.concat(tab,","))
  local t={1,tab[NB]}
  for i=NB-1,1,-1 do
    t=F(tab[i],t)
  end
  t[1],t[2]=t[2],t[1]
  return t
end
--

function exp_GN(NB)
  local tab={}
  local i=1
  tab[i]=2
  for i=2,NB do
    tab[i]=1
  end
  for i=3,NB,3 do
    tab[i]=2*i/3
  end
  --print(table.concat(tab,","))
  local t={{1},{tab[NB]}}
  for i=NB-1,1,-1 do
    t=F_GN({tab[i]},t)
  end
  t[1],t[2]=t[2],t[1]
  return t
end


local a={}
for i=1,100 do
  --print(table.concat(exp_GN(i),"/"))
  
  a=exp_GN(i)
  --print(table.concat(a[1]) .. "/" ..table.concat(a[2]))  
end

local s=table.concat(a[1])

local somme=0
for i=1,string.len(s) do
somme=somme+tonumber(string.sub(s,i,i))
end
print("-->",somme)

--











