--[[
pe015.lua
Starting in the top left corner of a 22 grid, and only being able to move to the right
and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 2020 grid?
--]]

tab={}

dimH=20
dimV=20

for i=0,dimV,1 do
  local a={}
  for j=0,dimH,1 do
    if i==0 then
    a[j]=1
    elseif j==0 then
      a[j]=1
    else
      a[j]=a[j-1]+tab[i-1][j]
    end
  end
  tab[i]=a
end

print(tab[dimV][dimH])

