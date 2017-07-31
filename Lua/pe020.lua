--[[
pe020.lua
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
--]]

dofile("GNlib.lua")

a="1"
a=StringtoGN(a)
for i=1,100,1 do
  a=GN_mult(a,StringtoGN(tostring(i)))
end

 

a=GNtoString(a)


somme=0
for i=1,string.len(a) do
  somme=somme+tonumber(string.sub(a,i,i))
  
end
print(a,somme)


