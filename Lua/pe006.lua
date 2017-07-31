--[[
PE006.lua
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
]]


function sumNb(a,b)
  n=0
  for i=a,b,1 do
    n=n+i
  end
  return n
end

function sumCarres(a,b)
  n=0
  for i=a,b,1 do
    n=n+i^2
  end
  return n
end


a=1
b=100
print(sumNb(a,b)^2-sumCarres(a,b))