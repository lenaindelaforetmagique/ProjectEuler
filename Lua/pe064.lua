--[[
PE064.lua



--]]

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
  print(n,a)
  local cpt=0
  repeat
    cpt=cpt+1
    a,t=suivant(t,n)
    local s2=table.concat(t," ")
    print(n,a)
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

print(lgCycle(313))




