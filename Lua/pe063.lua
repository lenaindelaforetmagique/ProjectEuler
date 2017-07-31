--[[
PE063.lua

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number,
134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

--]]

dofile("DIVlib.lua")
-- includes quickSort(t)

cpt=0
t={}

for i=1,9 do
  local n=1
  while (n-1)*math.log(10)<=n*math.log(i) do
    --print(n,i^n)
    cpt=cpt+1
    t[cpt]=i^n
    n=n+1
  end
end

quickSort(t)

for i=table.maxn(t),2,-1 do
  if t[i]==t[i-1] then
    table.remove(t,i)
  end
end
print("-->",#t)


