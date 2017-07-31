--[[
PE024.lua
A permutation is an ordered arrangement of objects. For example, 3124 is one possible
permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or
alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012 : pos 0, ordre croissant
021 : 
102
120
201
210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
--]]


dofile("DIVlib.lua")
-- includes quickSort(t)
-- includes nextPerm(t)


function init(a)
  local t={}
  for i=1,a do
    t[i]=i-1
  end
  return t
end

function print_t(t)
  local s=""
  for i=1,table.maxn(t) do
    s=s .. t[i]
  end
  print(s)
  --return s
end

--[[
0123
0132
0213
0231
0312
0321
1023
1032
1203
1230
1302
1320



--]]



tab=init(10)
print_t(tab)
for i=1,1e6-1 do
  nextPerm(tab)
  --print_t(tab)
end

print_t(tab)









