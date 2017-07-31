--[[
pe016.lua
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
--]]

dofile("GNlib.lua")


a="1"
a=StringtoGN(a)
for i=1,1000,1 do
  a=GN_add(a,a)
end

 

a=GNtoString(a)


somme=0
for i=1,string.len(a) do
  somme=somme+tonumber(string.sub(a,i,i))
  
end
print(a,somme)

a=StringtoGN("1")
b=StringtoGN("2")

for i=1,1000,1 do
  --print(i,GNtoString(e),e)
  a=GN_mult(a,b)
  --print(e)
end
a=GNtoString(a)
print(a)



