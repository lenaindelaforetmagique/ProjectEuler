--[[
PE052.lua

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.

--]]

dofile("DIVlib.lua")
-- includes quickSort(t,s_i,e_i)

-----------
function ordre(n) -- retourne un nombre dont les digits sont ordonnés dans l'odre décroissant
  local i=1
  local t={}
  while n/10>0 do
    t[i]=n%10
    n=(n-n%10)/10
    i=i+1
  end
  t=quickSort(t,1,i-1)
  n=0
  for j=1,i-1 do
    --print(t[j])
    n=n+10^(j-1)*t[j]
  end
  return n
end
--

MultMax=6
notFound=true
i=0


while notFound do
  i=i+1
  local ID=ordre(i)
  local j=2
  while ID==ordre(i*j) and j<=MultMax do
    j=j+1
  end
  if j==MultMax+1 then
    notFound=false
  end
end

print("-->",i,ordre(i))
for j=2,MultMax do
	print(j,j*i,ordre(j*i))
end














