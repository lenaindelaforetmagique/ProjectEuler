--[[
PE071.lua
Consider the fraction, n/d, where n and d are positive integers. If nd and HCF(n,d)=1, it is
called a reduced proper fraction.

If we list the set of reduced proper fractions for d  8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6,
6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d  1,000,000 in ascending order of size,
find the numerator of the fraction immediately to the left of 3/7.

--]]

--coins={1,2,5,10,20,50,100,200}

dofile("DIVlib.lua")

d=1e6
frac=3/7

valMax={0}
valMax[0]=0



for i=1,d do
  local t={}
  t[1]=math.floor(frac*i)
  t[2]=i/pgcd(t[1],i)
  t[1]=t[1]/pgcd(t[1],i)
  t[0]=t[1]/t[2]
  if t[0]>valMax[0] and t[0]<frac then
    valMax=t
  end
end

print(table.concat(valMax,"/"))










