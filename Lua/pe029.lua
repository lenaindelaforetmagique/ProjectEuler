--[[
PE029.lua

Consider all integer combinations of ab for 2=<a=<5 and 2=<b=<5:

2^2=4, 2^3=8, 2^4=16, 2^5=32
3^2=9, 3^3=27, 3^4=81, 3^5=243
4^2=16, 4^3=64, 4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2=<a=<100 and 2=<b=<100?

--]]



N=100
dofile("GNlib.lua")
dofile("DIVlib.lua")

print("Ecriture...")  
i=1
t={}
for a=2,N do
  local GNa=StringtoGN(tostring(a))
  for b=2,N do
    t[i]=GNtoString(GN_pow(GNa,b))
    --print(t[i])
    i=i+1
  end
end


print("Tri...")
t=quickSort(t)



print("Comptage...")


compteur=1
for i=2,table.maxn(t) do
  --print(t[i])
  if t[i]~=t[i-1] then compteur=compteur+1 end

end

print(compteur)


