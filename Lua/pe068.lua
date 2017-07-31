--[[
PE068.lua


--]]

dofile("GNlib.lua")
dofile("DIVlib.lua")
-- includes nextPerm(t)
-- includes fact(n)



function init(a)
  local t={}
  for i=1,a do
    t[i]=i
  end
  return t
end
--

function testPerm(t,n)
  local test=true
  -- test du nb mini en premier
  for i=2,n do
    test=test and t[1]<t[i]
  end
  -- test de somme
  if test then
    local somme=t[1]+t[1+n]+t[1+n+1]
    for i=2,n-1 do
      test=test and somme==t[i]+t[i+n]+t[i+n+1]
    end
    test=test and somme==t[n]+t[n+n]+t[n+1]
  end
  return test
end
--

function ID(t,n)
  local s=""
  for i=1,n-1 do
    s=s .. t[i] .. t[i+n] .. t[i+n+1]
  end
    s=s .. t[n] .. t[n+n] .. t[n+1]
  return s
end
--





t={}
NB=10
t=init(NB)
stock={}
cpt=0
for i=1,fact(NB)-1 do
--for i=1,10-1 do
  if testPerm(t,NB/2) then
    local s=ID(t,NB/2)
    print(s)
    if string.len(s)==16 then
      cpt=cpt+1
      stock[cpt]=StringtoGN(s)
    end
  end
  nextPerm(t)
  
end
if testPerm(t,NB/2) then
    local s=ID(t,NB/2)
    print(s)
    if string.len(s)==16 then
      cpt=cpt+1
      stock[cpt]=StringtoGN(s)
    end
end

idMax=1
for i=2,cpt do
  if GN_cmpr(stock[i],stock[idMax])==1 then
    idMax=i
  end
end

  
print("-->",GNtoString(stock[idMax]))



