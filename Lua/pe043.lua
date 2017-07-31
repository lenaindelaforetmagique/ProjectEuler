--[[
PE043.lua

The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
--]]


dofile("DIVlib.lua")
-- includes nextPerm(t)



function extract_t(t,s_i,e_i)
  local a=0
  for i=s_i,e_i do
    a=a+t[i]*10^(e_i-i)
  end
  return a
end
--


tab={0,1,2,3,4,5,6,7,8,9}
div={2,3,5,7,11,13,17}


somme=0
for i=1,10*9*8*7*6*5*4*3*2*1-1 do
  local test=true
  for j=1,7 do
    test=test and extract_t(tab,1+j,1+j+2)%div[j]==0
  end
  if test then
    print(extract_t(tab,1,10))
    somme=somme+extract_t(tab,1,10)
  end
  nextPerm(tab)

end

print("-->",somme)
