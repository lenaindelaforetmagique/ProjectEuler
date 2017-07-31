--[[
PE048.lua

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

--]]


dofile("GNlib.lua")

somme={0} --StringtoGN("0")

for i=1,1000 do
	print(i)
	local nbre={i}
  somme=GN_add(somme,GN_pow(nbre,i))
end

somme=GNtoString(somme)

somme=string.sub(somme,string.len(somme)-9,string.len(somme))

print("-->",somme)
