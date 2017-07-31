--[[
PE001.lua
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
]]

function pe001(n)
  a=0
  for i=1,n-1,1 do
    if (i%3==0 or i%5==0) then
      --print(i)
      a=a+i
    end
  end
  return a
end

print(pe001(1e6))
