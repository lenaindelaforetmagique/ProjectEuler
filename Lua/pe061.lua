--[[
PE061.lua

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate
(polygonal) numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	1, 3, 6, 10, 15, ...
Square	 	P4,n=n^2	 	1, 4, 9, 16, 25, ...
Pentagonal	P5,n=n(3n-1)/2	1, 5, 12, 22, 35, ...
Hexagonal	P6,n=n(2n-1)	1, 6, 15, 28, 45, ...
Heptagonal	P7,n=n(5n-3)/2	1, 7, 18, 34, 55, ...
Octagonal	P8,n=n(3n-2)	1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

The set is cyclic, in that the last two digits of each number is the first two digits of the
next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882),
is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal
type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a
different number in the set.

--]]

dofile("DIVlib.lua")
-- includes nextPerm(t)

function init(a)
  local t={}
  for i=1,a do
    t[i]=i
  end
  return t
end
--



function Tri(n)
  return n*(n+1)/2
end
--
function Squ(n)
  return n^2
end
--
function Pen(n)
  return n*(3*n-1)/2
end
--
function Hex(n)
  return n*(2*n-1)
end
--
function Hep(n)
  return n*(5*n-3)/2
end
--
function Oct(n)
  return n*(3*n-2)
end
--
P={Tri,Squ,Pen,Hex,Hep,Oct}


NB=6

val={}
for i=1,NB do
  local l={}
  local j=1
  local cpt=0
  while P[i](j)<1e4 do
    if P[i](j)>1e3-1 then
      cpt=cpt+1
      l[cpt]=P[i](j)
    end
    j=j+1
  end
  val[i]=l
  --print(i,table.maxn(val[i]))
end

--print(t[1][1],t[1][table.maxn(t[1])])

function blah(n,t,f,val)
--print("--",n)
  if n==1 then
    for i=1,table.maxn(val[f[n]]) do
      t[n]=val[f[n]][i]
      blah(n+1,t,f,val)
    end
  elseif n<NB then
    for i=1,table.maxn(val[f[n]]) do
      if math.floor(val[f[n]][i]/100)==t[n-1]%100 then
        t[n]=val[f[n]][i]
  --print(table.concat(t,"-"))
        blah(n+1,t,f,val)
      end
    end
  else
    for i=1,table.maxn(val[f[n]]) do
   -- print(i)
      if math.floor(val[f[n]][i]/100)==t[n-1]%100 and math.floor(t[1]/100)==val[f[n]][i]%100 then
        t[n]=val[f[n]][i]
        local somme=0
        for j=1,NB do
          somme=somme+t[j]
        end
        print(table.concat(t,"-"),somme)
      end
    end
  
  end
  t[n]=nil
  
end


func=init(NB)

t={}
cpt=0
repeat
    --print(table.concat(func))
  cpt=cpt+1
  blah(1,t,func,val)
  nextPerm(func)
until cpt>fact(NB)-2
  blah(1,t,func,val)

