--[[
PE066.lua

Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13*180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2*2^2 = 1
2^2 – 3*1^2 = 1
9^2 – 5*4^2 = 1
5^2 – 6*2^2 = 1
8^2 – 7*3^2 = 1

Hence, by considering minimal solutions in x for D<=7, the largest x is obtained when D=5.

Find the value of D<=1000 in minimal solutions of x for which the largest value of x is
obtained.

--]]
-- http://fr.wikipedia.org/wiki/Fraction_continue_d%27un_nombre_quadratique
-- (x/y)^2=1/y^2+D 





dofile("GNlib.lua")


function suivant(t,n) -- table des valeurs pour racine de n
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
--

function lgCycle(n)
  local t={1,0,1}
  local tab={}
  local a=0
  tab[1],t=suivant(t,n)
  local s1=table.concat(t," ")
  --print(n,a)
  local cpt=0
  repeat
    cpt=cpt+1
    tab[cpt+1],t=suivant(t,n)
    local s2=table.concat(t," ")
    --print(n,a)
  until s1==s2
  return cpt,tab
end
--

function F_GN(a,t1)
  local t2={}
  t2[1]=t1[2]
  t2[2]=GN_add(GN_mult(a,t1[2]),t1[1])
  return t2
end
--


function racine_GN(a,NB)
  local tab={}
  --local i=1
  local lg,t=lgCycle(a)
  --print("------",table.concat(t,"-"),lg)
  tab[1]=t[1]
  for i=2,NB do
    tab[i]=t[(i+(lg-2))%lg+2]
  end
  --print(table.concat(tab,","))
  local t={{1},{tab[NB]}}
  for i=NB-1,1,-1 do
    t=F_GN({tab[i]},t)
  end
  t[1],t[2]=t[2],t[1]
  return t
end
--


function firstX(D)
  local i=1
  local a={}
  repeat
    a=racine_GN(D,i)
    local X2=GNtoString(GN_mult(a[1],a[1]))
    local Y2=GNtoString(GN_add({1},GN_mult({D},GN_mult(a[2],a[2]))))
    i=i+1
  until X2==Y2
  return a[1]
end
--


maxGN={0}
maxD=0
for i=1,1000 do
  if math.sqrt(i)%1~=0 then
    local x={}
    x=firstX(i)
    if GN_cmpr(x,maxGN)==1 then
      maxGN=x
      maxD=i
    end
    print(i,GNtoString(x))
  end
end
print("-->",maxD)









