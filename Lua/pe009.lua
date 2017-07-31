--[[
PE009.lua
A Pythagorean triplet is a set of three natural numbers, a<b<c, for which, a^2+b^2=c^2
For example 3^2+4^2=9+16=25=5^2
There exists exactly one Pythagorean triplet for which a+b+c=1000
Find the product abc
]]


for c=1000-3,3,-1 do
  for b=c-1,2,-1 do
    a=1000-b-c
      if a^2+b^2==c^2 and a<b then
        stock={a,b,c}
      end
    
    
    
  end


end

a=stock[1]
b=stock[2]
c=stock[3]

print(a,b,c,a+b+c,a^2+b^2,c^2,a*b*c)