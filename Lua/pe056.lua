--[[
PE056.lua
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost
unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the
digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
--]]

dofile("GNlib.lua")


max=0
for a=1,99 do
  local GN_a={}
  GN_a[1]=a
  local GN_ap={}
  GN_ap[1]=1
  for b=1,99 do
    GN_ap=GN_mult(GN_a,GN_ap)
    max=math.max(max,GN_sumDigit(GN_ap))
  end
end

print("-->",max)
