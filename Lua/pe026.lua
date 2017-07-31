--[[
PE026.lua

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7
has a 6-digit recurring cycle.

Find the value of d <1000 for which 1/d contains the longest recurring cycle in its decimal
fraction part.

--]]




function lgCycle(a,b) --a/b
  local t={}
  local reste=a%b
  local compteur=1
  while (t[reste]==nil and reste~=0) do
    t[reste]=compteur
    reste=(10*reste)%b
    compteur=compteur+1
  end
  
  if reste==0 then
    return 0
  else
    return compteur-t[reste]
  end
end


max=0
d=0
for i=1,1000 do
  local lg=lgCycle(1,i)
  if lg>max then
    max=lg
    d=i
  end
end
print(d,max)



